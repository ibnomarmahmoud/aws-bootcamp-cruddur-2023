# Week 5 — DynamoDB and Serverless Caching

## Homwork Submission 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Local DynamoDB Instance and implementing utility scripts

Local DynamoDB container was already started since Week1 and containing a table called "Music"

<img width="960" alt="image" src="https://user-images.githubusercontent.com/125532497/227595918-0c863283-e110-4aa3-93a5-a770ae5e6fe9.png">

![image](https://user-images.githubusercontent.com/125532497/227643459-9f97dd8d-3014-4409-97fa-416a809ecb29.png)

DynamoDb Utility Scrips were implemented as per the instructions 
where table was created as per the bash script , Music old table was dropped and seed data was added 


![image](https://user-images.githubusercontent.com/125532497/227596144-c7ee9db9-8859-4852-ad7a-2360be70924f.png)

![image](https://user-images.githubusercontent.com/125532497/227597118-c46166f0-c1a8-4682-9105-e0d99262e7a5.png)

List and Get Conversation scripts were added , RDS scripts were moved under db folder for the retreival of uuid called in list conversation script  

![image](https://user-images.githubusercontent.com/125532497/227642637-fc97e898-6465-4b11-bdfd-8f3014ec4199.png)
![image](https://user-images.githubusercontent.com/125532497/227642821-a8c8d41e-ea31-473b-8b9a-e97bfc9ae271.png)

Codewishper was attempted to see its capabilities and whether it can replace ChatGPT or not ;) 

![image](https://user-images.githubusercontent.com/125532497/227640077-7485df09-0884-40ff-bd41-bea4de3b6746.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implement Update Cognito ID Script for Postgres Database

Update Cognito User ID script as implemented successfully but I had to modify some scripts related to RDS previous week as I had to modify the path after collecting them all under db folder , also I had modified the seed data to the users already existing in my Cognito User Pool so instead of Andrew / Beko , I have inserted Mahmoud / Hema as shown below from the update cognito User ID Output 

**Before**

<img width="539" alt="image" src="https://user-images.githubusercontent.com/125532497/227703526-6d67376f-a79c-4235-95a6-28f2a3a072a9.png">


**AFter**

![image](https://user-images.githubusercontent.com/125532497/227703577-5143bf81-5352-4495-9b74-262c46cc5512.png)

![image](https://user-images.githubusercontent.com/125532497/227703592-f73563ed-1561-4439-882b-32151b6064e5.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implement various patterns for Listing/Creating Messages into Application

The modifications in the backend and frontend were performed as instructed , backend was found to be trying to connect to production RDS so modified the docker compose file and started it again 

No further errors were reported in the logs of backend however no message groups were reflected on the frontend 

![image](https://user-images.githubusercontent.com/125532497/227707121-8057d2f1-d270-4c6d-83b9-a5394a88a664.png)

![image](https://user-images.githubusercontent.com/125532497/227707133-e141577c-0705-4fc3-8585-6ae685767ce9.png)

So I believe that is related to the ddb seed part where the message should have my user instead of Andrew while messages.py is trying to fetch the ser id from the below

```
sql = db.template('users','uuid_from_cognito_user_id')
    my_user_uuid = db.query_value(sql,{
      'cognito_user_id': cognito_user_id
    })
```

So I updated the conversation to be between Mahmoud and Hema

![image](https://user-images.githubusercontent.com/125532497/227707561-6ee85ebc-37a3-47ec-b099-6d708644943d.png)

Still nothing was refleted on the backend and "Failed to Fetch MessageroupsPage.js" was reported 

So tried to access the backend "api/message_groups" directly and TypeError: MessageGroups.run() got an unexpected keyword argument 'user_handle' appeared

![image](https://user-images.githubusercontent.com/125532497/227719052-06d90be0-a6f6-4c1a-b739-2ff53f73bc62.png)

Further troubleshooting led to db.py was not udpated correctly and finally "api/message_groups" reflected correct data 

![image](https://user-images.githubusercontent.com/125532497/227722299-eac69311-3e9f-432d-95b4-a679ff0cdf36.png)

![image](https://user-images.githubusercontent.com/125532497/227723694-bfdc562a-ff28-4a74-ae0d-7ba87f23f942.png)
I can't have the data reflected on the fronetend URL post addng checkAuth function which needs to be checked furthr but I am running out of time !!

```
Access to fetch at 'https://4567-ibnomarmahm-awsbootcamp-uxcy2mjo4rb.ws-eu92.gitpod.io/api/message_groups' from origin 'https://3000-ibnomarmahm-awsbootcamp-uxcy2mjo4rb.ws-eu92.gitpod.io' has been blocked by CORS policy: Request header field authorization is not allowed by Access-Control-Allow-Headers in preflight response.
```

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### DynamoDB Streams
Production Table as created with enable streams on the table with 'new image' attributes included

![image](https://user-images.githubusercontent.com/125532497/227724554-137ef8c7-4a72-4afd-aa9f-2a69762341c8.png)
![image](https://user-images.githubusercontent.com/125532497/227724604-14b79c10-3bba-46bf-a686-86a0eaf33760.png)


![image](https://user-images.githubusercontent.com/125532497/227724678-856bd0ad-b461-4398-bdee-4c4bf00db8a0.png)


VPC Endpoint as created so that we have the DynamoDB accessible from other services 

![image](https://user-images.githubusercontent.com/125532497/227724968-f66ffb81-aa8b-4b36-8655-fdeec511e4c6.png)


Finally Lambda Function was created

![image](https://user-images.githubusercontent.com/125532497/227725289-0f3234ab-ad0f-447b-9dd7-7c223223238b.png)

I would test it once I fix the CORS error related to the frontend 


