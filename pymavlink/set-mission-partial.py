"""
    Send MISSION_WRITE_PARTIAL_LIST message to the vehicle first
    Vehicle will respond to this with MISSION_REQUEST message
    This message contains requested mission item sequence number
    Respond to this message with MISSION_ITEM_INT message as soon as possible
    Vehicle will wait and re-request the MISSION_ITEM_INT messages with limited time and timeout
    After sending the last mission item, vehicle will send MISSION_ACK message

    https://mavlink.io/en/messages/common.html#MISSION_WRITE_PARTIAL_LIST
    https://mavlink.io/en/messages/common.html#MISSION_REQUEST
    https://mavlink.io/en/messages/common.html#MISSION_ITEM_INT
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

# create partial mission item list
target_locations = {"3": (-35.36088422, 149.17235277, 50.0),
                    "4": (-35.36547152, 149.17320997, 50.0)}

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create mission write partial list message
message = dialect.MAVLink_mission_write_partial_list_message(target_system=vehicle.target_system,
                                                             target_component=vehicle.target_component,
                                                             start_index=3,
                                                             end_index=4,
                                                             mission_type=dialect.MAV_MISSION_TYPE_MISSION)

# send mission write partial list message to the vehicle
vehicle.mav.send(message)

# this loop will run until receive a valid MISSION_ACK message
while True:

    # catch a message
    message = vehicle.recv_match(blocking=True)

    # convert this message to dictionary
    message = message.to_dict()

    # check this message is MISSION_REQUEST
    if message["mavpackettype"] == dialect.MAVLink_mission_request_message.msgname:

        # check this request is for mission items
        if message["mission_type"] == dialect.MAV_MISSION_TYPE_MISSION:

            # get the sequence number of requested mission item
            seq = message["seq"]

            # create mission item int message that contains a target location
            message = dialect.MAVLink_mission_item_int_message(target_system=vehicle.target_system,
                                                               target_component=vehicle.target_component,
                                                               seq=seq,
                                                               frame=dialect.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                                               command=dialect.MAV_CMD_NAV_WAYPOINT,
                                                               current=0,
                                                               autocontinue=0,
                                                               param1=0,
                                                               param2=0,
                                                               param3=0,
                                                               param4=0,
                                                               x=int(target_locations[str(seq)][0] * 1e7),
                                                               y=int(target_locations[str(seq)][1] * 1e7),
                                                               z=target_locations[str(seq)][2],
                                                               mission_type=dialect.MAV_MISSION_TYPE_MISSION)

            # send the mission item int message to the vehicle
            vehicle.mav.send(message)

    # check this message is MISSION_ACK
    elif message["mavpackettype"] == dialect.MAVLink_mission_ack_message.msgname:

        # check this acknowledgement is for mission and it is accepted
        if message["mission_type"] == dialect.MAV_MISSION_TYPE_MISSION and \
                message["type"] == dialect.MAV_MISSION_ACCEPTED:
            # break the loop since the upload is successful
            print("Mission upload is successful")
            break
