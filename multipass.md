`NOTE:` - most of these assume Win10 Pro and Hyper/V

# References
- [Documentation](https://multipass.run/docs)


# The basics

Listing VM's

```
PS C:\Users\matth> multipass list
Name                    State             IPv4             Image
helpful-dog             Running           172.26.164.110   Ubuntu 22.04 LTS
                                          100.122.105.91
```

Stopping and Changing Memory

```
PS C:\Users\matth> multipass stop helpful-dog
>>
PS C:\Users\matth> multipass set local.helpful-dog.memory=8G
PS C:\Users\matth> multipass get local.helpful-dog.memory
8.0GiB
PS C:\Users\matth> multipass get local.helpful-dog.disk
5.0GiB
PS C:\Users\matth> multipass get local.helpful-dog.cpus
1
PS C:\Users\matth> multipass start helpful-dog
PS C:\Users\matth> multipass exec helpful-dog free
               total        used        free      shared  buff/cache   available
Mem:         8140380      243712     7604520         916      292148     7658384
Swap:              0           0           0
```
