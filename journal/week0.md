# Week 0 — Billing and Architecture

## Homework Submission 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Create an Admin User 

After creating a new AWS Account -since my 2 accounts are older than 1 years accordingly I won't be able to make use of the Free Tier benefits- , uisng the root user a new admin group was created to which mahmoudOmar user was added and using the below link access to billing was granted to such user 
```
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_billing.html?icmpid=docs_iam_console#tutorial-billing-step2
```
![Admin User](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/ADMIN_USER_WITH_ACCESS_TO_BILLING.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Use CloudShell  

Cloud Shell was loaded and few AWS commands were tested a shown below

![AWS CLOUDSHELL](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/AWS_CLOUD.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Generate AWS Credentials

From IAM , Secret keys for accessing the CLI using the Admin user were generated , its CSV was downloaded , they were loaded in GitPod using pd command as shown below 
![Admin Access Keys](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/ADMIN_SECRET_KEYS.png)
![GITPOD Variables for Keys](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/AWS_CLI_VARIABLES_SETTINGS_IN_GITPOD.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Installed AWS CLI

AWS CLI V2 were installed manually as per the commands in the below manual on GitPod using Visual Studio Code then gitpod.yaml was updated to include this task as updated in the repo

```
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```
AWS CLI v2 was installed earlier on my windows laptop and it was reconfigured towards my new account as shown in the below PowerShell CLI to upload files to S3 bucket if needed in the future 

![Powershell](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/POWER_SHELL.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
###  Create a Budget and Billing Alarm

I have added 25$ Credit acquired from attending an AWSomeDay earlier accordingly I created a budget to track my spendings with a budget of 25 USD per monty and two alerts towards my personal email one at 50% and another at 80% , Another budget would be added in a later stage to track specfic service usage 

![Monthly spending](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Budget_Again.JPG)
![Billing including Credits](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Billing_Credits.png)
![Alert1](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Billing_Alert1.png)
![Alert2](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Billing_Alert2.png)

**Free Tier Usage** : By default, AWS Budgets automatically notifies you over email when you exceed 85 percent of the Free Tier limit for each service
 


