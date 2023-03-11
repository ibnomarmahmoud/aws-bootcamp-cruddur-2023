# Week 3 — Decentralized Authentication
## Homework Submission 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Cognito User Pool Creation 
The User pool was created from AWS console as per the Live stream instructions and the user pool ID , Client ID under App integartion were updated in the application code so that the authetication is done via AWS Cognito 

<img width="914" alt="cognito1" src="https://user-images.githubusercontent.com/125532497/224495961-7cc58c0e-5ff3-49bc-b726-ea3ccffee4d4.png">

<img width="287" alt="Cruddle" src="https://user-images.githubusercontent.com/125532497/224495979-e5908c6a-ec35-4e5e-8d80-f631114672fd.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Implement custom Signup / Confirmation / Recovery Pages   
Multiple Users were created via the new custom signup page and confirmed their emails 

<img width="580" alt="List of Users" src="https://user-images.githubusercontent.com/125532497/224496023-3998208e-9428-4f17-be50-7268176c93b8.png">

The same was checked/verified  via AWS CloudTrail as witnessed afterwards from Ashish's video 

![cognito](https://user-images.githubusercontent.com/125532497/224496128-136393c4-8e8b-47b2-80e9-1377e75b2aa4.png)

Upon Signing-out , one user requested recovering the password and the verification Code was sent correctly

<img width="828" alt="image" src="https://user-images.githubusercontent.com/125532497/224496317-5d8d1be1-dcc0-49f1-808e-5b9b2447d4ef.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

### JWT Different approaches  

The related video was watched but it was not properly digested so I prefered to read more about such topic from external resources and enhance my coding experience specially for Flask and re-do the backend implementation for Cognito part once more instead of copying the backend modified .py files specially this is not dependant on the next steps

## Homework Challenges  

I have attempted the challenge of creating a new User Pool with MFA as SMS message 

<img width="483" alt="image" src="https://user-images.githubusercontent.com/125532497/224496963-9813b94b-1cc1-4ec7-b4df-5d1916211639.png">

Its spending consideration was checked and the SMS containing the OTP for Egypt various operators will be costing the below fees 

<img width="689" alt="image" src="https://user-images.githubusercontent.com/125532497/224497074-bdee2ec7-2b94-4eb2-9cee-64cbfed6a547.png">

This was not applied in the Frontend end code to avoid actual money spending 


