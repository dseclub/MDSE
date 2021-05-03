# AWS Cloudformation

AWS CloudFormation helps providing a repeatable and reliable mechanism to create complete solutions that can be deployed into any AWS account.
Use JSON or YAML to describe what AWS resources you want to create and configure.


**AWSTemplateFormatVersion** 'version date' (optional) # version of the CloudFormation template. Only accepted value is '2010-09-09'

**Description** 'String' (optional) # a text description of the Cloudformation template

**Metadata** 'template metadata' (optional) # objects that provide additional information about the template

**Parameters** 'set of parameters' (optional) # a set of inputs used to customize the template

**Rules** 'set of rules' (optional) # a set of rules to validate the parameters provided at deployment/update

**Mappings** 'set of mappings' (optional) # a mapping of keys and associated values

**Conditions** 'set of conditions' (optional) # conditions that control whether certain resources are created

**Transform** 'set of transforms' (optional) # for serverless applications

**Resources** 'set of resources' (required) # a components of your infrastructure

**Hooks** 'set of hooks' (optional) # Used for ECS Blue/Green Deployments

**Outputs** 'set of outputs' (optional) # values that are returned whenever you view your stack's properties



**Intrinsic functions** are built-in functions that help you manage your stacks

Use the Fn::Ref function to dynamically assign parameter values to a resource property.
Tag an instance with Fn::Join function.
Add a tag to the instance using Fn::Sub function.

Fn::GetAtt intrinsic function

**User Data**
You can use AWS CloudFormation to automatically install, configure, and start applications on Amazon EC2 instances. Doing so enables you to easily replicate deployments and update existing installations without connecting directly to the instance, which can save you a lot of time and effort.
Deploy an Apache Web server with a simple PHP application via UserData property.  Bootstrapped an EC2 instance.

**Helper scripts**

CloudFormation provides helper scripts. These helper scripts make CloudFormation a lot more powerful and enable you to fine tune templates to better fit your use case. For example, you can update application configuration without recreating an instance.

The helper scripts come pre-installed on Amazon Linux and can be updated periodically by using yum install -y aws-cfn-bootstrap

**Nested Stack**


## Resources

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-applications-eu-west-1.html

https://github.com/awslabs/aws-cloudformation-templates/



## Books
