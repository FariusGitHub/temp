Below is not a jenkinsfile, but simply it shows a leverage needed to consider outside a jenkinsfile.
Unlike Jenkinsfile that only calls python code on the EV3 bricks, it has no control on what inside it. 
Below are the example of python codes with an interactive mode to tweak the robot outside Jenkinsfile.

```txt
Pybricks MicroPython v1.11 2020-05-06; linux version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> from pybricks.hubs import EV3Brick
>>> from pybricks.ev3devices import Motor
>>> from pybricks.parameters import Port
>>> Motor(Port.B).run_target(1000, 100)
>>> EV3Brick().speaker.beep(100,100)
```
[![Play Button](https://img.icons8.com/material-outlined/24/000000/play--v1.png)](https://drive.google.com/file/d/1eeN6F5NzGrVoI5H6viZYJt6AiuZHUE5f/view?usp=drive_link)

```txt
Pybricks MicroPython v1.11 2020-05-06; linux version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> from pybricks.hubs import EV3Brick
>>> from pybricks.ev3devices import Motor
>>> from pybricks.parameters import Port
>>> Motor(Port.B).run_target(1000, 100)
>>> EV3Brick().speaker.beep(500,100)
```
[![Play Button](https://img.icons8.com/material-outlined/24/000000/play--v1.png)](https://drive.google.com/file/d/1-Ypu--c1ilZQ7s3gwirj3pHg_UNMvoLA/view?usp=drive_link)
