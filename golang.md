# Installation
- Get tgz from  https://golang.org/dl/ and go to https://golang.org/doc/install

## Using Documentation

See https://golang.org/doc/

### Install local godoc server

```
go get -v  golang.org/x/tools/cmd/godoc
```

and run from a non-code directory (or else, LOL)

```
godoc -http=:9999
using GOPATH mode
```

You should see all your installed packages under *Third Party*
