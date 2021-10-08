
## Install nodejs and npm
```
sudo apt update
sudo apt install nodejs npm
node --version
npm --version
```

## Install nodejs v 14
```
sudo apt update
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt -y install nodejs
node  -v
```

## Install CDK & Bootstrap CDK  & Update it later
```
sudo npm install -g aws-cdk
cdk --version
```

## update CDK 
```
sudo npm i -g aws-cdk --force
```


## Initialize new project

### Create a directory to hold our project files
```
mkdir cdkworkshop && cd cdkworkshop
```

### create a new python cdk project:
```
cdk init app --language python
```

# Activate virtual environment
```
# python3 -m venv .venv
source .venv/bin/activate
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

### Deploy the CDK Toolkit stack. once per region
### Creates a cfn, S3 Bucket to host the cfn templates
```
cdk bootstrap
cdk bootstrap --profile dev
```


### Remove the resources created by CDK
```
cdk destroy
```


```
cdk metadata
cdk context
cdk docs or cdk doc
cdk help
```


### Check the cdk for potential problems
```
cdk doctor
```
