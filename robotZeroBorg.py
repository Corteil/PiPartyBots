#!/usr/bin/python

import ZeroBorg
from ST_VL6180X import VL6180X


class Robot:
    def __init__(self):
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

        #  Setup the power limits
        if voltageOut > voltageIn:
            maxPower = voltageIn - (voltageIn*0.8)
        else:
            maxPower = voltageOut / float(voltageIn)

        # kill power to motors

        ZB.MotorsOff()