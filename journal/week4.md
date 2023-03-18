# Week 4 — Postgres and RDS

## Homwork Submission 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Create RDS Database 

As instructed in the Live Stream , DRS database was created via the CLI command under us-west-2a AZ and started 

<img width="978" alt="image" src="https://user-images.githubusercontent.com/125532497/224531128-42168b9a-119a-4040-8d25-eef98a33219f.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Local Postgres Database

Local Postgres container was already started since Week1

<img width="978" alt="image" src="https://user-images.githubusercontent.com/125532497/224531217-b3225b60-911d-493c-bd6f-87eb5366b222.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Environmental Variables Setting 

CONNETION_URL and PROD_CONNECTION_URL were exported and set in Gitpod and all bash scripts were created and tested towards both databases depending on the first argumnet whether it is the local Postgres instances or the RDS one 

<img width="515" alt="image" src="https://user-images.githubusercontent.com/125532497/224531523-41b427c0-18cf-4641-a971-dc5ff1dc2bc4.png">

For the RDS and as instructed , the Security Group was updated so that it accepts connections on port 5432 from the Gitpod workspace IP , initially the SG inbound rule was updated manually so that it accepts traffic from any IP

<img width="963" alt="image" src="https://user-images.githubusercontent.com/125532497/224531603-5ef0915c-7fbf-42b1-8c78-3659f02f2304.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Database SQL operations towards Local and RDS Instances using Scripts  

Some formating was done as shown below for 

#### 1. DB Connection Script 

<img width="517" alt="image" src="https://user-images.githubusercontent.com/125532497/224532599-76c41c0e-654f-4425-9b02-1c1e2a0aeaf3.png">

#### 2. Loading Schema  

<img width="515" alt="image" src="https://user-images.githubusercontent.com/125532497/224533285-3ddeacfb-f66b-4086-84a8-71349bf06d26.png">

#### 3. Populating some records in the 2 tables 

<img width="516" alt="image" src="https://user-images.githubusercontent.com/125532497/224533307-2e45877a-3c8f-425a-bfe2-0479ac510eda.png">

#### 4. Retreiving the populated tables contents 

![image](https://user-images.githubusercontent.com/125532497/224533340-add2fef7-ab32-4b91-9168-e1643dab59e9.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### RDS SG Update Script  

DB_SG_ID and DB_SG_RULE_ID variables were set in Gitpod variables according to what is being configured in the EC2 SG of our RDS DB and yaml file is updated accordingly to run the SG setting script once workspace is restarted 

![image](https://user-images.githubusercontent.com/125532497/224538269-60cbc208-cf0a-450d-a0bb-121f29949a18.png)

<img width="959" alt="image" src="https://user-images.githubusercontent.com/125532497/224538366-5a8ddaf9-e76c-44a5-a79f-6268301de493.png">


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Allow the web application to connect to RDS / local Instance and retreive the seed activities 

Initially we started by the local instance where I followed the instructions and set the CONNECTION_URL parameter in the yaml compose file with 127.0.0.1 as the hostname , I tried to troubleshoot it before following your troubleshooting steps and on connecting to the backend container , executing the python commands , it was found that the connection URL doesn't make any sense as it is pointing towards localhost ( backend container ) which is obviously not containing apostgres instance 

![image](https://user-images.githubusercontent.com/125532497/225243007-3cd7dba4-6c8f-411f-b8f0-ab32259bf176.png)

Once manually setting the hostname to db which is similar to the Postgres container as per the compose yaml file , issue had been fixed  

![image](https://user-images.githubusercontent.com/125532497/225243097-8b89dbc7-6420-4175-9cfb-e2546de523a2.png)

![image](https://user-images.githubusercontent.com/125532497/225243461-441e058c-d8fb-4e67-b136-041c1368e004.png)

The retreival of the activity from backend was verified from the backend initially 

![image](https://user-images.githubusercontent.com/125532497/225256234-1537e653-ddab-4561-b829-bf19b416a7d1.png)

Then the connection URL was set towards the RDS instance and it was checked from the frontend URL

![image](https://user-images.githubusercontent.com/125532497/225256124-65f1540b-e83e-469c-8ebd-9b60c11edf34.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Post Confirmation Lambda Function 

I followed the instructions , created the Lambda function , updated the environmental parameters and added the Layer with a reference to my region  

<img width="948" alt="image" src="https://user-images.githubusercontent.com/125532497/225322898-7da5e937-6f83-41dd-bbe4-dd3121be92e4.png">

I kept getting the below error which complains about the psycopg2 module 

<img width="279" alt="image" src="https://user-images.githubusercontent.com/125532497/225327597-bd7a0b26-4de4-44c7-b8f9-2c1f944402f7.png">

I kept troubleshooting this for 2 days :( and issue got fixed once I complied the module compatible with Python3.9 locally and upload its zip file with the lambda_function  

<img width="215" alt="image" src="https://user-images.githubusercontent.com/125532497/226087376-6310f800-ec44-4109-a06d-38f2657be214.png">

I tried the below code instead and for which the function environmental parameter CONNECTION_URL was set

<img width="946" alt="image" src="https://user-images.githubusercontent.com/125532497/226087437-3caaf7c3-9ec2-47b5-a761-c2f1b8a00a75.png">

And finally after more than 20 trials , user was reflected in the production database 

<img width="493" alt="image" src="https://user-images.githubusercontent.com/125532497/226087471-6634096a-98f3-4b2c-ac45-ffd2b7a02cf5.png">

For that I used a temp email site to avoid loading my personal email with verification mails/codes

<img width="758" alt="image" src="https://user-images.githubusercontent.com/125532497/226087590-6369c45a-ba1c-4510-a31a-e8fd3ea97519.png">


Also I kept using the below AWS command to delete the user from Cognito User pool to avoid switching between tabs and giving some confirmations 

```
aws cognito-idp admin-delete-user --user-pool-id us-west-2_UaMtMOXPr --username f0b93df9-bd94-4eef-870c-bc4fc8f76aed
```

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Cruddluring 

Finally after fixing the Lambda function issue , I logged in and followed the backend instructions to update the code so that activities are inserted into the database and retrived on the home
![image](https://user-images.githubusercontent.com/125532497/225997973-b72fe765-cadb-45eb-bdca-20c9a34c2bed.png)

![image](https://user-images.githubusercontent.com/125532497/225998180-f581617a-e1ce-4a35-a8c2-94afdd9e0937.png)

The same was followed and worked fine however the correct user uuid was not reflected successfully , it was shown as "Andrw Brown" only although my user was logged in which I decided to fix in coming weeks

![image](https://user-images.githubusercontent.com/125532497/226087866-e09b625e-b297-4746-adcf-79820ef5620d.png)


