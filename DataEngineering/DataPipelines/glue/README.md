# AWS Glue

AWS Glue is serverless - a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries.
 
Glue Crawler  You can use a crawler to populate the AWS Glue Data Catalog with tables. It automatically discover new data, extracts schema definitions. It detects schema changes and version tables. It can also detect Hive style partitions on Amazon S3.
 
Glue Connection Connections are used by crawlers and jobs in AWS Glue to access certain types of data stores. A connection contains the properties that are needed to access your data store.

Glue Classifier A classifier reads the data in a data store. If it recognizes the format of the data, it generates a schema. The classifier also returns a certainty number to indicate how certain the format recognition was. AWS Glue provides a set of built-in classifiers, but you can also create custom classifiers.

## Resources

https://docs.aws.amazon.com/glue/latest/dg/getting-started.html

https://github.com/awsdocs/aws-glue-developer-guide/tree/master/doc_source

https://aws.amazon.com/about-aws/whats-new/2020/10/aws-glue-streaming-etl-jobs-support-schema-detection-and-evolution/

https://docs.aws.amazon.com/glue/latest/dg/add-job-streaming.html
