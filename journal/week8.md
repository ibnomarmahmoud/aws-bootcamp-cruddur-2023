# Week 8 — Serverless Image Processing

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Fixing the Frontend Issue from previous week

It was found that I have an issue with the JWT Token verify as the backend was missing the Cognito Pool environemtal variables 
![image](https://user-images.githubusercontent.com/125532497/233379115-d4a3dd93-73cf-4901-9f2b-6875893b0df3.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implement CDK Stack

Instructions was followed as per the Live stream and the following recorded video and CDK stack was implemneted 

![image](https://user-images.githubusercontent.com/125532497/233326782-c390dbff-031b-48d4-8433-4f5b8be0ad43.png)

**Lambda Function**
![image](https://user-images.githubusercontent.com/125532497/233357759-d2042a08-3182-43c4-ab74-53dfbd71f053.png)


**S3 Bucket**
![image](https://user-images.githubusercontent.com/125532497/233358033-4c9d0e8a-0f63-4419-83db-28e0b1ed1948.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Serve Avatars via CloudFront

CloudFront distribution was created towards S3 origin 

![image](https://user-images.githubusercontent.com/125532497/233359126-b0e253cc-8c22-4347-ae62-d0b33dc22461.png)

Also Route 53 for our hosted zone was updated so that assets.eg-cruddur.online is being resolved as the Cloud Front

![image](https://user-images.githubusercontent.com/125532497/233359466-33949e9c-35d3-49d9-8c1e-6d9ebcc9088d.png)

I sticked to the initial implemnetation and didn't create a seperate bucket for processed avatars and another for Avatar uploads , Lambda function was triggered successfully 

![image](https://user-images.githubusercontent.com/125532497/233363473-35327c5f-5082-432d-81f0-346942d6bd01.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implement Users Profile Page

The background and Avatar were reflected from the S3 

![image](https://user-images.githubusercontent.com/125532497/233385822-e254c73b-76cc-4894-8e29-cecd45bf0063.png)

Also upon Crudduring , the count had been incremented 

![image](https://user-images.githubusercontent.com/125532497/233389011-1a578071-e358-4fa0-a460-9482942b33cb.png)

One issue faced , It was not showing any info related to the User as backend was complaining about the non existing "bio" field in users table 

```
psycopg.errors.UndefinedColumn: column users.bio does not exist
LINE 10:       users.bio,
```

Before proceeding further in the video and the use of the migration script to add the Bio column , I have modified the schema to include this bio field and it worked as shown above but migration scripts had been updated anyway and the setup script was modified as well

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implement Users Profile Form

The Dispaly Name and Bio had been modified successfully via the "Edit Profile" button 

![image](https://user-images.githubusercontent.com/125532497/234564566-05ee3a58-d92b-44db-bb44-d31de5495a36.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Presigned URL generation via Ruby Lambda / HTTP API Gateway with Lambda Authorizer / Create JWT Lambda Layer 



![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Render Avatars in App via CloudFront 


