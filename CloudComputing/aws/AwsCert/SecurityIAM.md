# Security and Identity (IAM, Inspector, WAF)


# IAM

### Region vs Availability Zones
A Region is a geographical area. Each Region consists of 2 (or more) Availability Zones.

An Availability Zones is consists of 1 or more data centers.

![Region](./images/region.png)

### Edge Location
Edge location is used for caching content, consists of CloudFront, Amazon's Content Delivery Network (CDN)

## IAM
### 4 types of permission:
- Users: end users such as people employees of  organization
- Groups: a collection of users
- Policies: made of documents, call Policy documents, in Json format
- Roles: create roles and assign to AWS Resources

### Sumary
- IAM is universal. It does not apply to regions at this time
- The "root account" is simply the account created when first setup your AWS account. It has complete Admin access
- New Users have No permissions when first created
- New Users are assigned **Access Key ID** & **Secret Access Keys** when first created
- Cannot use **Access key ID** & **Secret Access Key** to Login in to the console. Can use this to access AWS via the APIs and Command Line
- If you lose **Access key ID** and **Secret Access Key**, you have to regenerate them
- Always setup Multifactor Authentication on your root account (google authen)
- Can create and customise your own password rotation policies

## WAF
- Web Application Firewall (WAF) A web application firewall is used to defend an application that may contain vulnerabilities from exploitation.
- AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability,
compromise security, or consume excessive resources.
- Using AWS WAF to Control Access to Your Content
- WAF Rules Logic that will dictate what type of requests to allow or block

AWS Firewall Manager Control WAF settings and Security Groups for all AWS accounts from a central management interface.
