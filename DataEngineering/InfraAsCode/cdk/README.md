# AWS Cloud Development Kit (AWS CDK)

CDK is a software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.

AWS CloudFormation enables you to:

- Create and provision AWS infrastructure deployments predictably and repeatedly.

- Leverage AWS products such as Amazon EC2, Amazon Elastic Block Store, Amazon SNS, Elastic Load Balancing, and Auto Scaling.

- Build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure.

- Use a template file to create and delete a collection of resources together as a single unit (a stack).

Use the AWS CDK to define your cloud resources in a familiar programming language. The AWS CDK supports TypeScript, JavaScript, Python, Java, and C#/.Net.

Developers can use one of the supported programming languages to define reusable cloud components known as Constructs. You compose these together into Stacks and Apps.


## Install nodejs and npm
```
sudo apt update
sudo apt install nodejs npm
node --version
npm --version
```

## Install CDK & Bootstrap CDK  & Update it later
```
sudo npm install -g aws-cdk
cdk --version
```

## Initialize new project

### Create a directory to hold our project files
```
mkdir cdkworkshop && cd cdkworkshop
```
### Deploy the CDK Toolkit stack 
```
cdk bootstrap
cdk bootstrap --profile dev
```

### Creates a cfn, S3 Bucket to host your templates etc
```
cdk init sample-app --language python
```

```
python3 -m venv .env
code
source .env/bin/activate
```

### Install python modules in virtual env
```
pip install -r requirements.txt
```

## Validate & list all stacks in the app
```
cdk ls
```

## Compare deployed stack with current state
```
cdk diff
```


## Synthesize the cfn template
```
cdk synth              
```

## Deploy
```
cdk deploy
```
### Remove the resources created by CDK
```
cdk destroy
```


```
cdk metadata
cdk context
cdk doc
cdk help
```


### Check the cdk for potential problems
```
cdk doctor
```



## Resources

https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html

https://github.com/aws/aws-cdk

https://cdkworkshop.com/30-python.html

https://docs.aws.amazon.com/cdk/api/latest/docs/pipelines-readme.html

https://github.com/aws-samples/cdk-pipelines-demo/tree/python

https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-go


