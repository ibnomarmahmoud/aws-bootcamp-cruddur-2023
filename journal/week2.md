# Week 2 — Distributed Tracing

## Homework Submission 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### HoneyComb

HoneyComb Account was set in Week0 , I just copied its API Key and set it in Gitpod variables , updated the compose file as per the Live stream instructions and data were sent successfully to my project

Initially nothing was sent to the project and after connecting to the shell of container of the backend , enviornmnetal vraiables were found to be not set as per the configuration in the compose file

![Missing Variables](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Missing_Env_variables.JPG)

But later post restarting my Gitpod workspace and composing up the frontend and backend images , issue got resolved 

I added multiple spans for home activities endpoint , another for Notifications endpoint and added some attributes as indicated in each endpoint .py files , also I tried adding another inner span for home activities endpoint accordingly we can see 3 spans as shown in the below snapshot

![Custom Span](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CustomSpan.png)

Finally I ran 2 queries to get the count and average duration of requests per endpoint variable and added them to the Board 


![Query1](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Query1.png)

![Query2](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Query2.png)

![Board](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Board.png)

