# Installation 

See [Ubuntu](https://software.opensuse.org/download.html?project=security%3Azeek&package=zeek-lts)

# Plugins of Interest

## JA4

See https://github.com/FoxIO-LLC/ja4/tree/main/zeek but basically

```
# /opt/zeek/bin/zkg install zeek/foxio/ja4s
```

add `@load ja4` to `/opt/zeek/share/zeek/site/local.zeek`

and then `[ZeekControl] > deploy`
