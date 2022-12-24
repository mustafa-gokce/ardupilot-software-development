"""
    Sometimes a mission may require a certain flight speed from the vehicle.
    For example:
                Deliver a supply item as fast as possible.
                Slowly move to capture or admire a scenic view over the air.
                Match the flight speed with another moving object.
    Flight speed can be changed using MAV_CMD_DO_CHANGE_SPEED in the COMMAND_LONG form.

    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_CHANGE_SPEED
    https://mavlink.io/en/messages/common.html#COMMAND_LONG
"""

import sys
import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# get flight speed from user (in meters per second form)
desired_flight_speed = float(sys.argv[1])

# debug the desired flight speed
print("Desired flight speed:", desired_flight_speed)

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create the command
message = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_CHANGE_SPEED,
                                               confirmation=0,
                                               param1=0,
                                               param2=desired_flight_speed,
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send the command to the vehicle
vehicle.mav.send(message)
