import lineSensor
import explorerhat
import time

# define pins for the line following sensor

left_pin = 10
middle_pin = 9
right_pin = 11

# define line following object

line = lineSensor.LineSensor(left_pin, middle_pin, right_pin)

# set robot's speed

speed = 50

# define motor variables and assign zero to them

drive_left = 0
drive_right = 0
old_drive_left = 0
old_drive_right = 0

while True:

    values = line.read()
    print("left: " + str(values["left"]) + " middle: " + str(values["middle"]) + " right: " + str(values["right"]))
    if values["left"] == 1:
        drive_left = speed
        drive_right = -speed

    if values["middle"] == 1:
        drive_left = speed
        drive_right = speed

    if values["right"] == 1:
        drive_left = -speed
        drive_right= speed

    if values["left"] == 1 & values["middle"] == 1 & values["right"] == 1:
        drive_left = old_drive_left
        drive_right = old_drive_right

    explorerhat.motor.one.speed(drive_left)
    explorerhat.motor.two.speed(drive_right)

    print("left motor: " + str(drive_left) + " right motor: " + str(drive_right))

    # change value for how long before motors speeds are updated

    time.sleep(0.1)

