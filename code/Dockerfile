FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-client sshpass

CMD ["sshpass", "-p", "maker", "ssh", "-o", "StrictHostKeyChecking=no", "robot@10.42.0.3", \
     "brickrun", "-r", "--directory=/home/robot/curve1", "/home/robot/curve1/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve2", "/home/robot/curve2/main.py", "&&", \ 
     "brickrun", "-r", "--directory=/home/robot/curve3", "/home/robot/curve3/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve4", "/home/robot/curve4/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve5", "/home/robot/curve5/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve6", "/home/robot/curve6/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve7", "/home/robot/curve7/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve8", "/home/robot/curve8/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve9", "/home/robot/curve9/main.py", "&&", \
     "brickrun", "-r", "--directory=/home/robot/curve10", "/home/robot/curve10/main.py"]
