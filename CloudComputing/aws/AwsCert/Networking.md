# Networking 


## VPC

## DirectConnect

## ELB

## Route53

## CloudFront



VPC is an isolated segment of the AWS network infrastructure, allowing you to securely provision your cloud resources. 

VPC Subnets allow you to segment your VPC CIDR block, forming smaller network segments across multiple availability zones within your VPC region. 


Internet Gateway is an AWS managed component attached to your VPC, and it provides a connection between your isolated VPC and the outside world, essentially the internet. To enable a subnet to use the internet gateway, it needs a route. 

Route tables are used to make sure that subnets can communicate with each other and that traffic knows where to go.
Every subnet that you create is automatically associated with the main route table for the VPC.

## Direct Connect
Direct Connect is an AWS service that establishes a dedicated network connection between your premises and AWS. You can create this private connectivity to reduce network costs, increase bandwidth, and provide more consistent network experience compared to regular internet-based connections.


## Elastic Load Balancers (ELB)
Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, Docker containers, IP addresses, and Lambda functions. 


## Amazon Route 53

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) service. You can use Route 53 to perform three main functions in any combination:
domain registration, DNS routing, and health checking.

When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to DNS queries.
  
The routing policies available are:
-	Simple Routing
-	Weighted Routing
-	Latency-based Routing
-	Failover Routing
-	Geolocation Routing
-	Geo-proximity Routing
-	Multivalue Answer Routing


## CloudFront

A content delivery network (CDN) is system of distributed servers (network) that deliver webpages and other web content to a user based on the geograpich locations of the user, the origin of the webpage, and a content delivery server.

- Edge Location - This is the location where content will be cached. This is separate to an AWS Region
- Origin - This is the origin of all the files that the CDN will distribute. This can be either an S3 Bucket, an EC2 Instance, an Elastic Load Balancer or Route53
- Distribution - This is the name given the CDN which consists of a colleciton of Edge Locations
- Web Distribution - Typically used for Websites
- RTMP - Used for Media Streaming
- Edge locations are not just READ only - you can write to them too (eg: put an object to them)
- Objects are cached for the life of the TTL (Time To Live)
- Can clear cached objects, but will be charged

## CloudFront vs S3  Transfer Acceleration

S3 Transfer Acceleration optimizes the TCP protocol and adds additional intelligence between the client and the S3 bucket, making **S3 Transfer Acceleration** a better choice if a **higher throughput** is desired. If you have objects that are **smaller than 1GB** or if the data set is less than 1GB in size, you should consider using **Amazon CloudFront**'s PUT/POST commands for optimal performance.




