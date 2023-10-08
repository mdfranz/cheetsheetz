Notes from [https://www.terraformupandrunning.com/](Terraform: Up and Running, 3rd Edition) and https://github.com/brikis98/terraform-up-and-running-code

# 1 - Why Terraform

*Provisioning* compared with other tools:
- Config Management & Server Templating
- Orchestration 

DSL vs. General Purpose 

# 2 - Getting Started 

## Provider

## Resource 

```
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIG ...]
}
```

Lifecycle as in `prevent_destroy`

```
<PROVIDER>_<TYPE>.<NAME>.<ATTRIBUTE>
```

Reference Syntax


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
```

### Output Variables

```
output "<NAME>" {
  value = <VALUE>
  [CONFIG ...]
}
```

## Data

```
data.<PROVIDER>_<TYPE>.<NAME>.<ATTRIBUTE>
```

## CLI States
- init
- plan
- apply
- destroy

# 3 - How to Manage Terraform State

Backends

State File Isolation Approaches
- workspaces
- file layout 
