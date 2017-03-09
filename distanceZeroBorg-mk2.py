#!/usr/bin/python

import time
import robotZeroBorg as Robot


# -- Setup --

robot = Robot()

# set robot's speed

speed = 0.5

robot.ZB.SetMotor1(speed)
robot.ZB.SetMotor2(speed)
robot.ZB.SetMotor3(speed)
robot.ZB.SetMotor4(speed)

time.sleep(0.1)
speed = 0.30

robot.ZB.SetMotor1(speed)
robot.ZB.SetMotor2(speed)
robot.ZB.SetMotor3(speed)
robot.ZB.SetMotor4(speed)

stop_distance = 80

# -- MAIN LOOP --

while True:

    distance = robot.tof_sensor.get_distance()

    print "Measured distance is : %d mm" % distance

    if distance > stop_distance:
        print("*** Carry On ***")
    else:
        robot.ZB.MotorsOff()
        print("*** WALL ***")
