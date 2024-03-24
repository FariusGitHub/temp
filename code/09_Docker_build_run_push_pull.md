# DOCKER BUILD, RUN, PUSH and PULL

Here, we will deploy Dockerfile into DockerHub by pushing it and pulling it back and try to run the container. 

Now we have the Dockerfile built previously with full understanding of how the robotic movement [works](https://github.com/FariusGitHub/temp/blob/main/code/08_Docker_Dockerfile_Design.md).
```txt
$ ls
  Dockerfile
```
Next, we will build the image locally named ev3.

```txt
$ docker build -t ev3 .
  [+] Building 3.3s (7/7) FINISHED                                                                                                                                                              docker:desktop-linux
   => [internal] load build definition from Dockerfile                                                                                                                                                          0.2s
   => => transferring dockerfile: 1.17kB                                                                                                                                                                        0.0s
   => [internal] load metadata for docker.io/library/ubuntu:latest                                                                                                                                              1.4s
   => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                                                                                 0.0s
   => [internal] load .dockerignore                                                                                                                                                                             0.3s
   => => transferring context: 2B                                                                                                                                                                               0.0s
   => [1/2] FROM docker.io/library/ubuntu:latest@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e                                                                                        0.0s
   => CACHED [2/2] RUN apt-get update &&     apt-get install -y openssh-client sshpass                                                                                                                          0.0s
   => exporting to image                                                                                                                                                                                        0.2s
   => => exporting layers                                                                                                                                                                                       0.0s
   => => writing image sha256:4f4e8c1388a77f97a51fc11ba5b9de961f255be2b1998254aa71901a6ece60a3                                                                                                                  0.1s
   => => naming to docker.io/library/ev3                                                                                                                                                                        0.1s
  
  View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/jw381vjvzgvuje24le2z311fp
  
  What's Next?
    View a summary of image vulnerabilities and recommendations → docker scout quickview
```
As the build successful, we can review the image as follow
```txt
$ docker images
  REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
  ev3          latest    4f4e8c1388a7   4 hours ago   135MB
```
And so far, there is no container run yet.
```txt
$ docker ps -a
  CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
Then, we will run the container. The container would control EV3 for the 10 steps to complete the 10 curves.
```txt
$ docker run ev3
  Warning: Permanently added '10.42.0.3' (ED25519) to the list of known hosts.
```
![](https://github.com/FariusGitHub/temp/blob/main/image/image11.gif) </br>


Next, we will push the image into Docker Hub by tagging and pushing it as follow.
```txt
$ docker tag ev3 ftjioesman/ev3
$ docker push ftjioesman/ev3
  Using default tag: latest
  The push refers to repository [docker.io/ftjioesman/ev3]
  de99cbdf373a: Pushed 
  5498e8c22f69: Mounted from library/ubuntu 
  latest: digest: sha256:dbc7a043187bb25a74d75b43c4b46d7a29ad1336839ad671eafa652d7fed1dd9 size: 741
```
I cleaned all of my local containers and images and let's see what we have after pulling it back.
```txt
$ docker images
  REPOSITORY       TAG       IMAGE ID       CREATED       SIZE
  ftjioesman/ev3   latest    4f4e8c1388a7   4 hours ago   135MB
```
And certainly the same functionality will appear as I run the container I made/debug earlier.

```txt
$ docker run ftjioesman/ev3
  Warning: Permanently added '10.42.0.3' (ED25519) to the list of known hosts.
```
