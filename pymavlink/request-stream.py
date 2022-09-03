"""
    EXTENDED_SYS_STATE message contains landed state of the vehicle
    This message does not send by default
    It can be requested as a stream
    Stream request can be done by sending the command as COMMAND_LONG

    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL
    https://mavlink.io/en/messages/common.html#EXTENDED_SYS_STATE
    https://mavlink.io/en/messages/common.html#MAV_LANDED_STATE
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

# create set message interval command
set_message_interval_command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                                                    target_component=vehicle.target_component,
                                                                    command=dialect.MAV_CMD_SET_MESSAGE_INTERVAL,
                                                                    confirmation=0,
                                                                    param1=dialect.MAVLINK_MSG_ID_EXTENDED_SYS_STATE,
                                                                    param2=1e6,
                                                                    param3=0,
                                                                    param4=0,
                                                                    param5=0,
                                                                    param6=0,
                                                                    param7=0)

# send command to the vehicle
vehicle.mav.send(set_message_interval_command)

# infinite loop
while True:

    # catch EXTENDED_SYS_STATE message
    message = vehicle.recv_match(type=dialect.MAVLink_extended_sys_state_message.msgname,
                                 blocking=True)

    # convert the received message to dictionary
    message = message.to_dict()

    # check landed state of the vehicle
    if message["landed_state"] == dialect.MAV_LANDED_STATE_ON_GROUND:
        print("Vehicle is on the ground")
    elif message["landed_state"] == dialect.MAV_LANDED_STATE_TAKEOFF:
        print("Vehicle is taking off")
    elif message["landed_state"] == dialect.MAV_LANDED_STATE_IN_AIR:
        print("Vehicle is on air")
    elif message["landed_state"] == dialect.MAV_LANDED_STATE_LANDING:
        print("Vehicle is landing")

    # print this message
    # print(message)
