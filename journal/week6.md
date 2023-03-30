# Week 6 — Deploying Containers

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


