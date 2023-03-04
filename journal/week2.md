# Week 2 — Distributed Tracing

## Homework Submission 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### HoneyComb

HoneyComb Account was set in Week0 , I just copied its API Key and set it in Gitpod variables , updated the compose file as per the Live stream instructions and data was sent successfully to my project

Initially nothing was sent to the project and after connecting to the shell of container of the backend , environmental variables were found to be not set as per the configuration in the compose file

![Missing Variables](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Missing_Env_variables.JPG)

But later post restarting my Gitpod workspace and composing up the frontend and backend images , issue got resolved 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### HoneyComb Challenge
I added multiple spans for home activities endpoint , another for Notifications endpoint , also I tried adding another inner span for home activities endpoint accordingly we can see 3 spans as shown in the below snapshot

![Custom Span](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CustomSpan.png)

I added some attributes as indicated in each endpoint .py files , one of them is app.endpoint which represents the endpoint whether it is "Notifications" Or " Home-Activities"

Finally I ran 2 queries to get the count and average duration of requests per endpoint variable and added them to the Board , I used the Where clause to filter only the requests where  app.endpoint exists


![Query1](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Query1.png)

![Query2](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Query2.png)

![Board](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Board.png)

One final query was made to get the distribution of the Source IP , whether it was triggered from the backend directly or via the frontend 

<img width="714" alt="image" src="https://user-images.githubusercontent.com/125532497/222753773-8b7e7751-cab8-4679-848a-488717ca5de6.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### CloudWatch Log

The video instructions were followed and a logger info was added in home activities endpoint, the log stream was created and called "cruddle" similar to what is configured in app.py , I fired multiple requests and info log message was displayed in backend container but it was never reflected in Cloudwatch logs till I found that the default region set in Gitpod is not the one selected , once chnaged to us-west-2 , logs were found 

<img width="813" alt="image" src="https://user-images.githubusercontent.com/125532497/222781184-3664320f-5025-464d-8a4f-4e71e40676b6.png">

<img width="814" alt="image" src="https://user-images.githubusercontent.com/125532497/222781565-b9d56723-9f7f-48f8-a068-e5a37d18b550.png">

### X-Ray

The video instructions were followed and the X-ray daemon container was started and sent the events to the X-ray in us-west-2 region as shown below

<img width="707" alt="image" src="https://user-images.githubusercontent.com/125532497/222801207-43c70e8c-7a97-48eb-b322-9aeea06bab03.png">

<img width="912" alt="image" src="https://user-images.githubusercontent.com/125532497/222800870-bf17243d-c05a-42be-9f18-9044168bb8bc.png">

Still I need to add segments and sub-segments but I found the honeycomb more easy to use

### Rollbar

The video instructions were followed and Token key was set in Gitpod variables , updated the compose file and data was sent to the created project , same problem of having variables not reflected in the containers was faced like honeycomb 

Items were checked under Cruddle project 

![image](https://user-images.githubusercontent.com/125532497/222881498-f3589d91-6c5a-4b55-a9a8-620f9d770403.png)





