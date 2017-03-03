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




    explorerhat.motor.one.speed(drive_left)
    explorerhat.motor.two.speed(drive_right)


    old_drive_left = drive_left
    old_drive_right = drive_right

    print("left motor: " + str(drive_left) + " right motor: " + str(drive_right))


