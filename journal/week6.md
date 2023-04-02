# Week 6 — Deploying Containers
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Preparations 

Post the Live stream and after Andrew declared that the week may have some spendings since Fargate is not covered in the Free Tier , I suddenly received a mail from AWS because of the new account and a submit request that I am building an application like Twitter as part of Andrew's bootcamp and I have received 300$ credits :)

![image](https://user-images.githubusercontent.com/125532497/228462311-45cca416-47a3-4195-af2a-4254fab65c49.png)

![image](https://user-images.githubusercontent.com/125532497/228462511-16d116a8-4aa4-4a94-bef2-4946f11682f5.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Apply the RDS Test Script 

RDS database instance was started after automatically after being stopped for 7 days

<img width="960" alt="image" src="https://user-images.githubusercontent.com/125532497/228796723-ef532d80-bd5a-434a-8391-7332f76c4429.png">

So I tested the connection from the local backend container before pushing to ECR

<img width="697" alt="image" src="https://user-images.githubusercontent.com/125532497/228796976-fb9782be-ec66-48d3-85a9-4a52ceec955e.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implemnet Health-check API and script

The health check was tested and it was working fine , the issue is that I forgot it since it was missed in week-6-again repo and had to re-do all coming steps once more after having the ECS Cluster running due to missing the health check scripts and once I did the re-built again , I forgot to make the script executable 

![image](https://user-images.githubusercontent.com/125532497/228805875-cdacae7c-8c76-485c-a525-3e1f9b085e16.png)
<img width="458" alt="image" src="https://user-images.githubusercontent.com/125532497/228806523-7053f4ae-f43c-4905-b5c0-29e8195912db.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### ECS Cluster Creation

As a pre-step , I have set all the environmnetal variables and exported them to gitpod

<img width="941" alt="image" src="https://user-images.githubusercontent.com/125532497/228811013-6f2f0caf-5f83-41e9-b2c2-225649b3de7c.png">

The namespace was created and the ECS cluster was provisioned 

<img width="963" alt="image" src="https://user-images.githubusercontent.com/125532497/228815946-cc31f31e-9ca3-4f02-9b20-7467733cc930.png">
<img width="967" alt="image" src="https://user-images.githubusercontent.com/125532497/228816045-136b19d6-4eaa-4755-a201-5d62a96482be.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Create ECR repo and push image for backend-flask

The repo was created 
![image](https://user-images.githubusercontent.com/125532497/228834470-7258ba6e-9c05-4a94-aea7-9b32e3a5c80a.png)
The Python image was pushed to ECR , initially the base image was pulled from Docker hub , tagged and pushed back to the private repo after login to ECR 


<img width="710" alt="image" src="https://user-images.githubusercontent.com/125532497/228836717-598239bc-2de4-4f69-935a-eb5f9b65171f.png">
<img width="750" alt="image" src="https://user-images.githubusercontent.com/125532497/228837353-045f33e3-fafa-4176-8ae9-d3de9d7de048.png">
<img width="794" alt="image" src="https://user-images.githubusercontent.com/125532497/228837619-6c432735-c4ba-4c31-bfab-be3eb8680d08.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/125532497/228840353-320c4ea6-e2e6-4d42-b5f3-79c4f61ba091.png">
<img width="989" alt="image" src="https://user-images.githubusercontent.com/125532497/228840526-bbe26736-3c8f-4190-88aa-fe8f2f5c20b0.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Have Cloudwatch Logging group created before task definition 

Found it created since the Lamdbda function so just updated the retension 
![image](https://user-images.githubusercontent.com/125532497/228845152-4c848415-749d-4103-9a50-e91080c43877.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Passing the sensitive data to SSM instead of the Secret Manager to avoid paying money before the backend task definition 
![image](https://user-images.githubusercontent.com/125532497/228847608-06db3dc2-8253-4617-bcf2-80a097c582d2.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Creating the Backend task definition 

After all previous step , I have created the backend task 
![image](https://user-images.githubusercontent.com/125532497/228859364-b3a48163-f1ff-42d2-8c64-42a00db99619.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
## Deploy Backend Flask app as a service to Fargate

The task was created but it kept on failing due to the roles and the missing health check script as previouslly mentioned 

![image](https://user-images.githubusercontent.com/125532497/228873734-b2bfbb7f-c1b8-47b2-b809-51541e83cfca.png)

![image](https://user-images.githubusercontent.com/125532497/228874053-84a38ad1-9987-443a-9b13-0235c634be6b.png)

![image](https://user-images.githubusercontent.com/125532497/228876023-f044d524-8786-4a73-8d05-3e6b5004498b.png)

But after fixing the roles and rebuilding with the health-checks , finally it stabilized :tada:

![image](https://user-images.githubusercontent.com/125532497/228903050-234110a3-ae24-4c48-a09c-52c5b81edc91.png)
It shown here that it kept starting and stopping 
![image](https://user-images.githubusercontent.com/125532497/228903439-c2b345ca-2d69-4226-b854-74191c1b8535.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Create ECR repo and push image for fronted-react-js

The instructions were followed and the image was pushed to ECR

![image](https://user-images.githubusercontent.com/125532497/229377231-83d65bdf-697e-4380-b503-e4301e04b312.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Deploy Frontend React JS app as a service to Fargate

The Service was deployed successfully but this was done after updating the definitions to include the Load balancer for both backend and frontend 

![image](https://user-images.githubusercontent.com/125532497/228968914-c51866ae-ef5b-40bb-ae93-25cc3c7b543d.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Provision and configure Application Load Balancer along with target groups

Both Target groups were created and the tasks were registered successfully and showed healthy status 
![image](https://user-images.githubusercontent.com/125532497/228968966-8fc8c7ec-876e-4df0-9dda-34000b1797e2.png)

Then I tested accessing the frontend from the loadbalancer endpoint 

![image](https://user-images.githubusercontent.com/125532497/228969122-f2334b9f-757b-47e6-ba9f-b24cf3ffecdd.png)

And for the Backend , it was accessed successfully after allowing port 4567 with Task public IP provided by ENI

![image](https://user-images.githubusercontent.com/125532497/228905212-a9c4cb35-db8d-4f4a-bbe1-057139631187.png)

![image](https://user-images.githubusercontent.com/125532497/228905712-8b2ebfa5-aad0-4a4f-bf77-6fe47518e205.png)

Then after adding the ALB and application Load Balancer , it is now accessible 

![image](https://user-images.githubusercontent.com/125532497/228955723-02b5a332-ecd6-4edc-a37e-249c0b0f3567.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Domain Registration
I didn't create it previouslly since I didn't know earlier whether it would be covered by the AWS Credits or not and what would be its best name so I created it from GoDaddy this week ( eg-cruddur.online )
![image](https://user-images.githubusercontent.com/125532497/229273016-8d1d0fdf-8de3-41ca-87a2-62e21121a4f6.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Manage your domain useing Route53 via hosted zone

Route 53 hosted zone was created for my domain and I had to update the NS in GoDaddy
![image](https://user-images.githubusercontent.com/125532497/229277631-11e83726-3b3d-4dec-9177-1ee149ad0645.png)
![image](https://user-images.githubusercontent.com/125532497/229277617-5e251706-1a1c-49f8-98d6-2d628a46c643.png)
![image](https://user-images.githubusercontent.com/125532497/229278032-6db8a929-c92f-4127-bf15-3b070f36bdad.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Create an SSL cerificate via ACM
I had some issues in issuing the SSL certificate since its status was kept "Pending verifications" till I created a record for it in Route 53 afterwards it was verified but I didn't find it while creating the rule in ALB and it was found to be created in a different region so I deleted it and re-created a new one 
![image](https://user-images.githubusercontent.com/125532497/229284494-0d5750ad-3540-4329-ae40-e7fd029a8324.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Setup a record set for naked domain to point to frontend-react-js and api subdomain to point to the backend-flask

The records were created in Route 53 as shwon below

![image](https://user-images.githubusercontent.com/125532497/229378965-9a0d3606-fea2-4c68-87e8-3960c2d0f908.png)

And both backend and frontend were accessed directly and from my mobile phone as well 

![image](https://user-images.githubusercontent.com/125532497/229287554-0f0ea760-7555-44e4-86a9-31509003e1f6.png)
![image](https://user-images.githubusercontent.com/125532497/229287580-44949f16-b10e-4bc0-86ec-607563a3afeb.png)


Even I tried the Cognito integration and craeted new user from the web version of the application 

![image](https://user-images.githubusercontent.com/125532497/229288150-9ed502d6-8ba5-49b7-843a-453534421da7.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Secure Flask by not running in debug mode

A new dockerfile was created with "--no-debugger" and "--no-reload" options as per the instructions but building the new image and updating the task was postponed till fiixng some issues in app.py since week 5

And for the sake of ease of deloying the new image , the below script was created 

```
#! /usr/bin/bash

aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
export ECR_BACKEND_FLASK_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/backend-flask"
echo $ECR_BACKEND_FLASK_URL
cd /workspace/aws-bootcamp-cruddur-2023/backend-flask
docker build -t backend-flask .
docker push $ECR_BACKEND_FLASK_URL:latest
cd ..
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json
```
