# AWS Cloudformation




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

Intrinsic functions can only be used in certain parts of a template. You can use intrinsic functions in resource properties, outputs, metadata attributes, and update policy attributes.

Fn::GetAtt intrinsic function

**User Data**
You can use AWS CloudFormation to automatically install, configure, and start applications on Amazon EC2 instances. Doing so enables you to easily replicate deployments and update existing installations without connecting directly to the instance, which can save you a lot of time and effort.
Deploy an Apache Web server with a simple PHP application via UserData property.  Bootstrapped an EC2 instance.

**Helper scripts**

CloudFormation provides helper scripts. These helper scripts make CloudFormation a lot more powerful and enable you to fine tune templates to better fit your use case. For example, you can update application configuration without recreating an instance.

The helper scripts come pre-installed on Amazon Linux and can be updated periodically by using yum install -y aws-cfn-bootstrap

**Nested Stack**

The root stack (which is also a parent stack for the first level stacks). This root stack will contain all the other stacks.
The VPC stack. This contains a simple VPC template which the EC2 instance will be placed into.
The IAM instance role stack. This contains the IAM instance role template decoupled form your EC2 template.
The EC2 stack. This contains the EC2 instance you have defined in your previous CloudFormation template.


**Layered stacks**
Layered stacks are a different method of managing common or re-usable components in CloudFormation. The nested stack option results in child stacks that can only be referenced by the parent stack. With Layered stacks the same referencing is possible but also references can be made from multiple stacks. You are not limited to a single parent.

The VPC stack. This contains the same simple VPC template used in the previous lab but with Export added to the Outputs.
The IAM instance role stack. This contains the same IAM instance role used in the previous lab but with Export added to the Outputs.
The EC2 stack. This contains the EC2 instance you have defined in previous labs but will make use of the Fn::ImportValue function.


Layered stacks allow you to create resources that can be used again and again in multiple stacks.
All the stack needs to know is the Export name used. They allow the separation of roles and responsibilities.
For example, a network team could create and supply an approved VPC design as a template.
You deploy it as a stack and then just reference the Exports as needed. Similarly, a security team could do the same for IAM roles or EC2 security groups.


**Package and deploy**
to package, validate and deploy CloudFormation templates with the AWS CLI.

Identify when packaging a template is required
Package a template using aws cloudformation package command
Validate a CloudFormation template using aws cloudformation validate-template command
Deploy a template using the aws cloudformation deploy command

with aws cloudformation package you can refer to the local files directly.
https://docs.aws.amazon.com/cli/latest/reference/cloudformation/package.html









## Resources

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-applications-eu-west-1.html

https://github.com/awslabs/aws-cloudformation-templates/


https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html

https://github.com/aws-samples/cfn101-workshop/

## Books
