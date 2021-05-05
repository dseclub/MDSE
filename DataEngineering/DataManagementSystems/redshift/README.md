# Amazon Redshift

Amazon Redshift is a fully managed, fast, petabyte-scale data warehouse service that is cost-effective and provides a simple way to efficiently analyze your data using your existing business intelligence tools. 

Amazon Redshift costs less than a tenth of most traditional data warehousing solutions and is optimised for datasets ranging from a few hundred gigabytes to petabytes.


**Redshift Cluster:** Redshift uses a cluster of nodes as its core infrastructure component. A cluster usually has one leader node and several compute nodes. In cases where there is only one compute node, there is no additional leader node.

 **Compute Nodes:** Each compute node has its own CPU, memory and storage disk. Client applications are oblivious to the existence of compute nodes and never have to deal directly with compute nodes. 
 
**Leader Node:** The leader node is responsible for all communications with client applications. The leader node also manages the coordination of compute nodes. Query parsing and execution plan development is also the responsibility of the leader node. On receiving a query, the leader node creates the execution plan and assigns the compiled code to compute nodes. A portion of the data is assigned to each compute node. The final aggregation of the results is performed by the leader node.

 ## Features:
### Massively Parallel
Amazon Redshift delivers fast query performance on datasets ranging in size from gigabytes to exabytes. Redshift uses columnar storage, data compression, and zone maps to reduce the amount of I/O needed to perform queries. It uses massively parallel processing (MPP) data warehouse architecture to parallelize and distribute SQL operations to take advantage of all available resources. The underlying hardware is designed for high-performance data processing, using locally attached storage to maximize throughput between the CPUs and drives, and a high bandwidth mesh network to maximize throughput between nodes.

### Machine Learning
Amazon Redshift uses machine learning to deliver high throughout, irrespective of workloads or concurrent usage. It utilizes sophisticated algorithms to predict incoming query run times and assigns them to the optimal queue for the fastest processing. For instance, queries such as dashboards and reports with high concurrency requirements are routed to an express queue for immediate processing.

### Fault-Tolerant
Amazon Redshift has multiple features that enhance the reliability of your data warehouse cluster. Redshift continuously monitors the health of the cluster, and automatically re-replicates data from failed drives and replaces nodes as necessary for fault tolerance.

###Flexible Querying
Amazon Redshift gives you the flexibility to execute queries within the console or connect SQL client tools, libraries, or Business Intelligence tools you use. Query Editor on the AWS console provides a powerful interface for executing SQL queries on Redshift clusters and viewing the query results and query execution plan (for queries executed on compute nodes) adjacent to your queries.




## Resources


https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html


https://docs.aws.amazon.com/redshift/latest/dg/

https://github.com/aws-quickstart/quickstart-amazon-redshift

https://github.com/awslabs/amazon-redshift-utils

https://github.com/awslabs/amazon-redshift-monitoring


https://aws.amazon.com/blogs/aws/new-aqua-advanced-query-accelerator-for-amazon-redshift/


## Books

Amazon Redshift Cookbook
