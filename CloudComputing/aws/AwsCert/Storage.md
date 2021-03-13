# AWS Storage services

## Amazon Simple Storage Service (S3)
Object storage built to store and retrieve any amount of data from anywhere

## Amazon Glacier

## EC2 instance storage

## Amazon Elastic File System
Scalable, elastic, cloud-native NFS file system

## Amazon FSx for Windows File Server
Fully managed file storage built on Windows Server

## Amazon FSx for Lustre
Fully managed high-performance file system integrated with Amazon S3

## Amazon Elastic Block Store
Easy to use, high performance block storage at any scale

## AWS Backup
Centrally manage and automate backups across AWS services

## Data transfer
## AWS Storage Gateway
Hybrid cloud storage that provides on-premises access to virtually unlimited cloud storage

## AWS DataSync
Easily transfer data to and from AWS up to 10x faster

## AWS Transfer Family
Simple and seamless file transfer to Amazon S3 using SFTP, FTPS, and FTP

## AWS Snow Family
Physical devices to migrate data into and out of AWS


## S3

Amazon S3 is a fully managed object-based storage service that is highly available, highly durable, very cost-effective and widely accessible. 

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

Amazon Glacier classes offer a low-cost long term durable storage solution which is often referred to as cold storage, ideally suited for long term backup and archival requirements. 

S3 Glacier storage classes directly interact with the Amazon S3 lifecycle rules.

The data structure within Glacier is centered around vaults and Archives. 

Move your data into the Glacier vault using the available API or SDKs or S3 lifecycle rules .

Retrieving your data from archives with the APIs, SDKs or the AWS CLI. 
