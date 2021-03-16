#	Compute 

EC2 - Amazon Elastic Compute Cloud 

ECS - Amazon Elastic Container Service

ECR - Amazon Elastic Container Registry

EKS - Amazon Elastic Container Service for Kubernetes

Amazon Lightsail 

AWS Fargate

AWS Lambda

AWS Batch



# EC2

## EC2 Pricing Models

### On Demand

Allows you to pay a **fixed rate** by the **hour** (or by the **second**) with no commitment

⇒ suitable for use cases where you dont want any long term commitment like testing and POCs, **spiky**, unpredictable workloads that cannot be interrupted

### Reserved

Provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. Contract Terms are **1 Year** or **3 Year** Terms

- Standard Reserved Instances
    - can change Availability Zone, instance size (for Linux OS), networking type
- Convertible Reserved Instances
    - can change Availability Zone, instance size (for Linux OS), networking type
    - can change instance families, operating system, tenancy, and payment option
- Scheduled Reserved Instances

### Spot

These are unused EC2 instances that can bid for. Once your bid exceeds the current spot price the instance is launched. The instance **can be shuted down anytime** the spot price becomes greater than your bid price.

⇒ providing for even greater saving if your app have flexible start and end times, very low compute prices, urgent computing needs for large amounts of additional capacity, for a workload with several Reserved Instances reading from a queue, can use Spot Instances to alleviate heavy traffic in a cost-effective way

### Dedicated Hosts

Physical EC2 server. reduce costs by allowing to use your existing server-bound **software licenses** (oracle license...) 

- can be purchased on-demand (hourly)
- can be purchased as a reservation

Change Dedicated hosting back to default hosting ⇒ use CLI, SDK, API, stop instance befor change

## EBS

- Termination Protection is turned off by default, you must turn it on
- On an EBS-backed instance, the **default action is for the root EBS volume to be deleted** when the instance is terminated but **any additional volumes by default won't be deleted**
- EBS Root Volumes of your DEFAULT AMI's (amazone machine image) **CAN be encrypted** by use a third party tool or creating AMI's in the aws console or using the API
- Additional volumes can be encrypted

## EC2  Security Groups

- All **Inbound** traffic is **blocked by default**
- All **Outbound** traffic is **allowed by default** (outbound = response of inbound traffic + request to external services)
- Security Groups are **STATEFUL** ⇒ an inbound rule allowing traffic in, that traffic is automatically allowed back out again
- Changes to Security Groups take effect immediately
- n EC2 instances ↔ 1 security group
- 1 EC2 instances ↔ n security group
- cannot block specific IP address using Security Groups (instead use Network Access Control Lists - VPC)
- can specify allow rules, but not specify deny rules
- **combine of multiple security group: (or)** if there is an allow rules, the request is allowed, evaluation stops (no matter other group's rules)

## Volumes, Snapshots

- Volumes exist on EBS ⇒ virtual hard disk
    - Volumes is **always** be in the same AZ as the EC2 instance
    - Can change EBS volume sizes and storage type when it's running
- Snapshots exist on S3 ⇒ photo of the disk
    - Can take a snapshot while the instance is running, **however** should stop the instance before take the snapshot for volumes that serve as root devices ⇒ snapshots will be consistent
    - Snapshots are incremental ⇒ only the blocks that have change since your last snapshot are moved to S3
        - t1 ⇒ snapshot1
        - create file a.txt ⇒ t2 ⇒ snapshot2
        - S3 2 files is storaged: snapshot1, (snapshot2 -snapshot1)

        ⇒ first snapshot may take some time to create

- Snapshots are point in time copies of Volumes
- AMI (amazone machine image) can be created from both Volumes and Snapshots

### **Move an EC2 volumes from one AZ to another**

- take a snapshot
- create an AMI
- launch the EC2 instance in a new AZ (choose subnet of AZ)

### **Move an EC2 volumes from one region to another**

- take a snapshot
- create an AMI
- copy AMI to other region
- launch the EC2 instance by the copied AMI

### Encrypted

- Snapshots of encrypted volumes are encrypted automatically
- Volumes restored from encrypted snapshots are encrypted automatically
- can share snapshots but only if they are unencrypted
- can encrypt root device volumes when create EC2 instance

### Encrypt an unencrypted root device volume

- take a snapshot of the uncrypted root device volume
- copy snapshot and enable encryption
- create an AMI from the encrypted Snapshot
- use that AMI to launch new encrypted instances

### Snapshot ⇒ AMI ⇒ instance

- copy a snapshot can enable **encryption**
- create AMI from a snapshot can only change **virtualization type** (HVM, PV)
- copy AMI can change **region**
- launch instance from an AMI can choose **AZ**

## EBS vs Instance Store

- Instance Store Volumes are also called Ephemeral Storage
    - use case: temporary storage such as buffers, caches, scratch data or data that is replicated across a fleet of instances such as load-balanced pool
    - very cost effective, very high IOPS
    - **require provision** but charge is based on the **hourly cost of instance**
    - Instance store volumes **can't be stopped**. If the host fails ⇒ lose data
- EBS:
    - EBS backed instances **can be stopped**. If instance is stopped ⇒ not lose data
    - **require provision**, charge is based on the total **amount of storage provisioned**
- can reboot both, not lose data
- By default, both Root volumes will be deleted on termination. Can choose option that keep the root device volume backed by EBS volumes.

## IAM Roles With EC2

- Roles are more secure and easier than storing access key and secret access key in EC2 instance
- Roles can be assigned to an EC2 instance after it's created
- Roles are universal - can use in any region

## AWS Fargate 
-	AWS Fargate is a serverless compute engine for containers.
-	The Fargate launch type allows you to run your containerized applications without the need to provision and manage the backend infrastructure. Just register your task definition and Fargate launches the container for you.
-	It works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS).
-	Fargate makes it easy for you to focus on building your applications. It removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.


## AWS Batch   

Fully managed batch processing at any scale. It used to manage and run batch computing workloads within AWS. Batch computing is primarily used in specialist use cases, which require a vast amount of computer power across a cluster of compute resources to complete batch processing, executing a series of jobs or tasks. 
