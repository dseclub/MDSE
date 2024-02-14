
## Grafana

Amazon Managed Grafana is a fully managed and secure data visualization service that you can use to instantly query, correlate, and visualize operational metrics, logs, and traces from multiple sources. Amazon Managed Grafana makes it easy to deploy, operate, and scale Grafana, a widely deployed data visualization tool that is popular for its extensible data support.

With Amazon Managed Grafana, you create logically isolated Grafana servers called workspaces. Then, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces without having to build, package, or deploy any hardware to run your Grafana servers.

Amazon Managed Grafana manages the provisioning, setup, scaling, and maintenance of your logical Grafana servers so that you don't have to do these tasks yourself. Amazon Managed Grafana also provides built-in security features for compliance with corporate governance requirements, including single sign-on, data access control, and audit reporting.

Amazon Managed Grafana is integrated with AWS data sources that collect operational data, such as Amazon CloudWatch, Amazon OpenSearch Service, AWS X-Ray, AWS IoT SiteWise, Amazon Timestream, and Amazon Managed Service for Prometheus. Amazon Managed Grafana includes a permission provisioning feature for adding supported AWS services as data sources. Amazon Managed Grafana also supports many popular open-source, third-party, and other cloud data sources.

For user authentication and authorization, Amazon Managed Grafana can integrate with identity providers (IdPs) that support SAML 2.0 and also can integrate with AWS Single Sign-On.

Amazon Managed Grafana is priced per active user in a workspace.

https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html

Amazon Managed Grafana announces new data source plugins for Amazon Athena and Amazon Redshift, enabling customers to query, visualize, and alert on their Athena and Redshift data from Amazon Managed Grafana workspaces. Amazon Managed Grafana now also supports CloudFlare, Zabbix, and Splunk Infrastructure Monitoring data sources as well as the Geomap panel visualization and open source Grafana version 8.2.

With the new Amazon Athena data source, customers can now connect to, query, and analyze their Amazon Simple Storage Service (Amazon S3) data using standard SQL directly from Amazon Managed Grafana workspaces. Customers can also leverage the default dashboard that comes with the Amazon Athena plugin to query their AWS Cost and Usage Reports and visualize their AWS spend. Using the new Amazon Redshift data source, customers can now create dashboards and alerts in their Amazon Managed Grafana workspaces to analyze their structured and semi-structured data across data warehouses, operational databases, and data lakes. The Amazon Redshift plugin also comes with a default dashboard out-of-the-box that makes it easy for customers to get started with monitoring the health and performance of their Redshift clusters.

Customers can now also use the Geomap panel visualization to visualize their geospatial data in a map view. Customers can configure multiple overlay styles to visually represent important location-based characteristics of their data, such as the heatmap overlay to cluster data points for visualizing hotspot locations with high data densities. The Zabbix and CloudFlare data sources are now available on Amazon Managed Grafana, enabling customers to visualize Zabbix metrics and connect to their CloudFlare account to monitor their DNS traffic by geography, latency, response code, query type, and hostname. With the Splunk Infrastructure Monitoring data source, available with a Grafana Enterprise License, customers can now also visualize Splunk Infrastructure Monitoring data directly from their Managed Grafana workspaces. Existing and new Amazon Managed Grafana workspaces are now automatically upgraded to Grafana version 8.2, with no action required from customers.

Amazon Managed Grafana is a fully managed service that takes care of the provisioning, setup, scaling, and maintenance of Grafana servers

https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-grafana-athena-redshift-data-sources-geomap/

https://aws.amazon.com/blogs/mt/amazon-athena-amazon-redshift-plugins-and-new-features-in-amazon-managed-grafana/ 



```
```
