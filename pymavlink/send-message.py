"""
    Source: https://mavlink.io/en/messages/common.html#COMMAND_LONG
            https://mavlink.io/en/messages/common.html#MAV_CMD
            https://mavlink.io/en/messages/ardupilotmega.html#MAV_CMD_DO_SEND_BANNER
            https://mavlink.io/en/messages/common.html#STATUSTEXT
            https://mavlink.io/en/messages/common.html#COMMAND_ACK

    To receive a message from MAVLink stream, recv_match() is used
    To send a message, mav.send() is used

    There are three ways to send commands to vehicle:
        COMMAND_LONG (MAV_CMD_* command messages)
        COMMAND_INT (MAV_CMD_* command messages)
        CUSTOM (Like SET_POSITION_TARGET_LOCAL_NED, SET_POSITION_TARGET_GLOBAL_INT, ...)
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# build up the command message
message = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_SEND_BANNER,
                                               confirmation=0,
                                               param1=0,
                                               param2=0,
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send the command to the vehicle
vehicle.mav.send(message)

# do below always
while True:

    # receive a message
    message = vehicle.recv_match(type=[dialect.MAVLink_statustext_message.msgname,
                                       dialect.MAVLink_command_ack_message.msgname],
                                 blocking=True)

    # convert message to dictionary
    message = message.to_dict()

    # show the message
    print(message)
