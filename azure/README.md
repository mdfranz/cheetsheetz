# CLI
- [azure-cli](https://pypi.org/project/azure-cli/) on PyPi
- [Azure CLI Documentation](https://learn.microsoft.com/en-us/cli/azure/) 

# Azure Functions
## Python
- [Azure Functions Python Developer Guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=application-level)

## Go 
- [Deploying an Azure Function in Go](https://www.hildeberto.com/2021/01/azure-function-golang-2.html)

## Deployment 
- [Provisioning Azure Functions Using Terraform](https://www.hildeberto.com/2021/03/terraform-azure-function.html)

# Azure Messaging Services
[AMQP 1.0 in Azure Service Bus and Event Hubs protocol guide](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-amqp-protocol-guide)

See https://github.com/rlevchenko/terraform-azure-data has multiple data and messaging services

## Service Bus
- [Azure Service Bus Documentation](https://docs.microsoft.com/en-us/azure/service-bus-messaging/)

### Infra Code
- https://github.com/jungopro/terraform-azurerm-servicebus
- https://github.com/najgel/terraform-azurerm-servicebus-queue-authorization-rule

## Event Hubs
- [Azure Event Hubs — A big data streaming platform and event ingestion service](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about) 
- [Azure Event Hubs Documentation](https://docs.microsoft.com/en-us/azure/event-hubs/)
- [Automatically deploy and configure EventHubs, Stream Analytics, and CosmosDB using Terraform](https://tsuyoshiushio.medium.com/automatically-deploy-and-configure-eventhubs-stream-analytics-and-cosmosdb-using-terraform-16aa5a34240e_) (March, 2018)
- [Send events to or receive events from event hubs by using Python (azure-eventhub)](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send) using [azure-eventhub](https://pypi.org/project/azure-eventhub/)
- https://github.com/claranet/terraform-azurerm-eventhub

## Event Grid

### Infra Code
- [Using Terraform to Deploy Event Grid Subscriptions for Function Apps](https://jfarrell.net/2019/12/13/using-terraform-to-deploy-event-grid-subscriptions-for-function-apps/)
- https://github.com/markti/tf_azure_eventgrid
- https://github.com/grayjeremy/terraform-azurerm-eventgrid-blob 
