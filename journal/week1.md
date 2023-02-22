# Week 1 — App Containerization

## Homework Submission 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Preparations 

#### Docker Knowledge refresh 

Before re-watching the Live stream recording , I have attended Adrian's free Docker fundamental training to refresh my Docker knowledge

![Adrian Course](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Docker%20Course.JPG)

#### Gitpod Codespace settings

I have Creating an SSH key for VS Code to connect to Codespace and granted permissons so that commits can be uploaded to Github repo 

![Grant Permissions](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Grant%20Permission.png)
![SSH Keys](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/SSH_key_Generation.JPG)

#### Verify the spending Limits

I have verified the current spendings on Gitpod Free-Tier before working on Week1

![Spending Limits](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Gitpod%20Free%20Tier%20Usage%20Check.JPG)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Starting the various containers 

After following the instructions in the Live Stream and updating the compose yaml file , I managed to have the containers started 

![Running Containers](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Containers_running_Up.png)

As per Ashish's Security video , Snyk integration was done to see the vulenrabilities in the container related Dockerfiles

![Snyk](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Snyk.png)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Interacting with PostgreSQL and DynamoDB containers 

Once containers were started post composing the yaml file , I tried to connect to psql and DynamoDB as shwon below 

#### DynamoDB
![DynamoDB](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/DynamoDB.JPG)

#### PostgreSQL
![PSQL1](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Postgres1.JPG)
![PSQL2](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Postgres2.JPG)


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Update the Frontend and backend to add the notifications 

The instructions were followed and Notifications endpoint was added as shown below 

![Backend Notifictaions](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Backend%20Notification.png)
![Frontend Notifictaions](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Frontend%20Notification.png)


## Homework Challenges
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
### Run Docker on EC2 Instance 

I have followed the below [link](https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/) to install Docker on Amazon Linux 2 EC2 instance and pulled couple of images and started Fedora container 

![Docker on EC2 Instance](https://github.com/ibnomarmahmoud/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Run_Docker_EC2.png)

### Build a new image via Dockerfile to run "Hello World" python Script 

I made a new Dockerfile on the EC2 intance as follows

```
FROM python:3.8-buster
RUN pip install --upgrade pip
COPY src/ .
CMD [ "python", "trtest.py"]
```
And Inside src directory , I made trtest.py with the following content 

```
print ("Hello World")
```
I built the docker image as follows 

```
docker build -t aws_bootcamp_2023 .
```

I ran the docker container 

```
[ec2-user@ip-172-31-51-160 DOCKER]$ docker images
REPOSITORY          TAG          IMAGE ID       CREATED          SIZE
aws_bootcamp_2023   latest       4ddd0f9d43f2   24 seconds ago   896MB
aws_bootcamp        latest       d0d2193ee828   7 minutes ago    2.22GB
python              3.8-buster   d98cbcebcd8b   11 days ago      880MB
fedora              latest       e0d7a1685fed   13 days ago      184MB
hello-world         latest       feb5d9fea6a5   17 months ago    13.3kB
[ec2-user@ip-172-31-51-160 DOCKER]$ docker run 4ddd0f9d43f2
Hello World

```

Since AWS will charge me for the outbound traffic to push the +800M image on Docker hub , I decided to push the hello-world image instead for which the Docker hub token was activated 

```
[ec2-user@ip-172-31-51-160 DOCKER]$ docker image tag hello-world omaraldeeb/hello-world:latest
[ec2-user@ip-172-31-51-160 DOCKER]$ docker login -u omaraldeeb
Password:
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-51-160 DOCKER]$ docker image push omaraldeeb/hello-world:latest
The push refers to repository [docker.io/omaraldeeb/hello-world]
e07ee1baac5f: Mounted from library/hello-world
latest: digest: sha256:f54a58bc1aac5ea1a25d796ae155dc228b3f0e11d046ae276b39c4bf2f13d8c4 size: 525
```

