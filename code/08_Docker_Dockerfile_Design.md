# The Making of Dockerfile
Before we create a container, herewith a simple command we run traditionally without docker.

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
```
