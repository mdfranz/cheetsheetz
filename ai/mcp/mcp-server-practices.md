# Model Context Protocol (MCP) Server Best Practices

This guide outlines the architectural foundations, implementation strategies, and production best practices for building Model Context Protocol (MCP) servers in **Golang** and **Python**.

---

## 1. Core Architecture: MCP vs. REST

MCP represents a shift from "machine-to-machine" (REST) to "AI-to-tool" (MCP) orchestration. While REST focuses on noun-based resources (URLs), MCP focuses on **Capabilities** (Tools, Resources, and Prompts) that an LLM can reason about and execute.

| Feature | REST API | MCP Server |
| :--- | :--- | :--- |
| **Primary User** | Human Developers (writing code) | AI Models (reasoning & tool use) |
| **Statefulness** | Strictly Stateless | Stateful/Contextual Sessions |
| **Discovery** | Static (OpenAPI/Swagger) | Dynamic (Runtime self-description) |
| **Transport** | HTTP/HTTPS | stdio, HTTP/SSE (JSON-RPC 2.0) |

**The Wrapper Pattern:** In production, MCP servers typically act as a "translation layer" that wraps existing REST APIs, converting JSON endpoints into LLM-friendly **Tools**.

---

## 2. Golang Implementation: High-Performance Path

Go is the preferred choice for high-throughput gateways, system-level tools, and "zero-dependency" binary distribution.

### Production-Grade Project Structure
```text
mcp-server-go/
├── cmd/mcp-server/main.go   # Server initialization & entry point
├── internal/handler/        # MCP-specific handlers (Tool/Resource logic)
├── internal/service/        # Pure business logic (agnostic of MCP)
├── pkg/                     # Shared public library code
└── go.mod                   # Official SDK: github.com/modelcontextprotocol/go-sdk
```

### Technical Best Practices (Go)
*   **Concurrency:** MCP calls in Go are handled via goroutines. Since the SDK invokes handlers concurrently, protect shared state (e.g., connection pools) with `sync.Mutex`.
*   **Logging:** **Crucial:** Always redirect logs to `sys.stderr`. Writing to `stdout` in `stdio` transport mode will corrupt the JSON-RPC stream and disconnect the client.
*   **Zero-Dependency Binaries:** Use multi-stage Docker builds to produce tiny, statically linked binaries (~18MB RAM usage).
*   **Type Safety:** Leverage Go structs and the official SDK's built-in JSON-RPC types for strict schema validation.

---

## 3. Python Implementation: Rapid Prototyping Path

Python excels in AI/ML-adjacent logic and offers the fastest development cycle via the `FastMCP` framework.

### Production-Grade Project Structure
```text
mcp-server-python/
├── src/my_server/
│   ├── main.py          # FastMCP instance & registration
│   ├── tools.py         # @mcp.tool decorators
│   └── logic/           # Core logic (e.g., NumPy/Pandas processing)
├── pyproject.toml       # Managed by 'uv' (standard for MCP)
└── .env                 # Environment variables for API keys
```

### Technical Best Practices (Python)
*   **Error Handling:** Never let exceptions bubble up. Catch them and return a `CallToolResult` with `isError=True`. Ensure error messages are "model-friendly" (e.g., "The field 'email' is missing, please provide it").
*   **Async Management:** Use `asyncio` for I/O-bound tool calls. For CPU-bound tasks, offload to a `ProcessPoolExecutor` to avoid blocking the MCP heartbeat.
*   **Dependency Management:** Use [uv](https://github.com/astral-sh/uv) for fast, reproducible builds and isolation.
*   **Validation:** Use `pydantic` (integrated into FastMCP) for strict input validation of tool arguments.

---

## 4. Advanced Patterns & Scaling

### Dynamic Tool Discovery
For servers with hundreds of tools, sending the entire list via `tools/list` will exhaust the LLM's context window.
1.  **Semantic Search Pattern:** Expose a `find_tool` meta-tool that performs a vector search over your tool registry.
2.  **Hierarchical Namespacing:** Use prefixes (e.g., `db:query`, `fs:read`) to allow models to discover capabilities in stages.
3.  **List Changed Notification:** Use `notifications/tools/list_changed` to alert the client when the toolset changes dynamically.

### Resources vs. Tools
*   **Resources:** Use for *contextual data* the model needs to "read" (e.g., `logs://today`, `file://config.json`). They are URI-based and read-only.
*   **Tools:** Use for *actions* the model needs to "perform" (e.g., `delete_user`, `run_query`). They require a JSON Schema for arguments.

---

## 5. Testing Strategy & Quality Assurance

### Local Testing with MCP Inspector
The [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is the official interactive testing tool for MCP servers. Use it to:
- **Validate Tool Schemas:** Ensure tool descriptions, JSON schemas, and argument names are correct
- **Test Tool Execution:** Call tools manually and inspect responses
- **Debug Error Handling:** Verify error messages are clear and model-friendly
- **Protocol Compliance:** Confirm your server responds correctly to all MCP message types

**Before Production:** Run MCP Inspector locally for every server revision to catch integration issues early.

### Transport Protocol Testing
Test across multiple transport protocols (stdio, HTTP, SSE) even if you only plan to use one initially:
- Stdio: Fast for local development and testing
- HTTP/SSE: Necessary for cloud deployments and remote access
- Server behavior should be identical across transports

### CI/CD Integration
Implement automated testing pipelines that run:
- **Functional Tests:** Unit tests for each tool's business logic
- **Integration Tests:** Full MCP message flow from tool list through tool execution
- **Security Tests:** Input validation, path traversal attempts, injection tests
- **Performance Tests:** Response times, throughput, memory usage under load
- **Linting & Type Checking:** Go: `gofmt`, `golangci-lint`; Python: `ruff`, `mypy`

---

## 6. Error Handling & Validation

### Input Validation Best Practices
AI models can be "tricked" into injection attacks. Implement strict validation:

**Path Traversal Protection:**
```go
// Go: Validate file paths
safeDir := "/data/allowed"
requestedPath := filepath.Clean(filepath.Join(safeDir, userInput))
if !strings.HasPrefix(requestedPath, safeDir) {
    return fmt.Errorf("path traversal detected")
}
```

```python
# Python: Use pathlib for safe path handling
from pathlib import Path
base_dir = Path("/data/allowed").resolve()
requested = (base_dir / user_input).resolve()
if not str(requested).startswith(str(base_dir)):
    raise ToolError("Path traversal detected")
```

**API Argument Validation:**
- Use JSON Schema (auto-generated from Go structs or Pydantic models)
- Validate enum values, string length limits, numeric ranges
- Never trust the LLM's interpretation of your schema

### Error Response Strategy
**Expected Errors (User-Facing):** Return `isError=true` with clear, actionable messages:
- ❌ "Database connection failed"
- ✅ "Cannot reach database. Please check network connectivity and try again."

**Internal Errors (Don't Leak Details):** Hide stack traces and sensitive info:
- Return generic message: "An internal error occurred. Please contact support."
- Log full error with context to stderr for debugging

**Async Error Handling (Python):**
```python
from fastmcp import ToolError

@mcp.tool
async def fetch_data(url: str) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException:
        raise ToolError(f"Request to {url} timed out after 30 seconds")
    except httpx.HTTPStatusError as e:
        raise ToolError(f"HTTP {e.response.status_code}: {e.response.text}")
```

---

## 7. Security & Validation Checklist

### Core Security Requirements
*   **Input Sanitization:** Always validate file paths, API arguments, and enum values. Use native type safety (Go structs, Pydantic) to reject malformed inputs.
*   **Consent & Authorization:** Hosts must obtain explicit user consent before invoking any tool. Implement role-based access control (RBAC) for tools that modify data.
*   **Data Protection:** Encrypt sensitive data in transit (TLS 1.3+) and at rest. Avoid logging PII or API keys.
*   **Code Signing & Supply Chain:** Build servers on pipelines with SAST (Static Application Security Testing) to prevent malicious dependencies.

### Secure-by-Design Practices
*   **Action-Oriented Descriptions:** The LLM decides to use a tool based on its description. Use active verbs: *"Use this tool to search Git history"* is better than *"Git search."*
*   **Principle of Least Privilege:** Each tool should request only the permissions it needs. Never give a tool access to all resources.
*   **Sandbox Execution:** For user-submitted or untrusted code, run in isolated processes or containers with strict resource limits.
*   **Clear Error Messages:** Never expose internal system details. Give models helpful context: *"The field 'email' is missing, please provide it"* instead of SQL error dumps.

### Pre-Deployment Security Checklist
- [ ] Run MCP Inspector to validate schemas and test all tools
- [ ] Perform security audit of input validation logic
- [ ] Review error messages for information disclosure
- [ ] Test with intentional malicious inputs (path traversal, injection)
- [ ] Verify all sensitive operations require explicit user consent
- [ ] Check for hardcoded secrets, API keys, or credentials
- [ ] Enable TLS 1.3 for HTTP/SSE transports
- [ ] Set up monitoring and alerting for suspicious tool usage patterns

---

## 8. Performance & Scalability

### Go vs. Python Performance Benchmarks
Based on 2025 performance testing across multiple languages:

| Metric | Go | Python | Node.js | Java |
| :--- | :--- | :--- | :--- | :--- |
| **I/O Operations** | 1.292ms (Best) | 2.1ms | 1.8ms | 1.5ms |
| **CPU-Bound** | 0.45ms | 4.2ms (Worst) | 0.8ms | 0.369ms (Best) |
| **Latency Consistency** | <0.02ms σ (Excellent) | 12% variance | ±0.05ms | <0.02ms σ |
| **Memory Overhead** | ~18MB | ~50MB | ~45MB | ~120MB |
| **Startup Time** | ~100ms | ~500ms | ~300ms | ~1500ms |

**Recommendation:** Use Go for latency-sensitive, high-throughput servers. Use Python for rapid prototyping and ML-heavy logic where development speed matters more than microsecond-level performance.

### Optimization Strategies

**Go Concurrency:**
- Goroutines are lightweight (~2KB each). Handle hundreds of concurrent tool calls without issues.
- Use `sync.Pool` to reuse HTTP client connections and buffer objects.
- Protect shared state (maps, counters) with `sync.RWMutex` for lock-free reads.

**Python Async I/O:**
- Use `asyncio` for all I/O-bound operations (database, API calls).
- Offload CPU-bound work to `concurrent.futures.ProcessPoolExecutor` to avoid blocking the event loop.
- Consider `uvloop` for 2-4x faster event loop performance.

**Caching & Resource Pooling:**
- Cache tool schemas, static resources, and immutable data in memory.
- Reuse HTTP client connections with connection pools.
- Implement request deduplication for identical queries within a time window.

### Scaling Patterns

**Horizontal Scaling (Kubernetes):**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-server
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: mcp-server
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
```

**Stateless Design:** MCP servers should be stateless to enable horizontal scaling. External state should live in databases or message queues.

---

## 9. Monitoring & Observability

### Three-Layer Monitoring Stack

1. **MCP Protocol Layer**
   - Tool invocation count and frequency
   - Tool execution latency (p50, p99)
   - Error rates and error types
   - Tool usage patterns (detect abuse)

2. **Application Layer**
   - Business logic performance metrics
   - Database query times
   - External API call latencies
   - Cache hit rates

3. **Infrastructure Layer**
   - Memory usage and GC pauses
   - CPU utilization
   - Network I/O
   - Goroutine/thread counts

### Recommended Observability Stack

**Logging:**
- Use structured logging (JSON format) for easy parsing
- Log all tool invocations with: user ID, tool name, arguments (sanitized), execution time, result status
- Always log errors with full context to stderr (not stdout)
- Avoid logging sensitive data (API keys, passwords, PII)

**Metrics:**
- Expose Prometheus metrics (Go) or StatsD (Python)
- Track: `mcp_tool_calls_total`, `mcp_tool_duration_seconds`, `mcp_tool_errors_total`
- Monitor system metrics: memory, CPU, goroutines

**Tracing:**
- Use OpenTelemetry for distributed tracing
- Correlate MCP calls across multiple microservices
- Identify bottlenecks and latency hotspots

### Monitoring Alerts
```
- Alert if tool error rate > 1% (production issue)
- Alert if p99 latency > 5s (performance degradation)
- Alert if memory grows unbounded (memory leak)
- Alert if unusual tool access patterns (potential abuse/attack)
```

---

## 10. Session Management & State

### Session Lifecycle
MCP supports stateful sessions, unlike REST's strict statelessness:
- **Session Creation:** Initiated by the client (Claude, IDE plugin)
- **Session Duration:** Configurable; default is to keep alive until client closes
- **State Storage:** Use external backends (Redis, database) for distributed deployments

**Session State Best Practices:**
- Minimize in-memory state; prefer database or cache for easy horizontal scaling
- Implement session timeouts; default to 1 hour of inactivity
- Store session metadata: user context, permissions, tool access logs

### Rate Limiting & Throttling
Protect against abuse and resource exhaustion:

```go
// Go: Simple token bucket rate limiter
import "golang.org/x/time/rate"

limiter := rate.NewLimiter(rate.Limit(100), 10) // 100 req/s, burst of 10

func (s *Server) CallTool(ctx context.Context, ...) error {
    if !limiter.Allow() {
        return fmt.Errorf("rate limit exceeded")
    }
    // ... call tool
}
```

```python
# Python: Per-user rate limiting
from fastmcp import RateLimitError
from collections import defaultdict
import time

call_counts = defaultdict(lambda: {"count": 0, "reset_time": time.time() + 60})

@mcp.tool
async def protected_tool(ctx: Context, user_id: str) -> str:
    bucket = call_counts[user_id]
    if time.time() > bucket["reset_time"]:
        bucket = {"count": 0, "reset_time": time.time() + 60}

    if bucket["count"] >= 100:
        raise ToolError("Rate limit exceeded. Max 100 calls/minute")

    bucket["count"] += 1
    # ... execute tool
```

---

## 11. Deployment Strategies

### Local Development
- Use stdio transport for simplicity
- Test with MCP Inspector for protocol compliance
- Use hot-reload for faster iteration (e.g., `air` in Go, `watchfiles` in Python)

### Cloud Deployment (Remote Access)
- Use HTTP/SSE transport for better compatibility with proxies and load balancers
- Deploy as containerized service (Docker)
- Use Kubernetes for orchestration and auto-scaling
- Enable TLS 1.3 for encryption in transit
- Implement health check endpoints (`/health`)

### Edge & Embedded
- Compile Go servers as small static binaries (~18MB)
- Use Python with `PyInstaller` or minimal ASGI servers for embedded environments
- Prefer stdio transport for local IPC

### Versioning & Backward Compatibility
- Version your server API (include version in tool names if breaking changes)
- Document deprecation timelines for removed/changed tools
- Support multiple API versions simultaneously during transition periods
- Use semantic versioning: MAJOR.MINOR.PATCH

---

## 12. Common Pitfalls & Solutions

| Pitfall | Problem | Solution |
| :--- | :--- | :--- |
| **Logging to stdout (Go)** | Corrupts JSON-RPC stream in stdio mode | Always use `stderr` for logging |
| **Blocking event loop (Python)** | Async tool calls hang, heartbeat fails | Use `asyncio` for I/O; `ProcessPoolExecutor` for CPU-bound |
| **Unvalidated input** | Path traversal, injection attacks | Use type-safe parsing; validate enums, paths, ranges |
| **Leaking errors** | Stack traces expose internal structure | Return generic user-facing errors; log details to stderr |
| **Stateful servers** | Can't horizontal scale | Use external backends (Redis, DB) for shared state |
| **Missing health checks** | Load balancers can't detect failures | Implement `/health` endpoint; expose readiness probe |
| **No rate limiting** | Resource exhaustion from abuse | Implement token bucket or sliding window rate limiting |
| **Ignoring tool descriptions** | LLM makes poor tool choices | Write active-verb descriptions that guide LLM reasoning |

---

## 13. Tool Design Patterns

### Tool Decomposition Strategy
Break down complex operations into focused, single-purpose tools. LLMs reason better with many small tools than a few large ones.

**Anti-pattern (Bad):**
```python
@mcp.tool
def manage_database(action: str, query: str, table: str) -> dict:
    """Generic database management - AVOID THIS"""
    if action == "select": ...
    elif action == "insert": ...
    elif action == "update": ...
```

**Pattern (Good):**
```python
@mcp.tool
def query_database(table: str, where: str = "") -> list:
    """Search rows in a table using SQL WHERE clause"""

@mcp.tool
def insert_record(table: str, record: dict) -> dict:
    """Insert a new row and return the created record with ID"""

@mcp.tool
def update_record(table: str, id: str, updates: dict) -> dict:
    """Update specific fields of an existing record"""
```

### Tool Batching
For high-frequency operations, offer batch variants alongside single-operation tools:

```python
@mcp.tool
def create_user(name: str, email: str) -> dict:
    """Create a single user"""

@mcp.tool
def create_users_batch(users: list[dict]) -> list[dict]:
    """Create multiple users efficiently in one call"""
```

### Progressive Disclosure
Start with essential tools; hide advanced/rare operations behind meta-tools that describe them:

```python
@mcp.tool
def search_tools(query: str) -> list[str]:
    """Search tool descriptions by keyword. Use this to discover advanced tools."""

@mcp.tool
def list_advanced_tools() -> list[dict]:
    """List rarely-used tools for power users"""
```

### Tool Composition
Design tools that work well together. Outputs from one should often feed into others:

```python
# Good composition chain:
# 1. list_users() -> returns user IDs
# 2. get_user_details(user_id) -> returns profile info
# 3. update_user(user_id, changes) -> updates the profile
```

---

## 14. Authentication & Authorization

### API Key Management
Never embed API keys in tool names or descriptions. Pass credentials securely:

**In-Process (Local):**
- Load from environment variables (`.env` file, not in code)
- Use credential files with restricted permissions (mode 0600)
- Rotate keys regularly

**Remote Servers:**
- Load from secret management systems (HashiCorp Vault, AWS Secrets Manager, etc.)
- Implement service-to-service authentication (mTLS, JWT)
- Audit all credential access

### User Context & RBAC
Implement role-based access control for multi-tenant servers:

```go
// Go example: Enforce permissions
type Context struct {
    UserID   string
    Role     string // "admin", "user", "viewer"
    Permissions []string
}

func (s *Server) CallTool(ctx context.Context, name string, args interface{}) error {
    userCtx := ctx.Value("user").(Context)

    // Check if user has permission for this tool
    requiredPerm := fmt.Sprintf("tool:%s", name)
    if !contains(userCtx.Permissions, requiredPerm) {
        return fmt.Errorf("insufficient permissions for tool: %s", name)
    }

    // ... proceed with tool execution
}
```

```python
# Python example: Enforce permissions with context
from fastmcp import Context

@mcp.tool
async def delete_resource(ctx: Context, resource_id: str) -> dict:
    """Delete a resource. Requires 'admin' role."""
    user = ctx.meta.get("user", {})
    if user.get("role") != "admin":
        raise ToolError("Only admins can delete resources")

    # ... perform deletion
    return {"deleted": True, "id": resource_id}
```

### Tool-Level Permissions
Document required permissions in tool descriptions and enforce at invocation time:

```python
# FastMCP with permission decorator
@mcp.tool
def sensitive_operation():
    """Requires: 'sensitive:write' permission"""
    # Implementation
```

### Audit Logging
Log all tool invocations with user context for compliance and security investigations:

```python
import logging
import json
from datetime import datetime

audit_log = logging.getLogger("audit")

@mcp.tool
async def sensitive_tool(ctx: Context, action: str) -> dict:
    user_id = ctx.meta.get("user_id", "unknown")

    try:
        result = await perform_action(action)

        # Log success
        audit_log.info(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "action": "tool_invoked",
            "tool": "sensitive_tool",
            "arguments": sanitize(action),
            "result": "success"
        }))

        return result
    except Exception as e:
        # Log failure
        audit_log.warning(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "action": "tool_invoked",
            "tool": "sensitive_tool",
            "result": "error",
            "error": str(e)
        }))
        raise ToolError(f"Operation failed: {str(e)}")
```

---

## 15. High-Quality Sources & Resources

### Official Documentation & Specifications
*   **[Official MCP Website](https://modelcontextprotocol.io):** The primary source for the protocol specification and architecture.
*   **[MCP Specification (2025)](https://modelcontextprotocol.io/specification/2025-11-25):** Detailed JSON-RPC 2.0 schema and capability definitions.
*   **[MCP Best Practices Guide](https://modelcontextprotocol.info/docs/best-practices/):** Comprehensive guide covering architecture, security, operations, and data management.
*   **[Build MCP Server Documentation](https://modelcontextprotocol.io/docs/develop/build-server):** Step-by-step tutorials for getting started.

### SDKs & Frameworks
*   **[Official Go SDK](https://github.com/modelcontextprotocol/go-sdk):** Maintained in collaboration with Google; provides typed server scaffolding and automatic JSON schema generation.
*   **[FastMCP (Python)](https://github.com/jlowin/fastmcp):** The high-level, Pythonic framework for rapid prototyping (recommended for most use cases).
*   **[Official Python SDK](https://github.com/modelcontextprotocol/python-sdk):** Low-level Python implementation from Anthropic for advanced use cases.
*   **[mcp-go (mark3labs)](https://github.com/mark3labs/mcp-go):** Popular community Go SDK with less boilerplate; supports stdio, HTTP, SSE, and in-process transports.

### Testing & Quality Assurance
*   **[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector):** Official interactive testing and debugging tool for MCP servers.
*   **[How to Test MCP Servers](https://www.stainless.com/mcp/how-test-mcp-servers):** Best practices for functional, security, and performance testing.
*   **[MCP Server Testing Tools 2025](https://testomat.io/blog/mcp-server-testing-tools-you-need):** Overview of testing frameworks and tools.

### Deployment & Operations
*   **[MCP Server Monitoring & Observability](https://www.speakeasy.com/mcp/monitoring-mcp-servers):** Guide to three-layer monitoring (protocol, application, infrastructure).
*   **[Kubernetes MCP Server Deployment](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-server-integration.html):** AWS patterns for containerized MCP servers.
*   **[MCP Best Practices: Operations](https://modelcontextprotocol.info/docs/best-practices/):** Session policies, caching strategies, monitoring, and logging.

### Performance & Benchmarking
*   **[MCP Server Performance Benchmark 2025](https://www.tmdevlab.com/mcp-server-performance-benchmark.html):** Comprehensive comparison of Go, Python, Node.js, and Java implementations.
*   **[Go MCP Implementation Guide](https://mcpcat.io/guides/building-mcp-server-go/):** Go-specific patterns and concurrency best practices.
*   **[Python FastMCP Tutorial](https://www.firecrawl.dev/blog/fastmcp-tutorial-building-mcp-servers-python):** Practical examples of error handling and async patterns.

### Security & Compliance
*   **[MCP Security Risks & Controls](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls):** Red Hat analysis of security implications and mitigation strategies.
*   **[MCP Best Practices: Security](https://modelcontextprotocol.info/docs/best-practices/):** Input validation, consent flows, access control, and data protection.

### Production Examples & Reference Implementations
*   **[Official MCP Servers Collection](https://github.com/modelcontextprotocol/servers):** Anthropic-maintained reference implementations for Git, Postgres, Google Drive, Slack, and more.
*   **[Awesome MCP Servers](https://github.com/appcypher/awesome-mcp-servers):** Community-curated list of high-quality, production-ready servers.
*   **[Top MCP Servers 2025](https://www.pomerium.com/blog/best-model-context-protocol-mcp-servers-in-2025):** Industry analysis of popular and innovative MCP servers.
