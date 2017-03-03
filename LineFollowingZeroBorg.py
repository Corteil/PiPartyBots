#!/usr/bin/env python
# coding: Latin-1

# some of the code in this program is from the example code by PiBorg.
# more imformation can be found here.
# https://github.com/piborg/zeroborg/
#
# the joy of open source code :-D

# import libraries required

import lineSensor
import ZeroBorg
import time


# define pins for the line following sensor

left_pin = 10
middle_pin = 9
right_pin = 11

# define line following object

line = lineSensor.LineSensor(left_pin, middle_pin, right_pin)

# Setup the ZeroBorg


ZB = ZeroBorg.ZeroBorg()
ZB.Init()
ZB.ResetEpo()

# Power settings
voltageIn = 8.4                         # Total battery voltage to the ZeroBorg (change to 9V if using a non-rechargeable battery)
voltageOut = 6.0                        # Maximum motor voltage

# Setup the power limits
if voltageOut > voltageIn:
    maxPower = 0.5
else:
    maxPower = voltageOut / float(voltageIn)

# kill power to motors

ZB.MotorsOff()


# set robot's speed

speed = 0.6
# define motor variables and assign zero to them

drive_left = 0
drive_right = 0
old_drive_left = 0
old_drive_right = 0

while True:

    values = line.read()
    time.sleep(0.01)

    print("*** left: " + str(values[0]) + " middle: " + str(values[1]) + " right: " + str(values[2]) + " ***")

    if values == [1,0,0]:
        drive_left = -speed
        drive_right = speed
        print("### left ###")

    if values == [0,1,0]:
        drive_left = speed
        drive_right = speed
        print("### middle ###")

    if values == [0,0,1]:
        drive_left = speed
        drive_right= -speed
        print("### right ###")

    if values == [0,0,0]:
        drive_left = old_drive_left
        drive_right = old_drive_right
        print("### old ###")

    print("### left: " + str(values[0]) + " middle: " + str(values[1]) + " right: " + str(values[2]) + " ###")

    old_drive_left = drive_left
    old_drive_right = drive_right

    print("left motor: " + str(drive_left) + " right motor: " + str(drive_right))

    # update motor values

    ZB.SetMotor1(drive_left * maxPower)
    ZB.SetMotor3(drive_left * maxPower)
    ZB.SetMotor2(drive_right * maxPower)
    ZB.SetMotor4(drive_right * maxPower)


