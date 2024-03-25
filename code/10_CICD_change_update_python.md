# Continuous Delivery = Continuous Integration + Continuous Deployment

Following a [classic](https://github.com/FariusGitHub/temp/blob/main/code/08_Docker_Dockerfile_Design.md) connection and code update to EV3 bricks, herewith is another way to call the command in cli in one line.<br>
```txt
$ sshpass -p 'maker' ssh robot@10.42.0.3 "brickrun -r --directory=\"/home/robot/curve0\" \"/home/robot/curve0/main.py\""
```
or we can preview the existing /home/robot/curve0/main.py file like below
```txt
$ sshpass -p 'maker' ssh robot@10.42.0.3 cat /home/robot/curve0/main.py
  #!/usr/bin/env pybricks-micropython
  from pybricks.hubs import EV3Brick
  from pybricks.ev3devices import Motor
  from pybricks.parameters import Port

  # Initialize the EV3 brick.
  ev3 = EV3Brick()

  # Initialize a motor at port B.
  test_motor = Motor(Port.B)

  # Run the motor up to certain degrees per second. 
  test_motor.run_target(1000, 180)

  # Play another beep sound.
  ev3.speaker.beep(100, 100)
```
And by using [spectrum analyzer](https://academo.org/demos/spectrum-analyzer/) to differentiate the sound, we can show like below.
![](https://github.com/FariusGitHub/temp/blob/main/image/image13.png) </br>
And we can change the last line of the code, says from beep(100, 100) to beep(500, 100) and review the changes like below 
```txt
$ sshpass -p 'maker' ssh robot@10.42.0.3 "sed -i 's/ev3.speaker.beep(100, 100)/ev3.speaker.beep(500, 100)/' /home/robot/curve0/main.py"
$ sshpass -p 'maker' ssh robot@10.42.0.3 cat /home/robot/curve0/main.py
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
  test_motor.run_target(1000, 180)
  # Play another beep sound.
  ev3.speaker.beep(500, 100)
```
By using the same spectrum analyzer, we can see the difference like below.
![](https://github.com/FariusGitHub/temp/blob/main/image/image14.png) </br>
