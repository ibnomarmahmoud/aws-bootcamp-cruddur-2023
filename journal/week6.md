# Week 6 — Deploying Containers
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Preparations 

Post the Live stream and after Andrew declared that the week may have some spendings since Fargate is not covered in the Free Tier , I suddenly received a mail from AWS because of the new account and a submit request that I am building an application like Twitter as per Andrew's bootcamp and I have received 300$ credits :)
![image](https://user-images.githubusercontent.com/125532497/228462311-45cca416-47a3-4195-af2a-4254fab65c49.png)

![image](https://user-images.githubusercontent.com/125532497/228462511-16d116a8-4aa4-4a94-bef2-4946f11682f5.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Pending Tasks / Snaglist from previous weeks 

- [] Check that Backend is working fine 
- [ ] Check that frontend is working fine 
- [ ] Make sure that scripts are updated  :tada:
- [X] Fix the AWS CLI in gitpod.yaml   :tada:

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Apply the RDS Test Script 

RDS database instance as started after the 7 days

<img width="960" alt="image" src="https://user-images.githubusercontent.com/125532497/228796723-ef532d80-bd5a-434a-8391-7332f76c4429.png">

Tested the connection from the local backend container before pushing to ECR

<img width="697" alt="image" src="https://user-images.githubusercontent.com/125532497/228796976-fb9782be-ec66-48d3-85a9-4a52ceec955e.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implemnet Health-check API and script

![image](https://user-images.githubusercontent.com/125532497/228805875-cdacae7c-8c76-485c-a525-3e1f9b085e16.png)
<img width="458" alt="image" src="https://user-images.githubusercontent.com/125532497/228806523-7053f4ae-f43c-4905-b5c0-29e8195912db.png">


<img width="941" alt="image" src="https://user-images.githubusercontent.com/125532497/228811013-6f2f0caf-5f83-41e9-b2c2-225649b3de7c.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### ECS Cluster Creation

<img width="963" alt="image" src="https://user-images.githubusercontent.com/125532497/228815946-cc31f31e-9ca3-4f02-9b20-7467733cc930.png">

<img width="967" alt="image" src="https://user-images.githubusercontent.com/125532497/228816045-136b19d6-4eaa-4755-a201-5d62a96482be.png">

### Backend Python reporisrory creation 

![image](https://user-images.githubusercontent.com/125532497/228834470-7258ba6e-9c05-4a94-aea7-9b32e3a5c80a.png)

How to connect to ECR repository for pulling the images

<img width="493" alt="image" src="https://user-images.githubusercontent.com/125532497/228835642-f37e40f9-6444-4fce-b396-e36c7248eec8.png">

<img width="710" alt="image" src="https://user-images.githubusercontent.com/125532497/228836717-598239bc-2de4-4f69-935a-eb5f9b65171f.png">

Python Image was pulled from Docker hub , tagged and pushed to the private repo after login to ECR 
<img width="750" alt="image" src="https://user-images.githubusercontent.com/125532497/228837353-045f33e3-fafa-4176-8ae9-d3de9d7de048.png">

<img width="794" alt="image" src="https://user-images.githubusercontent.com/125532497/228837619-6c432735-c4ba-4c31-bfab-be3eb8680d08.png">



<img width="500" alt="image" src="https://user-images.githubusercontent.com/125532497/228840353-320c4ea6-e2e6-4d42-b5f3-79c4f61ba091.png">

<img width="989" alt="image" src="https://user-images.githubusercontent.com/125532497/228840526-bbe26736-3c8f-4190-88aa-fe8f2f5c20b0.png">

### Have Cloudwatch Logging group created before task definition 

Found it created since the Lamdbda function so just updated the retension 

![image](https://user-images.githubusercontent.com/125532497/228845152-4c848415-749d-4103-9a50-e91080c43877.png)

## Backend Task desfinition , we are passing sensitive data to SSM instead of the Secret Manager to avoid paying money 

![image](https://user-images.githubusercontent.com/125532497/228847608-06db3dc2-8253-4617-bcf2-80a097c582d2.png)

## Create Backend task definition 

![image](https://user-images.githubusercontent.com/125532497/228859364-b3a48163-f1ff-42d2-8c64-42a00db99619.png)



### Update RDS SG to have Postgres Port be accessed from Service SG only , previuslly it was from our workstation only 

![image](https://user-images.githubusercontent.com/125532497/228863367-54ad1f70-73cd-4ea8-9966-13f34bf24859.png)

## Create Service 

From the definbition , choose the latest image , Service SG 

### Problem Faced

![image](https://user-images.githubusercontent.com/125532497/228872464-8a955e35-5bd9-4640-ac74-5f524af62521.png)

```
https://stackoverflow.com/questions/53370256/aws-creation-failed-service-already-exists-service-awsservicediscovery-stat
```

![image](https://user-images.githubusercontent.com/125532497/228873734-b2bfbb7f-c1b8-47b2-b809-51541e83cfca.png)

![image](https://user-images.githubusercontent.com/125532497/228874053-84a38ad1-9987-443a-9b13-0235c634be6b.png)


## Then Failed due to health checks

![image](https://user-images.githubusercontent.com/125532497/228876023-f044d524-8786-4a73-8d05-3e6b5004498b.png)

##  Finaly it stabilized

![image](https://user-images.githubusercontent.com/125532497/228903050-234110a3-ae24-4c48-a09c-52c5b81edc91.png)

![image](https://user-images.githubusercontent.com/125532497/228903439-c2b345ca-2d69-4226-b854-74191c1b8535.png)


## Backend Accessed after allowing port 4567  for the SG

![image](https://user-images.githubusercontent.com/125532497/228905212-a9c4cb35-db8d-4f4a-bbe1-057139631187.png)

![image](https://user-images.githubusercontent.com/125532497/228905712-8b2ebfa5-aad0-4a4f-bf77-6fe47518e205.png)

![image](https://user-images.githubusercontent.com/125532497/228906031-da36799d-535c-4384-8ae7-e93fa17f7466.png)


### AFter Adding the ALB

![image](https://user-images.githubusercontent.com/125532497/228954574-a63f4c69-04e4-4982-b05c-a83dcf7937b0.png)

Healthy TG

![image](https://user-images.githubusercontent.com/125532497/228955352-ff6d2a1f-7e57-4017-9f4b-78685bd65b3e.png)

Access from LB and it is no more accessible directly with Task public IP provided by ENI

![image](https://user-images.githubusercontent.com/125532497/228955723-02b5a332-ecd6-4edc-a37e-249c0b0f3567.png)

### FE ECR

![image](https://user-images.githubusercontent.com/125532497/228968133-84cf7b1d-42cc-49e2-94d6-1d0eb1378a03.png)


![image](https://user-images.githubusercontent.com/125532497/228968914-c51866ae-ef5b-40bb-ae93-25cc3c7b543d.png)

![image](https://user-images.githubusercontent.com/125532497/228968966-8fc8c7ec-876e-4df0-9dda-34000b1797e2.png)

![image](https://user-images.githubusercontent.com/125532497/228969122-f2334b9f-757b-47e6-ba9f-b24cf3ffecdd.png)

## Domain Registration

![image](https://user-images.githubusercontent.com/125532497/229273016-8d1d0fdf-8de3-41ca-87a2-62e21121a4f6.png)

![image](https://user-images.githubusercontent.com/125532497/229277617-5e251706-1a1c-49f8-98d6-2d628a46c643.png)
![image](https://user-images.githubusercontent.com/125532497/229277631-11e83726-3b3d-4dec-9177-1ee149ad0645.png)

![image](https://user-images.githubusercontent.com/125532497/229278032-6db8a929-c92f-4127-bf15-3b070f36bdad.png)

![image](https://user-images.githubusercontent.com/125532497/229278098-15f71061-7420-47fe-95b0-e29db489c8fe.png)

![image](https://user-images.githubusercontent.com/125532497/229278852-341a7d49-b66c-45b8-87c9-7329f6221711.png)


![image](https://user-images.githubusercontent.com/125532497/229284494-0d5750ad-3540-4329-ae40-e7fd029a8324.png)


![image](https://user-images.githubusercontent.com/125532497/229286964-c18fddf3-b363-4705-a677-ed64c0ffe382.png)

![image](https://user-images.githubusercontent.com/125532497/229287554-0f0ea760-7555-44e4-86a9-31509003e1f6.png)
![image](https://user-images.githubusercontent.com/125532497/229287580-44949f16-b10e-4bc0-86ec-607563a3afeb.png)

![image](https://user-images.githubusercontent.com/125532497/229288150-9ed502d6-8ba5-49b7-843a-453534421da7.png)

