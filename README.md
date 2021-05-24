# aws-lambda-test
This is based on Node `serverless` package to automate template and deploy from local to your aws account.

https://www.youtube.com/watch?v=71cd5XerKss

Install serverless npm package:
	1. install npm -g serverless
	2. serverless create -t aws-python --> Template boilerplate
Change and upate the serverless.yml template boilerplate file like this:
service: lambda-test

frameworkVersion: '2'

provider:
  name: aws
  runtime: python2.7
  lambdaHashingVersion: 20201221

functions:
  hello:
    handler: handler.hello
    events:
      - httpApi:
          path: /users/create
          method: get
	3. serverless deploy --aws-profile <profilename>
  
THis will create a new S3 bucket : This will create a new S3 bucket i.e. lambda-test-dev-serverlessdeploymentbucket-gz7olrhooi88

This will create a new Lambda Application: lambda-test-dev

and above runs in stage: dev with Lambda function named as "<service>-<stage>-<functions_name>" i.e. lambda-test-dev-hello, 

This creates an endpoint for the API i.e. 
endpoints:
  GET - https://lyxq3kdack.execute-api.us-east-1.amazonaws.com/users/create
	
Change the Stages:
--------------------
Change the serlverless template yml file:
service: lambda-test

frameworkVersion: '2'

provider:
  name: aws
  runtime: python2.7
  lambdaHashingVersion: 20201221

functions:
  hello:
    handler: handler.hello
    events:
      - httpApi:
          path: /
          method: get
  imageResize:
    handler: handler.imageResize
    events:
        - httpApi:
            path: /imageResize
            method: get
			
	4. serverless deploy --stage prod --aws-profile <profilename>

This will create a new S3 bucket i.e. lambda-test-dev-serverlessdeploymentbucket-gz7olrhooi88

This will create a new Lambda Application: lambda-test-prod

This will create a new Lambda Functions like:
	Lambda function named as "<service>-<stage>-<functions_name>" i.e. lambda-test-prod-hello and lambda-test-prod-imageResize
	
Everytime deployed - this will create 2 new endpoints as there are two functions:
endpoints:
  GET - https://4ya36zn1u1.execute-api.us-east-1.amazonaws.com/
  GET - https://4ya36zn1u1.execute-api.us-east-1.amazonaws.com/imageResize
 
so be careful to use the new endpoint only!