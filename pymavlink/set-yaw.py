"""
    Sometimes a mission may require to set the heading of the vehicle to a specific value.
    This can be done on all autonomous flight modes (like GUIDED and AUTO).
    To do that, MAV_CMD_CONDITION_YAW is used in COMMAND_LONG form.

    param1: Target angle (0 is north)
    param2: Angular speed (degrees per second)
    param3: Direction (-1: CCW, 0: Default, 1:CW)
    param4: Target angle type (0: Absolute, 1: Relative)

    WP_YAW_BEHAVIOR parameter let's set behaviour of yaw during autonomous flights.
    0 means do not change yaw at next waypoint.
    Other values overwrites previous yaw set point during flying towards next waypoint.

    https://mavlink.io/en/messages/common.html#MAV_CMD_CONDITION_YAW
    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://ardupilot.org/copter/docs/parameters.html#wp-yaw-behavior-yaw-behaviour-during-missions
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# helper constants
DIRECTION_CCW = -1
DIRECTION_DEFAULT = 0
DIRECTION_CW = 1
ANGLE_ABSOLUTE = 0
ANGLE_RELATIVE = 1

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create yaw command
message = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_CONDITION_YAW,
                                               confirmation=0,
                                               param1=90,
                                               param2=0,
                                               param3=DIRECTION_CCW,
                                               param4=ANGLE_RELATIVE,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send yaw command to the vehicle
vehicle.mav.send(message)
