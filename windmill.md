
# CLI

(Installation)[https://www.windmill.dev/docs/advanced/cli/installation] is done with and then updating `PATH` to include `$HOME/.deno/bin`

```
deno install -q -A https://deno.land/x/wmill/main.ts
```


# Local Development Tips

See (recommended setup)[https://www.windmill.dev/docs/advanced/local_development#local-development-recommended-setup] which suggests using the following when using within CI/CD

```
wmill sync pull --skip-variables --skip-secrets --skip-resources
```
