# Snowflake


Snowflake is a cloud data platform that’s provided as a fully-managed service, it is integrated platform delivered as-a-service. Multi-cluster, shared data, centralized, scale-out storage.

Snowflake platform includes storage, compute, and cloud services layers that are physically separated but logically integrated.

 Snowflake’s architecture has three layers that scale independently of one another: the database storage layer, the cloud services layer, and the query processing layer.

 Database storage: Snowflake has a scalable cloud blob storage for storing structured and semi-structured data, including JSON, AVRO, and Parquet. The storage layer contains tables, schemas, databases, and diverse data. Tables can store multiple petabytes of data. Data in Snowflake tables is automatically divided into micro-partitions, which are contiguous units of storage. Each micro-partition contains between 50 MB and 500 MB of uncompressed data.

 Cloud services layer: The cloud services layer provides services such as authentication, infrastructure management, and access control. It also provides metadata management.

 Query processing layer: The query processing layer handles query execution. Snowflake processes queries using “virtual warehouses.” Each virtual warehouse is an MPP compute cluster made up of multiple compute nodes and each virtual warehouse is an independent compute cluster. As a result, each virtual warehouse operates independently and has no impact on the performance of the other virtual warehouses.


https://www.snowflake.com/

https://www.snowflake.com/education-and-training/

https://www.guru99.com/star-snowflake-data-warehousing.html

https://docs.snowflake.com/en/user-guide/warehouses.html
