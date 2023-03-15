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


**Add The new parts here

![image](https://user-images.githubusercontent.com/125532497/225243007-3cd7dba4-6c8f-411f-b8f0-ab32259bf176.png)

![image](https://user-images.githubusercontent.com/125532497/225243097-8b89dbc7-6420-4175-9cfb-e2546de523a2.png)

![image](https://user-images.githubusercontent.com/125532497/225243461-441e058c-d8fb-4e67-b136-041c1368e004.png)

![image](https://user-images.githubusercontent.com/125532497/225256124-65f1540b-e83e-469c-8ebd-9b60c11edf34.png)

![image](https://user-images.githubusercontent.com/125532497/225256234-1537e653-ddab-4561-b829-bf19b416a7d1.png)





