#!/usr/bin/python

""" ST VL6180X ToF range finder program
 - power explorer board with 3.3 V
 - explorer board includes pull-ups on i2c """

import sys
import ZeroBorg
from ST_VL6180X import VL6180X
import time


# -- Setup --

debug = False
if len(sys.argv) > 1:
    if sys.argv[1] == "debug":  # sys.argv[0] is the filename
        debug = True


# setup ToF ranging/ALS sensor
tof_address = 0x29
tof_sensor = VL6180X(address=tof_address, debug=debug)
tof_sensor.get_identification()
if tof_sensor.idModel != 0xB4:
    print"Not a valid sensor id: %X" % tof_sensor.idModel
else:
    print"Sensor model: %X" % tof_sensor.idModel
    print"Sensor model rev.: %d.%d" % \
         (tof_sensor.idModelRevMajor, tof_sensor.idModelRevMinor)
    print"Sensor module rev.: %d.%d" % \
         (tof_sensor.idModuleRevMajor, tof_sensor.idModuleRevMinor)
    print"Sensor date/time: %X/%X" % (tof_sensor.idDate, tof_sensor.idTime)
tof_sensor.default_settings()

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

speed = 0.5

ZB.SetMotor1(speed)
ZB.SetMotor3(speed)
ZB.SetMotor2(speed)
ZB.SetMotor4(speed)

time.sleep(0.1)
speed = 0.30

ZB.SetMotor1(speed)
ZB.SetMotor3(speed)
ZB.SetMotor2(speed)
ZB.SetMotor4(speed)

stop_distance = 80

# -- MAIN LOOP --

while True:
    distance = tof_sensor.get_distance()
    light_level = tof_sensor.get_ambient_light(20)
    print "Measured distance is : %d mm" % distance

    if distance > stop_distance:
        ZB.SetMotor1(speed)
        ZB.SetMotor3(speed)
        ZB.SetMotor2(speed)
        ZB.SetMotor4(speed)
    else:
        ZB.MotorsOff()
        print("*** WALL ***")
