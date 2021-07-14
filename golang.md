# Installation
- Get tgz from  https://golang.org/dl/ and go to https://golang.org/doc/install

## Using Documentation
- https://golang.org/doc/
- https://pkg.go.dev/

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


# Concurrency

## Context() 
- https://gobyexample.com/context
- https://medium.com/rungo/understanding-the-context-package-b2e407a9cdae 
- https://levelup.gitconnected.com/how-to-use-context-to-manage-your-goroutines-like-a-boss-ef1e478919e6
- 