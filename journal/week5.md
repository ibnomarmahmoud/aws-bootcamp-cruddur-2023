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



