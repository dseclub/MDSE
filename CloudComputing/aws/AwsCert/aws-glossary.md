## Glossary

**Fault isolation** Means of containing a fault in a system to a limited area.

**Network latency** The time it takes network traffic to traverse back and forth over the network.

**Data locality** The practice of keeping data in a certain region or country because of legal restrictions.

**CLI** Command Line Interface.

**SDK** Software Development Kit.

**Network fabic** A high speed network interconnect, where high volumes of traffic move over short distances.

**Multicast networking** A networking protocol where traffic is sent in a "one-to-many" manner.

**Active/Active** A system that is running actively in multiple instances, typically in a distributed manner where complete functionality is available in more than one area.

**Snapshot** A complete copy of a dataset at a specific point in time.

**Server-based Services** Services that are existing applications that AWS provides as "managed services" and run on individual server instances.

**DynamoDB** AWS developed non-relational database

**DynamoDB Global Tables** Multi-Region DynamoDB Tables.

**S3** AWS developed object store that can store an unlimited amount of data.

**Compute Services** AWS services that provide generic compute capacity.

**Force Majeure** Term describing an event or circumstance that is completely unavoidable.

**IP whitelisting** Allowing specific IP addresses only to access some resource.

**Pilot light** Old appliances such as furnaces or water heaters had a small flame that was always burning that was used to ignite a larger flame when needed.

**Regulated industries** Industries where the government sets strict rules and guidelines for data storage or operational practices.

**Uptime** The time where you application is available and correctly functioning.

**Downtime** The time where your application is not available service it's critical functions during normal business hours.

**RTO** Recovery Time Objective, or the time that your application can be down for a given incident.

**RPO** Recover Point Objective, or a measure of how long of a period that data can be lost.

**SSL certificate** Cryptographic certificate for encrypting traffic between two computers.

**Source of truth** When data is stored in multiple places or ways, the "source of truth" is the one that is used when there is a discrepancy between the multiple sources.

**Monitoring** Systems to track and make visible metrics that are useful in identifying system performance.

**Alerting: Systems** to attract attention when performance thresholds are crossed.

**Chaos Engineering** Intentionally causing issues in order to validate that a system can respond appropriately to problems.


=============================================

**Baseline**	Measurement of conditions at the start of your project used to make planning decisions

**Cloud	Servers** and resources that are accessed over the internet

**Cloud Computing**	Storing and accessing data and applications over the Internet instead of a local or networked computer's hard drive

**High Performance Computing** (a.k.a. **supercomputing**)	Supercomputing harnesses the computing power of multiple computers and aggregates them to tackle complex problems in business and academia

**Infrastructure as Code**	The process of provisioning and managing your cloud resources by writing a template file that is both human readable, and machine consumable

**On-premises**	Hardware and software that is contained within the physical confines of a business or their assigned section of a data center

**Serverless**	Compute model where the developer doesn’t need to be concerned with the server because the cloud provider takes care of it



**11 9’s** guarantee	**99.999999999%** durability of objects over a given year. This durability level corresponds to an average annual expected loss of 0.000000001% of objects	
**AMI** (**Amazon Machine Image**)	Provides the configuration details needed to launch an EC2 instance

**Autoscaling** / Auto Scaling	Automatic changes that add or remove compute resources

**Availability Zones**	A logical data center in an AWS region with redundant and separate power, networking and connectivity reducing the likelihood of two zones failing simultaneously

**AWS Aurora**	Fully-managed MySQL-compatible relational database engine that combines the speed and availability of commercial databases with the simplicity and cost-effectiveness of open source databases. Aurora is VERY fast-10 times as fast as Microsoft SQL, but slightly more costly

**AWS CloudFront**	Fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency

**AWS DynamoDB**	Very fast scalable NoSQL database service that manages distri­buted replicas of your data for high availa­bility

**AWS Local Zones**	A type of AWS infrastructure deployment that places AWS compute, storage, database, and other select services closer to large population, industry, and IT centers where no AWS Region exists today

**AWS Outposts**	A hybrid cloud service that includes a physical AWS compute and storage appliance that resides on-premise in the customer datacenter

**AWS RDS**	Relational database that simplifies the process of configuring, operating, and scaling. Provides cost-efficient and resizable capacity for an industry-standard relational database and manages common database administration tasks

**AWS Regions**	A geographical location with a collection of availability zones physically isolated from and independent of every other region

**AWS Support**	Paid support plans offering AWS customers access to AWS technical experts and professional guidance	

**BLOBS (Binary Large Objects)**	Used to store binary data including videos, images, gifs, and audio files	

**BYOL**	A licensing model that lets companies use their licenses flexibly, whether on-premise, or in the cloud

**Capacity Reservations**	Reserve capacity for your EC2 instances in a specific Availability Zone for any duration.

**CLOBs (Character Large Objects)**	Used to store text data including text files, PDF documents, word processing documents	

**DBA	A Database Architect** is responsible for designing, deploying and managing the data architecture for an organizat
ion.

**Dedicated Hosts**	Pay for a physical host that is fully dedicated to running your instances, and bring your existing per-socket, per-core, or per-VM software licenses to reduce costs.

**Dedicated Instances**	Pay, by the hour, for instances that run on single-tenant hardware.

**Durability**	The probability that the object will remain intact and accessible after a period of one year	

**EBS	Elastic Block Store** - cloud-based block storage system provided by Amazon Web Services (AWS) that is best used for storing persistent data

**EC2 Spot Fleet**	A collection of EC2 Spot and On-Demand instances

**Edge Cache**	A high-speed data storage layer which stores a subset of data, typically transient in nature, close to the end user so that future requests for that data are served up faster

**dge Location**	A physical site that CloudFront uses to cache copies of your content for faster delivery to users at any location

**EFS	Elastic File System - a simple

**Fault Tolerance**	The property that enables a system to continue operating properly in the event of the failure of (or one or more faults within) some of its components	

**HDD**	Category of EBS hard disk drive. Can be throughput optimized (workhorse) or cold (infrequently scanned)

**High Availability**	Refers to systems that are durable and likely to operate continuously without failure for a long time	

**Horizontal Scaling**	Adding more nodes or workers a.k.a. scaling in and scaling out

**Hybrid Cloud**	A mix of public cloud, private cloud on-premise data centers and edge locations

**Lifecycle Policies**	Automate the actions you want to take on an object in an S3 bucket over its lifetime, for example, move them to another storage class, archive them after a number of days or years, or delete them.

**Memory-Optimized**	The R3 instance class recommended for applications that require high memory performance	

**NoSQL Databases	Built** for specific data models with flexible schemas for building modern applications and widely recognized for their ease of development, functionality, and performance at scale

**On-Demand Instances**	An AWS service or technology that can be acquired at any time for a predetermined standard cos

**Points of Presence**	AWS Edge Locations and Regional Edge Caches used for both AWS CloudFront and Lambda@Edge to deliver content to end users at high speeds

**Read Replica**	A read-only copy of a database instance; applications can connect to a read replica just as they would to any DB instance

**Reserved Instances**	An AWS service or technology that can be reserved for a period of time iat a discount in exchange for a payment commitment

**S3	Amazon Simple Storage Service** general purpose storage used for frequently accessed files

**S3 Endpoints**	A private connection between your VPC and S3 that doesn’t require internet access, potentially reducing NAT gateway costs

S**avings Plans**	Reduces your Amazon EC2 costs by making a commitment to a consistent amount of usage, in USD per hour, for a term of 1 or 3 years.

**Scheduled Instances**	Purchase instances that are always available on the specified recurring schedule, for a one-year term.

**SDD	Category** of EBS solid state drive. Can be IOPS optimized for databases (fast) or general purpose for boot volumes and dev/test systems

**Spot Instances**	an EC2 instance that can be acquired by bidding for a low price in exchange for the understanding that AWS can reclaim it at any time

**Storage Cache**	A high-speed data storage layer that stores a subset of typically transient data

**Storage-Optimized**	Instances are designed for workloads that require high, sequential read and write access to very large data sets on local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications	

**Tagging**	Allows you to name and classify S3 buckets. AWS can provide a usage and cost report based on tags

**Vertical Scaling**	Adding more resources to the system (memory and CPU) a.k.a. scaling up and down

**VPC Peering**	A networking connection between two AWS VPCs that allows you to route traffic between them using private IP addresses

**VPC Sharing**	allows you to share subnets with other AWS accounts in your organization

**Cloud performance optimization**

**Auto Scaling Group**	AWS EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management	

**Availability**	A storage volume’s ability to deliver data upon request

**AWS Direct Connect**	A cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS

**AWS DynamoDB**	A key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications

**AWS Global Accelerator**	Service that improves the availability and performance of your applications with local or global users. It provides static IP addresses that act as a fixed entry point to your application endpoints

**AWS RDS**	A web service that makes it easier to set up, operate, and scale a relational database in the cloud

**AWS VPC Endpoints**	Used to privately connect your VPC to other AWS services and endpoint services

**Burstable Performance** Instances	T3, T3a, and T2 instances, are designed to provide a baseline level of CPU performance with the ability to burst to a higher level when required by your workload

**CloudFront**	Uses a global network of 216 Points of Presence To deliver content to end users with lower latency

**Consumer**	Receives messages to an SQS queue

**Content Delivery Network**	A series of distributed servers that deliver content to users based on location

**Data Durability**	Refers to long-term data protection, so the stored data does not suffer from degradation or some other corruption. Durability is focused on redundancy, , sodata is never lost or compromised

**Decoupling**	Refers to components remaining autonomous and unaware of each other as they complete their work for some greater output

**Edge Cache**	Servers used to store content closer to end users

**Edge Location**	Where end users access services provided by AWS

**Elastic Block Store**	High performance block storage service designed for use with Amazon Elastic Compute Cloud (EC2) for both throughput and transaction intensive workloads

**Elastic File System**	Fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically

**Elasticity**	The ability to grow or shrink infrastructure resources dynamically as needed to automatically adapt to workload changes, maximizing the use of resources and resulting in savings in infrastructure costs

**Expedited Retrieval**	Faster access to your data when you need to have almost immediate access to your information within 1-5 minutes. This retrieval type can be used for archives up to 250MB.

**FIFO**	Queues designed to ensure that the order in which messages are sent and received is strictly preserved and that each message is processed exactly once- First In, First Out

**GPU (Graphics Processing Unit)**	A programmable chip used to manage and boost the performance of video and graphics. GPU renders images, animations, and video for the computer's screen

**Instance Family**	Six distinct classifications of EC2 instance optimized for different types of applications

**IOPS	Input/output operations per second** (IOPS, pronounced eye-ops) is an input/output performance measurement used to benchmark computer storage devices like hard disk drives (HDD), solid state drives (SSD)

**Latency**	Generally refers to a transport or transfer delay

**Latency Routing**	Configuration where DNS requests are routed from the AWS region that provides the lowest latency

**Launch Configuration**	an instance configuration template that an Auto Scaling group uses to launch EC2 instances

**Lift and Shift**	The process of moving your application from an on-premises environment to the cloud without making any major changes to the code

**Non-Relational Database**	A database that does not use the tabular schema of rows and columns found in most traditional database systems. Instead, non-relational databases use a storage model that is optimized for the specific requirements of the type of data being stored

**Optimized Instances**	Instance types optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, GPU, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your applications

**Performance**	Refers to the number of IOPS or the amount of throughput (measured in megabytes per second) that the storage volume can deliver

**Placement Groups**	Influence the placement of a group of interdependent instances to meet the needs of your workload	

**Points of Presence**	Made up of Edge locations and regional edge caches

**Predictive Scaling**	A feature of AWS Auto Scaling uses machine learning to schedule the right number of EC2 instances in anticipation of approaching traffic changes. Predictive Scaling predicts future traffic, including regularly-occurring spikes, and provisions the right number of EC2 instances in advance

**Producer**	Sends messages to an SQS queue

**Provisioned Capacity**	Paying up front to ensure that S3 expedited retrieval capacity is available when you need it

**Read Replica**	A copy of the master db that reflects changes to the master instance in almost real time

**Relational Database**	A set of formally described tables from which data can be accessed or reassembled in many different ways without having to reorganize the database tables

**Retrieval Job**	An asynchronous operation in which you first initiate a job, and then download the output after the job completes

**Route 53**	A highly available and scalable cloud Domain Name System (DNS) web service

**S3 Glacier**	Storage service optimized for infrequently used, or "cold data." Glacier is a low-cost storage service that provides durable storage with security features for data archiving and backup

**S3** IA	S3 storage class for data that is accessed less frequently, but requires rapid access when needed.

**SQS**	A fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless application

**Target Utilization**	The threshold we define at how much utilization (in %) we want auto scaling to take place

**Throughput**	Measurement of data that can be transferred from one location to another in a given amount of time used to measure the performance of hard drives and RAM as well as Internet and network connections

**Transient or Ephemeral Data**	Data created within an application session, and at the end of the session, it is discarded or reset back to its default and not stored

**VPC**	A logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network you define

**Workload**	A collection of resources and code that delivers business value, such as a customer-facing application or a backend process




### **Infra as code**

**Arguments**	An argument assigns a value to a particular name ex.- server_name = JR234. In this example, server_name is the argument name and JR234 is the argument value

**Automation**	The use of software to create repeatable instructions and processes to replace or reduce human interaction with IT systems

**AWS CloudFormation**	Allows for the use of code for the automation of complex infrastructure management in the AWS Cloud

**Blocks**	Containers for other content and usually represent the configuration of some kind of object, like a resource

**Cloud Agnostic/Cloud Neutral**	Software that is not tied to any particular provider and is portable between them

**Cloud Governance**	The people, process, and technology associated with your cloud infrastructure, security, and operations. It involves a framework with a set of policies and standard practices

**Cloud Neutral**	Software being deployed in the cloud does not use APIs that lock customers and IT service providers into a specific cloud provider

**Expressions**	An expression in Terraform is anything that returns a value

**Go**	An open source programming language that makes it easy to build simple, reliable, and efficient software

**HCL	Configuration language** authored by HashiCorp and used with HashiCorp's cloud infrastructure automation tools, like Terraform

**Infrastructure as Code**	The process of managing and provisioning computer resources through human and machine-readable definition files, rather than physical hardware configuration or interactive configuration tools like the AWS console

**Integrated Development Environment (IDE)**	A software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger

**IT Audit**	The examination and evaluation of an organization's information technology infrastructure, policies and operations

**Lifecycle Environment**	Application life cycles are divided into life cycle environments, which represent each stage of the application life cycle- Development, QA, UAT, Staging, Production, etc

**Local** Backend	Stores the **terraform.tfstate** file on your local disk

**Module**	A set of Terraform configuration files in a folder

**Provider**	Responsible for understanding API interactions and exposing resources. Providers generally are an IaaS (e.g. AWS, GCP, Microsoft Azure)

**Remote Backend**	Allows you to store the terraform.tfstate file in a remote, shared storage location

**Resources**	Describes one or more infrastructure objects, such as virtual networks, compute instances, or higher-level components such as DNS records

**Root** Module	The module in the current working directory

**Secrets**	Sensitive data that needs to be kept private

**Standard Operating Procedure (SOP)**	The documented processes that a company has in place to ensure services and/or products are delivered consistently every time

**Terraform State**	Information about what infrastructure Terraform created




### **Serverless**

**Amazon Elastic Container Registry (ECR)**	Registry that simplifies the storage and management of container images.

**Amazon Elastic Container Service (ECS))**	Service that simplifies the storage and management of container images.

**API**	A software intermediary that allows two applications to talk to each other

**API Gateway**	Fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale

**API Gateway Event**	One way to trigger Lambda. When someone or something is calling the gateway, it will trigger Lambda

**AWS Fargate**	Serverless compute engine for ECS and EKS

**AWS Lambda**	Run code for virtually any type of application or backend service without provisioning or managing servers

**AWS Step Functions**	organizes AWS services into serverless workflows ,allowing rapid application development

**Cloud Native**	An app that has been engineered specifically to use cloud services and infrastructure

**Cognito	Integrates** user sign-up, sign-in, and access control from social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via 

**SAML 2.0.** to your web and mobile apps quickly and easily, scaling to millions of users

**Cold Start**	The delayed response that occurs when a new labda instance receives its first request

**Dashbird.io**	A 3rd party serverless observability platform built to manage serverless application

**DynamoDB**	AWS managed Key-value and document NoSQL database that delivers single-digit millisecond performance on a serverless platform

**Elastic Kubernetes Service (EKS)**	Managed service for containerized applications using Kubernetes

**Event**	Can be almost anything- a file being uploaded, an API request, a login, a database update, etc. Events trigger lambda functions

**Event Source**	The AWS service or internal/external event action that triggers the lambda function

**FaaS**	Category of serverless cloud computing via serverless architectures

**Function**	A piece of code running in AWS lambda that is triggered by an event

**GB/sec**	Measure of compute time used to calculate costs in AWS lambda

**Iaas**	Online platforms that provide computing services over the internet

**JSON (JavaScript Object Notation)**	A lightweight data-interchange format that is both human-readable and easy for machines to parse and generate

**Keep Warm**	A periodic ping or function call to lambdas to keep them on in order to avoid the delay of

**Lambda Function	AWS Lambda** code containing associated configuration information, such as its name and description and the resources it requires to execute.

**Lift and Shift**	The process of moving your application from an on-premises environment to the cloud without making any major changes to the code.

**Microservices**	An approach to writing software where apps are broken down into their smallest components, independent from each other.

**Runtime**	Relates to what coding language the function is developed in

**SQS**	AWS managed message queuing service that enables service decoupling, distributed systems, and serverless applications

**Triggers**	Actions caused by specific events that will further trigger the lambda function

**XML (Extensible Markup Language)**	A markup language that defines a set of rules for encoding documents in a format that can be easily read by humans and machines
