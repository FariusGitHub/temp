# Infrastructure as a Code for Jenkins with jenkins-cli.jar

Based on earlier [blog](https://medium.com/p/69b2bc0adc3e/edit), we could mimic the same approach to run EV3. 
These sequence of code consist of:
- basic jenkins installation steps
- some necessary steps to enable access
- automation with cli

```txt
#!/bin/bash
sudo apt update
sudo apt install fontconfig openjdk-17-jre -y
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
http://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list> /dev/null
sudo apt-get update
sudo apt-get install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

# make /var/cache/jenkins accessible
sudo chown -R ubuntu:ubuntu /var/cache/jenkins              
sudo chmod -R 755 /var/cache/jenkins

# save initialAdminPassword into passjenkins, create and build project6
cd /var/cache/jenkins/war/WEB-INF/                          
sudo wget http://localhost:8080/jnlpJars/jenkins-cli.jar
export passjenkins=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
curl -LJO https://github.com/FariusGitHub/Jenkins/raw/main/config.xml -o /var/cache/jenkins/war/WEB-INF/config.xml
java -jar jenkins-cli.jar -auth admin:$passjenkins -s http://localhost:8080 create-job project6 < config.xml
java -jar jenkins-cli.jar -auth admin:$passjenkins -s http://localhost:8080 build project6
```
