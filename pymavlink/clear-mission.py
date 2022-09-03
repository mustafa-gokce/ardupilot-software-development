"""
    In some cases, for safety or other purposes, you want to clear the mission item list
    To do that, send MISSION_CLEAR_ALL to the vehicle

    https://mavlink.io/en/messages/common.html#MISSION_CLEAR_ALL
    https://mavlink.io/en/messages/common.html#MISSION_ACK

    Content of way.txt

QGC WPL 110
0	0	0	16	0.000000	0.000000	0.000000	0.000000	-35.363262	149.165237	584.090027	1
1	0	3	22	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	50.000000	1
2	0	3	16	0.000000	0.000000	0.000000	0.000000	-35.360590	149.162043	50.000000	1
3	0	3	16	0.000000	0.000000	0.000000	0.000000	-35.360848	149.168349	50.000000	1
4	0	3	16	0.000000	0.000000	0.000000	0.000000	-35.365070	149.168583	50.000000	1
5	0	3	16	0.000000	0.000000	0.000000	0.000000	-35.364261	149.161286	50.000000	1
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create mission request list message
message = dialect.MAVLink_mission_request_list_message(target_system=vehicle.target_system,
                                                       target_component=vehicle.target_component,
                                                       mission_type=dialect.MAV_MISSION_TYPE_MISSION)

# send the message to the vehicle
vehicle.mav.send(message)

# wait mission count message
message = vehicle.recv_match(type=dialect.MAVLink_mission_count_message.msgname,
                             blocking=True)

# convert this message to dictionary
message = message.to_dict()

# get the mission item count
count = message["count"]
print("Total mission item count:", count)

# create mission clear all message
message = dialect.MAVLink_mission_clear_all_message(target_system=vehicle.target_system,
                                                    target_component=vehicle.target_component,
                                                    mission_type=dialect.MAV_MISSION_TYPE_MISSION)

# send mission clear all command to the vehicle
vehicle.mav.send(message)

# create mission request list message
message = dialect.MAVLink_mission_request_list_message(target_system=vehicle.target_system,
                                                       target_component=vehicle.target_component,
                                                       mission_type=dialect.MAV_MISSION_TYPE_MISSION)

# send the message to the vehicle
vehicle.mav.send(message)

# wait mission count message
message = vehicle.recv_match(type=dialect.MAVLink_mission_count_message.msgname,
                             blocking=True)

# convert this message to dictionary
message = message.to_dict()

# get the mission item count
count = message["count"]
print("Total mission item count:", count)
