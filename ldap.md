# Background

From http://www.zytrax.com/books/ldap/ch2/

## Overview

Defines how the data is defined and consists of 4 models

- *information model* - aka data model 
- *naming model* - defines ou, DN, etc. 
- *functional model* - read, write, search modify 
- *security model* - who can do what to which data 

## Synchronization & Replication

Uses simple asynchronous process that doesn't have things like transactions, locking, rollback



## Data Model

### Object Trees

Heirarchy of objects called entries called a DIT (Directory Information Tree) where the top of the tree is the ROOT

Entry -> on or more ObjectClasses

#### objectClass

#### Attributes

Common ones

- cn
- dc
- ou
- uid


#### Schema

- core.schema
- 



## Random Facts

LDAP is generally not case sensitive except for password 


# LDAP Servers

## OpenDJ

See https://github.com/OpenIdentityPlatform/OpenDJ/wiki/Administration

To run in Docker

```
docker run -p 1389:1389 -p 1636:1636 -p 4444:4444 --name opendj openidentityplatform/opendj
```
