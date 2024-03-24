# The Making of Dockerfile
Before we create a container, herewith a simple command we run traditionally without docker.</br>
Imagine that we would carve a WeCloudData logo on flat surface from the plan below and</br>
passed some parameters to Lego EV3 motor through Raspberry Pi.</br></br>

The first x of curve1 will be passed to test_motor.run_target and the second x to the ev3.speaker.beep.</br>
Herewith are couple examples below. And for this project we would take 10 curves to demonstrate the pipeline.

```txt
$ ssh robot@10.42.0.3
Password: 
  Linux ev3dev 4.14.117-ev3dev-2.3.5-ev3 #1 PREEMPT Sat Mar 7 12:54:39 CST 2020 armv5tejl
               _____     _
     _____   _|___ /  __| | _____   __
    / _ \ \ / / |_ \ / _` |/ _ \ \ / /
   |  __/\ V / ___) | (_| |  __/\ V /
    \___| \_/ |____/ \__,_|\___| \_/
  
  Debian stretch on LEGO MINDSTORMS EV3!
  Last login: Sun Mar 24 01:45:06 2024 from fe80::43ff:dbf8:d153:8be3%usb0

robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve1" "/home/robot/curve1/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve2" "/home/robot/curve2/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve3" "/home/robot/curve3/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve4" "/home/robot/curve4/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve5" "/home/robot/curve5/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve6" "/home/robot/curve6/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve7" "/home/robot/curve7/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve8" "/home/robot/curve8/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve9" "/home/robot/curve9/main.py"
robot@ev3dev:~$ brickrun -r --directory="/home/robot/curve10" "/home/robot/curve10/main.py"
robot@ev3dev:~$

robot@ev3dev:~$ cat curve1/main.py
  #!/usr/bin/env pybricks-micropython
  from pybricks.hubs import EV3Brick
  from pybricks.ev3devices import Motor
  from pybricks.parameters import Port
  # Initialize the EV3 brick.
  ev3 = EV3Brick()
  # Initialize a motor at port B.
  test_motor = Motor(Port.B)
  # Play a sound.
  ev3.speaker.beep()
  # Run the motor up to certain degrees per second. 
  test_motor.run_target(1000, 360*-1.865)
  # Play another beep sound.
  ev3.speaker.beep(-5.529*100, 100)

robot@ev3dev:~$ cat curve2/main.py
  #!/usr/bin/env pybricks-micropython
  from pybricks.hubs import EV3Brick
  from pybricks.ev3devices import Motor
  from pybricks.parameters import Port
  # Initialize the EV3 brick.
  ev3 = EV3Brick()
  # Initialize a motor at port B.
  test_motor = Motor(Port.B)
  # Play a sound.
  ev3.speaker.beep()
  # Run the motor up to certain degrees per second. 
  test_motor.run_target(1000, 360*-5.4)
  # Play another beep sound.
  ev3.speaker.beep(-5.529*100, 100)
```
![](https://github.com/FariusGitHub/temp/blob/main/image/image8.png)

The python file was automatically uploaded to EV3 bricks which also run some sort of Linux OS</br>
when Visual Code debug the python file. The python project shall be created through Visual Code</br>
extension LEGOⓇ MINDSTORMSⓇ EV3 MicroPython like below.

![](https://github.com/FariusGitHub/temp/blob/main/image/image9.png) </br>

The architecture of EV3 brick Linux OS was limited although we could create sort of [Docker-in-Docker](https://github.com/FariusGitHub/Example_Webpage).</br>
We will keep it simple by relying the Docker container on Raspberry Pi Level only and not in EV3 robot.
| Feature          | x86_64                    | armv5tejl                 |
|------------------|---------------------------|---------------------------|
| Instruction Set  | x86_64                    | ARMv5TEJL                 |
| Endianness       | Little Endian             | Little Endian             |
| Registers        | 16 general purpose        | 15 general purpose        |
|                  | registers                 | registers                 |
| Addressing Modes | Multiple                  | Limited                   |
| Memory           | 64-bit                    | 32-bit                    |
| Extensions       | SSE, AVX, AES-NI,         | SIMD, Thumb, Jazelle,     |
|                  | FMA, etc.                 | DSP, VFP, NEON, TrustZone |
| Performance      | Higher performance        | Lower performance         |
|                  | and power consumption     | and power consumption     |

One last thing we can do with Visual Code is an interacive mode inside EV3 brick itself like below.</br>
```txt
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialize the EV3 brick
ev3 = EV3Brick()

# Initialize a motor on port B
motor = Motor(Port.B)

# Move the motor forward at 50% speed for 2 seconds
motor.run(500)

# Wait for 2 seconds
ev3.speaker.beep()
ev3.speaker.beep()

# Stop the motor
motor.stop()
```
![](https://github.com/FariusGitHub/temp/blob/main/image/image10.png) 
</br>

Next, we will start to write Dockerfile below, please note that we need to do the following: </br>
- ssh robot@10.42.0.3
- pass the EV3DEV password, which is maker  --> need to install sshpass inside Dockerfile
- dump the brickrun commands

Therefore we could get a simple Dockerfile as follow

```txt
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
```

