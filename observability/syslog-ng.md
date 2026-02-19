# MacOS
- [Collecting even more logs on MacOS using syslog-ng](https://www.syslog-ng.com/community/b/blog/posts/collecting-even-more-logs-on-macos-using-syslog-ng)

```
@version: 4.10
@include "scl.conf"

source s_local {
    darwin-oslog-stream(params("--type log --level debug"));
    internal();
};

source s_network {
    default-network-drivers();
};

destination d_openobserve_http {
    openobserve-log(
        url("http://127.0.0.1")
        organization("default")
        stream("syslog-ng")
        user("blah@blah.com")
        password("xxxxxx")
    );
};
log {
    source(s_local);
    destination(d_openobserve_http);
    flags(flow-control);
};
```
