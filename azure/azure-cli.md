# Installation

See [official docs](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

# Resource Groups

Remember resource groups are assigned to a region (Location)

```
$ az group list --output table                                                                                      
Name                        Location    Status
--------------------------  ----------  ---------
DefaultResourceGroup-EUS    eastus      Succeeded
NetworkWatcherRG            eastus      Succeeded
cloud-shell-storage-eastus  eastus      Succeeded
mattfirstoneunique          centralus   Succeeded
PackerResourceGroup         eastus      Succeeded
terraform-servicebus        centralus   Succeeded
testResourceGroup           westus      Succeeded
```



Not to be confused with resources

```
$ az resource list --output table
Name                                    ResourceGroup               Location    Type                                                Status
--------------------------------------  --------------------------  ----------  --------------------------------------------------  --------
cs210037ffea9b24f87                     cloud-shell-storage-eastus  eastus      Microsoft.Storage/storageAccounts
Failure Anomalies - mattfirstoneunique  mattfirstoneunique          global      microsoft.alertsManagement/smartDetectorAlertRules
Migration_AG1                           mattfirstoneunique          global      microsoft.insights/actiongroups
Migration_AG2                           mattfirstoneunique          global      microsoft.insights/actiongroups
NetworkWatcher_centralus                NetworkWatcherRG            centralus   Microsoft.Network/networkWatchers
NetworkWatcher_eastus                   NetworkWatcherRG            eastus      Microsoft.Network/networkWatchers
mdfranz-servicebus-namespace            terraform-servicebus        centralus   Microsoft.ServiceBus/namespaces
```

Using `jq`

```
$ az resource list | jq '.[]|{name,location}'
{
  "name": "cs210037ffea9b24f87",
    "location": "eastus"
}
```

# Resource Graph CLI Usage

See https://learn.microsoft.com/en-us/azure/governance/resource-graph/first-query-azurecli


