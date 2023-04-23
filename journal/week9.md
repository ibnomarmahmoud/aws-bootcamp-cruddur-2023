# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Configure CodeBuild 

The instructions had been followed and Codebuild configuration was done successfully , initially it was failing even after Beko's fixes and appearently Codebuild couldn't push to ECR with the below error 

```
d945d3acfd66: Retrying in 3 seconds
7f2fe4cb548a: Retrying in 3 seconds
588a8fad6792: Retrying in 2 seconds
ebfe17d7a4e5: Retrying in 2 seconds
19253075bcec: Retrying in 2 seconds
d945d3acfd66: Retrying in 2 seconds
7f2fe4cb548a: Retrying in 2 seconds
588a8fad6792: Retrying in 1 second
19253075bcec: Retrying in 1 second
ebfe17d7a4e5: Retrying in 1 second
d945d3acfd66: Retrying in 1 second
7f2fe4cb548a: Retrying in 1 second
EOF

[Container] 2023/04/23 11:43:53 Command did not exit successfully docker push $IMAGE_URL/$REPO_NAME exit status 1
[Container] 2023/04/23 11:43:53 Phase complete: POST_BUILD State: FAILED
[Container] 2023/04/23 11:43:53 Phase context status code: COMMAND_EXECUTION_ERROR Message: Error while executing command: docker push $IMAGE_URL/$REPO_NAME. Reason: exit status 1
[Container] 2023/04/23 11:43:53 Phase complete: UPLOAD_ARTIFACTS State: SUCCEEDED
[Container] 2023/04/23 11:43:53 Phase context status code:  Message: 
```
So I had to add the below policy to CodeBuild role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ecr:CompleteLayerUpload",
                "ecr:GetAuthorizationToken",
                "ecr:UploadLayerPart",
                "ecr:InitiateLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage"
            ],
            "Resource": "*"
        }
    ]
}
```

It is shown below that the built had been done successfully 

<img width="960" alt="image" src="https://user-images.githubusercontent.com/125532497/233839468-90f9f4ee-65f4-40b9-a787-67b9ab48a181.png">

**ECR Image uploaded**

<img width="960" alt="image" src="https://user-images.githubusercontent.com/125532497/233839545-4ca2e1aa-8888-4b89-83dc-20ce9f0aea0e.png">

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Configure CodePipeLine

Once the Codebuild issue had been fixed , I resumed the pipeline and its 3 stages had been completed post changing the input artifacts into image definition 

![image](https://user-images.githubusercontent.com/125532497/233841364-4b7f05a8-2e5a-4922-b751-8b94b28c0199.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Status of Pending Tasks / Snaglist 

- [X] Still have an issue with JWT 
- [X] Still geting CORS error in frontend and for which all frontend screenshots are not showing any content 
- [ ] Verify the Messaging and DynamoDB  post fixing the CORS issue
- [X] Check if AWSCLI and PoSTgres are working after re-launching the workspace 

### New Extras

- [ ] Build a separate pipeline for the Frontend deployment
- [ ] Update the Lucid Chat with CloudFront/ Pipeline
- [] Attend a crash course for Yaml to be prepared for the coming 2 weeks in CFN


