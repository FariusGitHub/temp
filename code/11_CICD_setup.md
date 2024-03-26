# CREATE, LAUNCH AND CONFIGURE JENKINS
Many of the process here was inspired by my previous blog on https://github.com/FariusGitHub/Example_Webpage </br>
It was a heavy approach with a web app and docker-in-docker application where we will not use them all in this case.

Assuming docker already installed, herewith some common procedure and expected output.
```txt
$ docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home://var/jenkins_home jenkins/jenkins:lts
  Unable to find image 'jenkins/jenkins:lts' locally
  lts: Pulling from jenkins/jenkins
  71215d55680c: Pull complete 
  35af8fb55c2f: Pull complete 
  c8dac3aae91a: Pull complete 
  1830bd5f9b45: Pull complete 
  234e1154c2a1: Pull complete 
  8d7cd7345072: Pull complete 
  a89f7edcbd51: Pull complete 
  83597e279c9f: Pull complete 
  6c39e3e60898: Pull complete 
  29150353c9ba: Pull complete 
  33fe415a6139: Pull complete 
  c5d8e31128fd: Pull complete 
  Digest: sha256:1fd79ceb68ce883fb86db70bdbf7f9eaa8b25e580aafe7a240235240396e3916
  Status: Downloaded newer image for jenkins/jenkins:lts
  eb06c35364614e7e9bbe661a15df869f0ff5307f0a3e872e73f3232a7971a3dd

$ docker ps -a
CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS         PORTS                                              NAMES
  54ed18a5d8a1   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->8080/tcp, 0.0.0.0:50000->50000/tcp   angry_goldwasser

$ docker exec -u 0 -it 54ed18a5d8a1 /bin/bash
jenkins@ceb8ac595bdf:/$ cat /var/jenkins_home/secrets/initialAdminPassword
  d96fXXXXXXXXXXXXXXXXXXXXXXXXXb5c
```

Remember that /var/jenkins_home/secrets/initialAdminPassword is only accessible inside the docker container. </br>
When we go to localhost:8080, we shall enter above password as an admin user. And I will leave the same going forward.

![](https://github.com/FariusGitHub/temp/blob/main/image/image18.png)

Remember to go inside the container as root (-u 0) so you can install update and run as sudo easily. </br>
Since we setup above jenkins inside Docker container, we may install a lightweight docker inside docker. </br>
We would notice that the same goovy command below will make a different.
```txt
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh"""
                
                docker login --username ftjioesman --password XXXXXXX
                
                """
            }
        }
    }
}
```
Before we install docker inside a docker would see this
![](https://github.com/FariusGitHub/temp/blob/main/image/image19.png)
After we install docker insider container 54ed18a5d8a1 as follow, we would see below
```txt
apt-get update
apt-get install -y docker.io
```
![](https://github.com/FariusGitHub/temp/blob/main/image/image20.png)

