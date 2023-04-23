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

