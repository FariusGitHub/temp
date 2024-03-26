# Console Output
Started by user admin
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/capstone
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Review)
[Pipeline] sh
+ rm -f Dockerfile
+ wget https://raw.githubusercontent.com/FariusGitHub/produce/main/Dockerfile
--2024-03-26 18:47:12--  https://raw.githubusercontent.com/FariusGitHub/produce/main/Dockerfile
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... ::ffff:185.199.111.133, ::ffff:185.199.110.133, ::ffff:185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|::ffff:185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 659 [text/plain]
Saving to: ‘Dockerfile’

     0K                                                       100% 14.6M=0s

2024-03-26 18:47:12 (14.6 MB/s) - ‘Dockerfile’ saved [659/659]

+ cat Dockerfile
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-client sshpass

CMD ["sshpass", "-p", "maker", "ssh", "-o", "StrictHostKeyChecking=no", "robot@10.42.0.3", \
     "brickrun", "-r", "--directory=/home/robot/curve1", "/home/robot/curve1/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve2", "/home/robot/curve2/main.py", "&&", \ 
     "brickrun", "-r", "--directory=/home/robot/curve3", "/home/robot/curve3/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve4", "/home/robot/curve4/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve5", "/home/robot/curve5/main.py" \
    ]
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] sh
+ docker build -t ftjioesman/capstone .
#1 [internal] load build definition from Dockerfile
#1 sha256:903df9aebd7a8daccfb5a2c06148a59d0365c0f8b93a1fe53ad1fcf03f0321f5
#1 transferring dockerfile: 704B 0.0s done
#1 DONE 0.3s

#3 [auth] library/ubuntu:pull token for registry-1.docker.io
#3 sha256:4ccafade920e2ff0707dd4b38e9e042b52a66313650cea10208d82d8a7f7d030
#3 DONE 0.0s

#2 [internal] load metadata for docker.io/library/ubuntu:latest
#2 sha256:8c6bdfb121a69744f11ffa1fedfc68ec20085c2dcce567aac97a3ff72e53502d
#2 DONE 0.9s

#4 [internal] load .dockerignore
#4 sha256:ac8ffb5677e00464b2b6970cda5ecc36f45808326fa4445b2d733b8d237a697b
#4 transferring context:
#4 transferring context: 2B done
#4 DONE 0.2s

#6 [1/2] FROM docker.io/library/ubuntu:latest@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e
#6 sha256:71ac576a42638db4e08d37e9cb59d344c26d3d83bfc623ba1a402e00b58a7bc3
#6 DONE 0.0s

#5 [2/2] RUN apt-get update &&     apt-get install -y openssh-client sshpass
#5 sha256:3224eeb8e382fcfe6df79a79304cc396a6ac0d0e35145ce17a21bd32c82002f4
#5 CACHED

#7 exporting to image
#7 sha256:b663965eff083ef778e2391026b0f503f922737f02f63478ba1b23cc5d8d042b
#7 exporting layers done
#7 writing image sha256:28b4b68f04fa16ad5bd8574f0a15be61c08b7b7397dbd859e396aa5b456f9657 0.1s done
#7 naming to docker.io/ftjioesman/capstone:latest
#7 naming to docker.io/ftjioesman/capstone:latest 0.1s done
#7 DONE 0.2s
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Push)
[Pipeline] sh
+ docker login --username XXX --password XXX
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /var/jenkins_home/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
+ docker tag ftjioesman/capstone ftjioesman/capstone:latest
+ docker push ftjioesman/capstone:latest
The push refers to repository [docker.io/ftjioesman/capstone]
de99cbdf373a: Preparing
5498e8c22f69: Preparing
de99cbdf373a: Layer already exists
5498e8c22f69: Layer already exists
latest: digest: sha256:f0576bb2ee7f2b9c2e1f4fdd3c9bc7b5a6cae3c54a2ecbde51428ddcabf2dd1e size: 741
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Pull)
[Pipeline] sh
+ docker pull ftjioesman/capstone
Using default tag: latest
latest: Pulling from ftjioesman/capstone
Digest: sha256:f0576bb2ee7f2b9c2e1f4fdd3c9bc7b5a6cae3c54a2ecbde51428ddcabf2dd1e
Status: Image is up to date for ftjioesman/capstone:latest
docker.io/ftjioesman/capstone:latest
+ docker run ftjioesman/capstone
Warning: Permanently added '10.42.0.3' (ED25519) to the list of known hosts.
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
