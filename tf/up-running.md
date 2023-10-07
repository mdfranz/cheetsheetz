Notes from [https://www.terraformupandrunning.com/](Terraform: Up and Running, 3rd Edition)

# 1 - Why Terraform

*Provisioning* compared with other tools:
- Config Management & Server Templating
- Orchestration 

DSL vs. General Purpose 

# 2 - Getting Started 

## Provisioner


## Resource 

```
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIG ...]
}
```

Reference Syntax

```
<PROVIDER>_<TYPE>.<NAME>.<ATTRIBUTE>
```

## Variables

```
var.<VARIABLE_NAME>
```

Variables take the following parameters and are references by 


- description
- default
- type
- validation 
- sensitive

```
variable "NAME" {
  [CONFIG ...]
}

### Output Variables

```
output "<NAME>" {
  value = <VALUE>
  [CONFIG ...]
}
```


```
## CLI States
- init
- plan
- apply
- destroy
