# DevOps | Produce
https://github.com/FariusGitHub/temp
![](https://github.com/FariusGitHub/temp/blob/main/image/image25.png)</br>
I would like to introduce an application of Raspberry Pi instances to move a robotic arm in order to slice a variety of produce using the fundamentals of DevOps.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image26.png)</br>
The majority of this blog will cover Infrastructure as Code, Container Technologies, and Continuous Delivery.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image27.png)</br>
In short, DevOps involves applying principles and practices such as using [Linux OS](https://github.com/FariusGitHub/temp/blob/main/code/01_DevOps_Fundamentals_Linux_OS.md), [Git](https://github.com/FariusGitHub/temp/blob/main/code/02_DevOps_Fundamentals_Git_GitHub.md), and Architectural Diagrams. </br>
For this capstone project, we will be using a simple application involving Raspberry Pi and Lego EV3 robotics to automate the slicing of produce while implementing DevOps practices.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image28.png)</br>
Unlike on-premises computers, cloud computing platforms like [AWS EC2](https://github.com/FariusGitHub/temp/blob/main/code/03_Terraform_VPC_EC2.md#example-of-ec2-with-ansible) and [Azure Virtual Machine](https://github.com/FariusGitHub/temp/blob/main/code/03_Terraform_VPC_EC2.md#example-of-azure-vm-setup-with-terraform) require more resources to set up beforehand. <br>
I have been exploring [bash](https://medium.com/p/23f568a31353/edit), Terraform, Ansible, and [Chef](https://github.com/FariusGitHub/chef-ec2) to automate the deployment of EC2 and Azure Virtual Machine instances. </br>
In this project, we will create an instance that will store a master plan to move the robotic arm to slice peach fruit at the master node.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image29.png)</br>
The next thing we can automate in terms of [infrastructure](https://github.com/FariusGitHub/temp/blob/main/code/06_Terraform_Jenkins.md) is [Jenkins](https://github.com/FariusGitHub/temp/blob/main/code/11a_CICD_jenkins_console_output.md) Continuous Integration and Continuous Deployment, also known as Continuous Delivery. </br>
While it is easier to set up CI/CD with a web UI, there is a Java tool called jenkins-cli.jar that can automate this process. </br>
This Java program reads a [config.xml](https://raw.githubusercontent.com/FariusGitHub/temp/main/image/image22.png) file that mimics all the setup options available through the web browser for setting up the pipeline.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image30.png)</br>
The next crucial aspect of this project is the powerful database. I chose mySQL for prototyping purposes only. </br>
In the real world, the database needs to be fast when reading and writing a large amount of live data, especially when advanced 3D scanning is involved. </br>
For this capstone project, we will focus only on the 3D movement of the robotic arm without worrying about reverse engineering from machine learning and image processing of irregular produce shapes. </br>
The main focus of this project is on storing numerous coordinates that will instruct the Raspberry Pi and Robotic Arm where and when to move. </br>
This data could be extensive considering the 3D coordinates and intensity of pressure required for slicing. </br>
Installing and running mySQL only requires a few lines of commands, along with testing the connection. </br>
The main work in the database attached to the master node will involve schema design, data mapping, and ETL using query language and entity relationship diagrams.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image31.png)</br>
The next automation we could implement in terms of infrastructure as code is related to the robotic arm system. </br>
The [EV3 brick](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/), which connects the Raspberry Pi to the motor movement, runs on a lightweight version of Linux. </br>
By SSHing instructions and uploading new Python files to the EV3's SD card, we can convert the code into actual movement. </br>
In 2020, some official websites provided image files for this purpose. </br>
An example shown in the slide demonstrates sending interactive commands to the EV3 brick to run a motor on port B at an intensity of 1000 for 100 milliseconds.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image32.png)</br>
Lastly, in terms of infrastructure as code, we can also apply the same principles to the [observability](https://github.com/FariusGitHub/temp/blob/main/code/07_Terraform_Grafana.md) aspect, which is mainly managed by Prometheus and Grafana when Docker and Kubernetes are utilized. </br>
Typically, we use Helm as a package manager to deploy Prometheus and Grafana for monitoring purposes.</br>
We will dive deeper into observability towards the end of this blog.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image33.png)</br>
The next section of this blog will cover the heart of the DevOps principles itself, Container Technology. </br>
In short, many will think DevOps is identical to Docker and Kubernetes as container and container orchestration. </br>
However, there are also a few choices from simple Docker swarm to large-scale Kubernetes clusters offered by major cloud players like AWS EKS, Google Kubernetes Engine, or Azure Kubernetes Service. </br>
As you can see in the chart, it reflects more on the business objectives and values rather than going deeper into technicality. </br>
A DevOps expert could be expected to know many things but should not be an expert in everything. </br>
There are emerging languages like [Golang](https://github.com/FariusGitHub/crd) and [Ruby](https://medium.com/p/14ffb11cd6cd/edit), or some cloud features from [AWS SNS](https://medium.com/p/9538f74936d9/edit) when we apply microservices, lambda, and step functions. </br> 
There are also load balancing and [autoscaling](https://medium.com/p/c340ddde64de/edit), and horizontal pod autoscaling which every DevOps engineer should become familiar with. </br> 
How do all of this apply to slicing a tiny peach? </br>
Well, the fun part is the materials for this experiment are abundant and relatively cheaper compared to those woods and metals every carpenter or machinist learns to do their job. </br>
Kaizen is famously known as [continuous improvement](https://en.wikipedia.org/wiki/DevOps), and in DevOps, it is all about it.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image34.png)</br>
Why did I choose a Lego toy for this project and how does it work in terms of slicing peach fruit? </br> 
The good news is that since EV3 was introduced in 2013, it may take seven years for this affordable platform to become as popular as [Python](https://github.com/FariusGitHub/temp/tree/main/code) and [Raspberry Pi](https://www.ev3dev.org/). </br>
Another option for running this project is utilizing an industrial-grade robotic arm, which may not be accessible for some students unless they have the opportunity to work in a robotic environment </br>
such as an automotive assembly line or agricultural machinery. </br>
In the past, something comparable to Docker and Kubernetes would be a Programmable Logic Controller (PLC) and Distributed Control System (DCS), </br>
although at that time cloud computing and single-board computers did not even exist.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image35.png)</br>
The basic process in Docker involves building and running from a [Dockerfile](https://github.com/FariusGitHub/temp/blob/main/code/08_Docker_Dockerfile_Design.md), as well as pushing and pulling Docker images for sharing on Docker Hub. </br>
The Dockerfile contains a sequence of Python code stored in EV3 bricks, and a Docker container manages the selection, prioritization, and execution of these Python files. </br> 
When a Docker image is run, it [controls](https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/) the movement of a robotic arm accordingly.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image36.png)</br>
The push and pull process is crucial for cloud computing and sharing. </br>
Typically, we tag the image, push it to Docker Hub, and then pull it back to test on different machines.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image37.png)</br>
The last part of the container technologies discussion here will focus on orchestrating the containers themselves. </br>
Kubernetes is the most popular platform and offers tracking features such as [ingress](https://github.com/FariusGitHub/temp/blob/main/code/ingress.yaml), load balancer, services, and [deployment](https://github.com/FariusGitHub/temp/blob/main/code/deployment.yaml). </br>
We can switch the service based on host-based routing and typically use [load balancing within a Kubernetes service](https://github.com/FariusGitHub/temp/blob/main/code/LoadBalancerService.yaml) to connect to deployed pods that are similar.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image38.png)</br>
The next part of this blog focuses on [CI/CD](https://github.com/FariusGitHub/temp/blob/main/code/11_CICD_setup.md). We use Jenkins here, although GitHub Actions is also growing in popularity. </br>
In the beginning of this blog, I introduced automation with jenkins-cli.jar. Now, we will delve deeper into the user-friendly Web UI. </br>
For configuration, we typically use [Groovy syntax](https://github.com/FariusGitHub/temp/blob/main/code/Jenkinsfile_github), as well as cron to schedule or [webhooks](https://github.com/FariusGitHub/Example_Webpage) to trigger the pipeline when there is a change.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image39.png)</br>
```txt
Scripted Pipeline: Most functionality provided by the Groovy language is made available to Scripted Pipeline,
which means it can be an expressive and flexible tool and it is ideal choice for power-users with complex requirements. 

Example (usually within sh command)
docker run ev3
```
![](https://github.com/FariusGitHub/temp/blob/main/image/image40.png)</br>
```txt
Declarative Pipeline: Presents a more simplified and opinionated syntax. It must be enclosed with a pipeline block
and it has a strict and pre-defined structure. It is friendly for beginners. 

Example
docker.image(ev3).run
```
![](https://github.com/FariusGitHub/temp/blob/main/image/image41.png)</br>
What is interesting in CI/CD is the continuous integration and deployment of changes into the production environment. In this case, the pipeline will typically refer to the latest Dockerfile. Whenever there is a change, it will be applied, documented in the GitHub repository using Groovy syntax, and saved as an updated Dockerfile.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image42.png)</br>
What is also interesting about this project is the coexistence of distributed computing from Raspberry Pi and a robotic arm with its own system. There is a limit to what Jenkinfiles can [leverage](https://github.com/FariusGitHub/temp/blob/main/code/leverage.md), and some improvements may need to be made outside of Jenkinfiles. In this case, a voice spectrum is used to differentiate between two scenarios by changing the beep from 100 to 500. Although changes made here do not affect the Dockerfile, they do impact the Robotic Arm PyBrick MicroPython system, not the Raspberry Pi.</br></br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image43.png)</br></br>
As we covered a bit about observability in the beginning of this blog, here is how Prometheus and Grafana work together through Helm to visualize various metrics such as CPU usage, memory allocation, networking, and more.</br></br>

# SUMMARY
This blog cover an application of Raspberry Pi and DevOps application, </br>
It is actually more than AWS, Kubernetes, Docker, Produce, Robotic, IoT. </br>
In few words, it shows how agile works in term of reliability and efficiency. </br>

# LINKS
Herewith is the youtube about Pi - Peach Cutter </br>
https://www.youtube.com/watch?v=23Wq8__pd8s </br>

Below is a link to above blog in presentation format.</br> 
https://drive.google.com/file/d/1-pUiTDBRnkanjGYIGqD4miXVh1JM1Nji/view?usp=drivesdk</br>

# CREDITS
</br>Thank you to my mentors, motivators from Toronto, Mississauga, Montreal.</br>
![](https://github.com/FariusGitHub/temp/blob/main/image/image24.png)
