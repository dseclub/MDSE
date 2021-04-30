# AWS Glue

AWS Glue is serverless - a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries.
 
 **Glue Data Catalog** is a central repository to store structural and operational metadata for all your data assets. For a given data set, you can store its table definition, physical location, add business relevant attributes, as well as track how this data has changed over time. AWS Glue provides a number of ways to populate metadata into the AWS Glue Data Catalog. AWS Glue Data Catalog is Apache Hive Metastore compatible. 
 
**Glue Crawler**  You can use a crawler to populate the AWS Glue Data Catalog with tables. It automatically discover new data, extracts schema definitions. It detects schema changes and version tables. It can also detect Hive style partitions on Amazon S3.
 
**Glue Connection** Connections are used by crawlers and jobs in AWS Glue to access certain types of data stores. A connection contains the properties that are needed to access your data store.

**Glue Classifier** A classifier reads the data in a data store. If it recognizes the format of the data, it generates a schema. The classifier also returns a certainty number to indicate how certain the format recognition was. AWS Glue provides a set of built-in classifiers, but you can also create custom classifiers.



**Glue streaming** extract, transform, and load (ETL) jobs that run continuously, consume data from streaming sources like Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka (Amazon MSK). 

Glue Streaming is built based on Spark streaming which is micro-batch oriented and inherits all features of Spark Streaming. 


**AWS Glue DataBrew** is a visual data preparation tool that makes it easy for data analysts and data scientists to prepare data with an interactive, point-and-click visual interface without writing code. With Glue DataBrew, you can easily visualize, clean, and normalize terabytes, and even petabytes of data directly from your data lake, data warehouses, and databases, including Amazon S3, Amazon Redshift, Amazon Aurora, and Amazon RDS.

AWS Glue DataBrew is built for users who need to clean and normalize data for analytics and machine learning. Data analysts and data scientists are the primary users.
 For data analysts, examples of job functions are business intelligence analysts, operations analysts, market intelligence analysts, legal analysts, financial analysts, economists, quants, or accountants. For data scientists, examples of job functions are materials scientists, bioanalytical scientists, and scientific researchers.


**AWS Glue Studio** is a visual interface for AWS Glue that makes it easy for extract-transform-and-load (ETL) developers to author, run, and monitor AWS Glue ETL jobs. 

**AWS Glue Elastic Views** makes it easy to build materialized views that combine and replicate data across multiple data stores without you having to write custom code.

With AWS Glue Elastic Views, you can use familiar Structured Query Language (SQL) to quickly create a virtual table—a materialized view—from multiple different source data stores. AWS Glue Elastic Views copies data from each source data store and creates a replica in a target data store. AWS Glue Elastic Views continuously monitors for changes to data in your source data stores and provides updates to the materialized views in your target data stores automatically, ensuring data accessed through the materialized view is always up-to-date.





## Resources

https://docs.aws.amazon.com/glue/latest/dg/getting-started.html

https://github.com/awsdocs/aws-glue-developer-guide/tree/master/doc_source

https://aws.amazon.com/about-aws/whats-new/2020/10/aws-glue-streaming-etl-jobs-support-schema-detection-and-evolution/

https://docs.aws.amazon.com/glue/latest/dg/add-job-streaming.html

https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/

https://aws.amazon.com/blogs/big-data/building-an-aws-glue-etl-pipeline-locally-without-an-aws-account/

https://partiql.org/
