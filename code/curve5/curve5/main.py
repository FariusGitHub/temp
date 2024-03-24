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
test_motor.run_target(1000, 360*-0.2719)
# Play another beep sound.
ev3.speaker.beep(0*100, 100)