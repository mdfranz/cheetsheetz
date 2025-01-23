# Overall Docs
- [Docs](https://learn.microsoft.com/en-us/azure/sentinel/) including [quick start onboarding](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard), [deployment guide](https://learn.microsoft.com/en-us/azure/sentinel/deploy-overview) and [data connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources?tabs=azure-portal) and [migration guide](https://learn.microsoft.com/en-us/azure/sentinel/migration)
- [MSSP Usage](https://learn.microsoft.com/en-us/azure/sentinel/multiple-tenants-service-providers)
- [APIs](https://learn.microsoft.com/en-us/rest/api/securityinsights/api-versions)

# Azure Arc/AMA
## Agent Installation
- [Linux Installation](https://learn.microsoft.com/en-us/azure/azure-arc/servers/manage-agent?tabs=linux-apt)
- [How-To Install and Setup: Azure Arc, (AMA) Azure Monitor Agent and (DCR) Data Collection Rules for sending Linux Syslog to Sentinel for Threat Hunting and Security Monitoring with AuditD](https://medium.com/@truvis.thornton/how-to-install-and-setup-azure-arc-ama-azure-monitor-agent-and-dcr-data-collection-rules-for-47381ee9d312)

# End to End
## Data Sources & Azure Log Analytics Tables
Sentinel uses [data collection rules](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-overview) that support [transformations](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-transformations) that process data from [collection endpoints](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-endpoint-overview?tabs=portal)

- [JSON Data Collection](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/data-collection-log-json)
- [Custom data ingestion and transformation in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/data-transformation)

### Blogs
- [Demystifying Data Collection Rules and Transformations](https://hybridbrothers.com/demystifying-data-collection-rules-and-transformations/) - May '23
- [How to create a Custom Table in Log Analytics Workspace (Azure)!](https://it-infrastructure.solutions/how-to-create-a-custom-log-analytics-workspace-table/)
- [How to manage Log Analytics tables using the Azure CLI](https://www.jorgebernhardt.com/log-analytics-workspace-tables-azure-cli/)
- [How to Create and Monitor Custom Logs with Azure Monitor](https://phiptech.com/how-to-create-and-monitor-custom-logs-with-azure-monitor/)
- [Ingest DCR-based custom logs in Microsoft Sentinel with Logstash](https://koosg.medium.com/ingest-dcr-based-custom-logs-in-microsoft-sentinel-with-logstash-f94c79e69b93) - Nov '22

### Automation
- [Terraform: Support for creating a new table in Log Analytics workspace #23359](https://github.com/hashicorp/terraform-provider-azurerm/issues/23359)
- [bicep dcr](https://github.com/petitess/bicep/blob/main/datacollectionrule01/modules/dcr.bicep)
- [Azure Monitor, Security Center, Sentinel Infrastructure as Code with Bicep](https://www.cloudsma.com/2021/04/iac-bicep-azure-monitor-security/) with [code](https://github.com/scautomation/Bicep-AzureMonitor-Sentinel)

## Logging

# KQL
- [Kusto Docs](https://learn.microsoft.com/en-us/kusto/?view=microsoft-fabric)
