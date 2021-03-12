# AWS storage

Amazon Simple Storage Service S3

Amazon Glacier

EC2 instance storage

Amazon Elastic File System EFS

the Amazon Elastic Block Store EBS

AWS Storage Gateway

AWS Snowball


## S3

Even though each bucket is created in specific region, S3 names must be **unique** globally

## S3's Object is consists of the following:
- Key
- Value
- Version ID
- Metadata
- Subresources (Access Control Lists, Torrent)

## Data consistency work for S3:
- Read after Write consistency for PUTS of new Objects
- Eventual Consistency for overwrite PUTS and DELETES

## Features:
- Tiered Storage Available
- Lifecycle Management
- Versioning
- Encryption
- MFA Delete
- **Access Control Lists** and **Bucket Policies**
- can create up to **100 buckets** per count by default
- object's size is from **0 bytes** up to **5TB**
- upload object > 100MB => **should** use multipart upload
- upload object > 5GB => **must** use multipart upload

## Amazon Glacier

Amazon Glacier classes offer an extremely low-cost long term durable storage solution which is often referred to as cold storage, ideally suited for long term backup and archival requirements. 

S3 Glacier storage classes directly interact with the Amazon S3 lifecycle rules.

The data structure within Glacier is centered around vaults and Archives. 

Move your data into the Glacier vault using the available API or SDKs or S3 lifecycle rules .

Retrieving your data from archives with the APIs, SDKs or the AWS CLI. 
