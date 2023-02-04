"""
    Sometimes it is necessary to pause/resume an autonomous flight.
    You may need to stop while flying autonomous, do some things, then resume to the flight.
        Drop or take a payload to/from a location calculated during flight
        Take a photo at previously unknown location
        Take some samples or measure a valuable data
    MAV_CMD_DO_PAUSE_CONTINUE is used to pause and resume an autonomous flight.
    param1 -> 0 = pause, 1 = resume (continue)
    This command can be sent with COMMAND_LONG or COMMAND_INT.

    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_PAUSE_CONTINUE
    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#COMMAND_INT

    (PS: I helped on development of this feature ^_^)
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# helper variables
PAUSE = 0
RESUME = 1

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create the command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_PAUSE_CONTINUE,
                                               confirmation=0,
                                               param1=PAUSE,
                                               param2=0,
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send this command to the vehicle
vehicle.mav.send(command)
