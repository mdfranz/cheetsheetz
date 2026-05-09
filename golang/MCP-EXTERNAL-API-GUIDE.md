# Go MCP Server Guide for External API Integrations

## 1) SDK and Core Choice

Use the official Go SDK:

```text
github.com/modelcontextprotocol/go-sdk v1.4.1
```

For tool registration, prefer the raw API:
- `server.AddTool` with `*mcp.Tool` and `json.RawMessage` schemas.
- Use `mcp.AddTool` only when simple typed schemas are enough.

Why: external APIs usually need flexible schemas and nuanced argument parsing.

## 2) Recommended Project Layout

```text
cmd/<app-name>/
  main.go      # config, logging, lock, server creation, run loop
  client.go    # HTTP/auth client and request methods
  tools.go     # tool schemas and handlers
  errors.go    # shared error formatting helpers (optional)
  schemas.go   # reusable JSON schema blocks (optional)
  cache.go     # token/result cache layer (optional)
tools/
  test_mcp.py  # end-to-end MCP test client
go.mod
go.sum           # Go dependency lockfile (always commit)
pyproject.toml   # Python deps for test client
uv.lock          # Python lockfile for test client (always commit)
.gitignore
Makefile
```

Keep server code in one package under `cmd/<app-name>/` until growth justifies splitting.

## 3) `main.go`: Server Bootstrap Pattern

Key rules:
- Use `mcp.StdioTransport`.
- Treat `stdout` as protocol-only (never debug-print to stdout).
- Fail fast on missing required environment variables.

```go
package main

import (
    "context"
    "fmt"
    "io"
    "log/slog"
    "os"
    "strings"
    "syscall"

    "github.com/modelcontextprotocol/go-sdk/mcp"
)

type Config struct {
    APIToken string
    BaseURL  string
    LockFile string
}

func loadConfig() Config {
    token := os.Getenv("APP_API_TOKEN")
    if token == "" {
        fmt.Fprintln(os.Stderr, "APP_API_TOKEN is required")
        os.Exit(1)
    }

    baseURL := os.Getenv("APP_BASE_URL")
    if baseURL == "" {
        baseURL = "https://api.example.com"
    }

    lockFile := os.Getenv("APP_LOCKFILE")
    if lockFile == "" {
        lockFile = "my-mcp-server.lock"
    }

    return Config{APIToken: token, BaseURL: baseURL, LockFile: lockFile}
}

func main() {
    level := slog.LevelInfo
    if os.Getenv("APP_DEBUG") != "" {
        level = slog.LevelDebug
    }

    var logWriter io.Writer = os.Stderr
    if logFile := os.Getenv("APP_LOGFILE"); logFile != "" {
        f, err := os.OpenFile(logFile, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0o644)
        if err == nil {
            defer f.Close()
            logWriter = f
        }
    }
    slog.SetDefault(slog.New(slog.NewTextHandler(logWriter, &slog.HandlerOptions{Level: level})))

    cfg := loadConfig()

    cleanupLock, err := acquireLock(cfg.LockFile)
    if err != nil {
        fmt.Fprintf(os.Stderr, "lock error: %v\n", err)
        os.Exit(1)
    }
    defer cleanupLock()

    client := NewClient(cfg)

    s := mcp.NewServer(&mcp.Implementation{Name: "my-mcp-server", Version: "0.1.0"}, nil)
    registerTools(s, client)

    if err := s.Run(context.Background(), &mcp.StdioTransport{}); err != nil {
        fmt.Fprintf(os.Stderr, "server error: %v\n", err)
        os.Exit(1)
    }
}
```

## 4) Single-Instance PID Lock

MCP clients may spawn your server multiple times (reconnects, IDE restarts). A PID lockfile prevents duplicate instances from competing for stdin/stdout or burning API rate limits.

Key rules:
- Write PID to a `.lock` file on startup; remove it on exit.
- On launch, check if the lockfile's PID is still alive (signal 0 on Unix).
- Remove stale lockfiles automatically.
- Allow disabling via env var (`APP_LOCKFILE=off`) for testing.

```go
const defaultLockFile = "my-mcp-server.lock"

func acquireLock(lockFile string) (func(), error) {
    if strings.EqualFold(lockFile, "off") {
        return func() {}, nil
    }

    // Check if lock file exists and is stale
    if _, err := os.Stat(lockFile); err == nil {
        content, err := os.ReadFile(lockFile)
        if err == nil {
            pid, err := strconv.Atoi(strings.TrimSpace(string(content)))
            if err == nil {
                process, err := os.FindProcess(pid)
                if err == nil {
                    // On Unix, FindProcess always succeeds. Signal 0 checks existence.
                    err = process.Signal(syscall.Signal(0))
                    if err == nil {
                        return nil, fmt.Errorf("another instance is already running (PID: %d)", pid)
                    }
                }
            }
        }
        // Stale or unreadable — safe to remove
        _ = os.Remove(lockFile)
    }

    f, err := os.OpenFile(lockFile, os.O_CREATE|os.O_EXCL|os.O_WRONLY, 0o644)
    if err != nil {
        return nil, fmt.Errorf("could not create lock file: %w", err)
    }
    defer f.Close()

    _, err = f.WriteString(fmt.Sprintf("%d", os.Getpid()))
    if err != nil {
        _ = os.Remove(lockFile)
        return nil, fmt.Errorf("could not write PID to lock file: %w", err)
    }

    return func() {
        slog.Debug("Removing lock file", "path", lockFile)
        _ = os.Remove(lockFile)
    }, nil
}
```

Usage in `main()`:

```go
cleanup, err := acquireLock(cfg.LockFile)
if err != nil {
    fmt.Fprintf(os.Stderr, "lock error: %v\n", err)
    os.Exit(1)
}
defer cleanup()
```

Add `*.lock` to `.gitignore` since lockfiles are runtime artifacts.

## 5) Environment and Config Conventions

Suggested env variables:

| Purpose | Example |
|---|---|
| Required auth | `APP_CLIENT_ID`, `APP_CLIENT_SECRET` or `APP_API_TOKEN` |
| Optional URL override | `APP_BASE_URL` |
| Debug logging | `APP_DEBUG=1` |
| Log file path | `APP_LOGFILE=/tmp/my-mcp.log` |
| Request timeout | `APP_HTTP_TIMEOUT=30s` |
| Lock file path/disable | `APP_LOCKFILE=off` or `APP_LOCKFILE=/tmp/my-mcp.lock` |

Helper parsers are useful for consistency:

```go
func envBool(key string, def bool) bool { /* ... */ }
func envInt(key string, def int) int { /* ... */ }
func envDuration(key string, def time.Duration) time.Duration { /* ... */ }
```

## 6) Auth Patterns for External APIs

Choose one and centralize it in `client.go`:

1. OAuth2 client credentials
- Fetch token from `/oauth/token`.
- Cache token with expiry buffer (for example, refresh 60s early).
- Protect shared token state with `sync.Mutex`.

2. API key
- Send `Authorization: Bearer <key>` or `X-API-Key: <key>`.
- No refresh logic needed.

3. Basic auth
- Send `Authorization: Basic <base64(user:pass)>`.

## 7) `client.go`: External API Client Pattern

Design goals:
- Return raw JSON (`string`) from API calls.
- Always set request timeout.
- Log request/response metadata for observability.
- (Optional) Integrate caching and request coalescing (single-flight) to prevent redundant API calls.

```go
type Client struct {
    httpClient *http.Client
    baseURL    string
    token      string
    mu         sync.Mutex
    // Optional: Add cache and single-flight fields
    // cache      Cache
    // inflightMu sync.Mutex
    // inflight   map[string]*inflightCall
}

func (c *Client) Post(ctx context.Context, path string, payload []byte) (string, error) {
    // Optional: 1. Check cache based on canonicalized path/payload
    // Optional: 2. Coalesce concurrent requests using a single-flight pattern

    req, err := http.NewRequestWithContext(ctx, http.MethodPost, c.baseURL+path, bytes.NewReader(payload))
    if err != nil {
        return "", err
    }

    req.Header.Set("Authorization", "Bearer "+c.token)
    req.Header.Set("Content-Type", "application/json")

    start := time.Now()
    resp, err := c.httpClient.Do(req)
    if err != nil {
        return "", err
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return "", err
    }

    slog.Info("api_request",
        "method", "POST",
        "path", path,
        "status", resp.StatusCode,
        "duration_ms", float64(time.Since(start).Microseconds())/1000,
        "response_bytes", len(body),
    )

    if resp.StatusCode < 200 || resp.StatusCode >= 300 {
        return string(body), fmt.Errorf("http %d: %s", resp.StatusCode, string(body))
    }

    // Optional: 3. Store successful response in cache before returning
    return string(body), nil
}
```

## 8) `tools.go`: Schema and Handler Pattern

Use reusable `json.RawMessage` schemas and explicit argument parsing.

```go
var querySchema = json.RawMessage(`{
  "type": "object",
  "properties": {
    "filter": {"type": "string", "description": "Search expression"},
    "maxCount": {"type": "integer", "minimum": 1, "maximum": 5000}
  }
}`)

func parseArgs(req *mcp.CallToolRequest) (map[string]any, error) {
    args := map[string]any{}
    if req.Params.Arguments == nil {
        return args, nil
    }
    if err := json.Unmarshal(req.Params.Arguments, &args); err != nil {
        return nil, err
    }
    return args, nil
}

func textResult(body string) (*mcp.CallToolResult, error) {
    return &mcp.CallToolResult{Content: []mcp.Content{&mcp.TextContent{Text: body}}}, nil
}

func errorResult(err error) (*mcp.CallToolResult, error) {
    return &mcp.CallToolResult{
        Content: []mcp.Content{&mcp.TextContent{Text: err.Error()}},
        IsError: true,
    }, nil
}
```

Tool registration example:

```go
func registerTools(s *mcp.Server, client *Client) {
    s.AddTool(&mcp.Tool{
        Name:        "api_query",
        Description: "Query the external API. IMPORTANT: project only required fields.",
        InputSchema: querySchema,
    }, func(ctx context.Context, req *mcp.CallToolRequest) (*mcp.CallToolResult, error) {
        args, err := parseArgs(req)
        if err != nil {
            return errorResult(fmt.Errorf("invalid args: %w", err))
        }

        payload := map[string]any{}
        if v, ok := args["filter"].(string); ok {
            payload["filter"] = v
        }
        if v, ok := args["maxCount"].(float64); ok {
            payload["maxCount"] = int(v) // JSON numbers become float64
        }

        raw, _ := json.Marshal(payload)
        body, callErr := client.Post(ctx, "/api/query", raw)
        if callErr != nil {
            return errorResult(callErr)
        }
        return textResult(body)
    })
}
```

Important MCP behavior:
- `req.Params.Arguments` is `json.RawMessage`, not `map[string]any`.
- Numeric args from JSON are `float64` after unmarshal.
- Prefer `errorResult(..., IsError: true)` instead of bubbling raw Go errors from handlers.

## 9) `cache.go`: Caching Pattern (Optional)

When an external API is slow or rate-limited, implement a caching layer. Use a simple interface to allow swappable caching strategies:

```go
type Cache interface {
	Get(key string) (string, bool)
	Set(key string, value string, ttl time.Duration)
}
```

Common implementations:
1.  **MemoryLRUCache**: An in-memory LRU cache using `container/list` and a map. Useful to limit memory usage by setting boundaries on both entry count and total byte size.
2.  **DiskCache**: A persistent cache that stores JSON entries on disk. Keys are hashed (SHA-256) to create a sparse directory structure (e.g., `0a/0a1b2c...`).
3.  **CombinedCache**: A wrapper that provides multi-layer caching (e.g., check memory, then disk; update memory on disk hit).

Cache keys for API requests should include the method, base URL, path, encoded parameters, and a hash of the canonicalized JSON body (for POST).

## 10) External API Reliability Checklist

For production-grade integrations:

1. Timeouts everywhere (`http.Client` and context deadlines).
2. Retries with backoff for 429/5xx (respect `Retry-After` when present).
3. Pagination controls in schemas (`limit`, `offset`, cursors).
4. Request coalescing/single-flight for duplicate in-flight calls.
5. Multi-tenant/scope validation when APIs take org/team/account arrays.
6. Structured logs with tool name, args size, status, latency, and bytes.
7. Optional extraction of API telemetry fields (rate-limit counters, query CPU/wait stats).

## 11) Build/Test Workflow

Minimal `Makefile`:

```makefile
.PHONY: all build run clean test fmt vet install
APP_NAME = my-mcp-server

all: fmt vet build

build:
	go build -o $(APP_NAME) ./cmd/$(APP_NAME)

run:
	go run ./cmd/$(APP_NAME)

test:
	go test -v ./...

fmt:
	go fmt ./...

vet:
	go vet ./...

install: build
	mkdir -p $(HOME)/.local/bin
	cp $(APP_NAME) $(HOME)/.local/bin/

clean:
	rm -f $(APP_NAME)
```

End-to-end MCP test (`tools/test_mcp.py`) using Pydantic AI + stdio:

```python
import asyncio
import os
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

async def main():
    env = os.environ.copy()
    env.setdefault("APP_API_TOKEN", "dummy_token")

    server = MCPServerStdio(
        "go",
        ["run", "./cmd/my-mcp-server"],
        env=env,
        cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
    )

    agent = Agent("google-gla:gemini-3-flash-preview", toolsets=[server])

    async with server:
        result = await agent.run("List available tools and run api_query with filter 'error'.")
        print(result.output)

if __name__ == "__main__":
    asyncio.run(main())
```

Run with:

```bash
uv run tools/test_mcp.py
```

## 12) Practical Design Guidance for LLM-Facing Tools

1. Put concise instructions in tool descriptions (for example, column projection guidance).
2. Add offline/reference tools when the LLM needs schema or syntax context to query an API effectively.
3. Keep responses as raw JSON whenever possible; avoid unnecessary Go struct modeling for pass-through endpoints.
4. Log every tool invocation and API call so debugging is possible when agent behavior changes.

## 13) Quick Start Sequence

1. Scaffold `main.go`, `client.go`, `tools.go`.
2. Implement auth in `client.go`.
3. Add one read-only tool with strict schema.
4. Validate via `go test` + `uv run tools/test_mcp.py`.
5. Add retries, pagination, and telemetry logging before expanding tool count.
