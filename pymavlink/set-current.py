"""
    In some cases, it is desired to change vehicle's current mission item during auto flight mode
    To do this, send MAV_CMD_DO_SET_MISSION_CURRENT command as COMMAND_LONG with sequence number
    To check it is successful or not, look sequence number on MISSION_CURRENT message
    Vehicle will travel to the new mission item by following the shortest path

    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_MISSION_CURRENT
    https://mavlink.io/en/messages/common.html#MISSION_CURRENT

    Content of way.txt

QGC WPL 110
0	0	0	16	0.000000	0.000000	0.000000	0.000000	-35.363262	149.165237	584.090027	1
1	0	3	22	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	30.000000	1
2	0	3	16	0.000000	0.000000	0.000000	0.000000	-35.363355	149.158274	30.000000	1
3	0	3	16	0.000000	0.000000	0.000000	0.000000	-35.362944	149.173090	30.000000	1
"""

import sys
import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# get the desired sequence number
seq_desired = int(sys.argv[1])

# debug the desired sequence number
print("Desired mission item:", seq_desired)

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# wait until receive MISSION_CURRENT message
message = vehicle.recv_match(type=dialect.MAVLink_mission_current_message.msgname,
                             blocking=True)

# convert message to dictionary
message = message.to_dict()

# get current sequence number
seq_current = message["seq"]

# debug the message
print("Current mission item:", seq_current)

# create MAV_CMD_DO_SET_MISSION_CURRENT command
message = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_SET_MISSION_CURRENT,
                                               confirmation=0,
                                               param1=seq_desired,
                                               param2=0,
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send this message to the vehicle
vehicle.mav.send(message)

# wait until receive MISSION_CURRENT message
message = vehicle.recv_match(type=dialect.MAVLink_mission_current_message.msgname,
                             blocking=True)

# convert message to dictionary
message = message.to_dict()

# get current sequence number
seq_current = message["seq"]

# debug the message
print("Current mission item:", seq_current)

if seq_desired == seq_current:
    print("Set current mission item is successful")
else:
    print("Failed to set current mission item")
