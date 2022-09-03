"""
    Source: https://mavlink.io/en/messages/common.html#COMMAND_LONG
            https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_MODE
            https://mavlink.io/en/messages/common.html#COMMAND_ACK
            https://mavlink.io/en/messages/common.html#HEARTBEAT

    vehicle.mode_mapping() contains name and id of the flight modes capable by the vehicle
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# desired flight mode
FLIGHT_MODE = "GUIDED"

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# get supported flight modes
flight_modes = vehicle.mode_mapping()

# check the desired flight mode is supported
if FLIGHT_MODE not in flight_modes.keys():

    # inform user that desired flight mode is not supported by the vehicle
    print(FLIGHT_MODE, "is not supported")

    # exit the code
    exit(1)

# create change mode message
set_mode_message = dialect.MAVLink_command_long_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    command=dialect.MAV_CMD_DO_SET_MODE,
    confirmation=0,
    param1=dialect.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    param2=flight_modes[FLIGHT_MODE],
    param3=0,
    param4=0,
    param5=0,
    param6=0,
    param7=0
)

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# catch HEARTBEAT message
message = vehicle.recv_match(type=dialect.MAVLink_heartbeat_message.msgname, blocking=True)

# convert this message to dictionary
message = message.to_dict()

# get mode id
mode_id = message["custom_mode"]

# get mode name
flight_mode_names = list(flight_modes.keys())
flight_mode_ids = list(flight_modes.values())
flight_mode_index = flight_mode_ids.index(mode_id)
flight_mode_name = flight_mode_names[flight_mode_index]

# print mode name
print("Mode name before:", flight_mode_name)

# change flight mode
vehicle.mav.send(set_mode_message)

# do below always
while True:

    # catch COMMAND_ACK message
    message = vehicle.recv_match(type=dialect.MAVLink_command_ack_message.msgname, blocking=True)

    # convert this message to dictionary
    message = message.to_dict()

    # check is the COMMAND_ACK is for DO_SET_MODE
    if message["command"] == dialect.MAV_CMD_DO_SET_MODE:

        # check the command is accepted or not
        if message["result"] == dialect.MAV_RESULT_ACCEPTED:

            # inform the user
            print("Changing mode to", FLIGHT_MODE, "accepted from the vehicle")

        # not accepted
        else:

            # inform the user
            print("Changing mode to", FLIGHT_MODE, "failed")

        # break the loop
        break

# catch HEARTBEAT message
message = vehicle.recv_match(type=dialect.MAVLink_heartbeat_message.msgname, blocking=True)

# convert this message to dictionary
message = message.to_dict()

# get mode id
mode_id = message["custom_mode"]

# get mode name
flight_mode_names = list(flight_modes.keys())
flight_mode_ids = list(flight_modes.values())
flight_mode_index = flight_mode_ids.index(mode_id)
flight_mode_name = flight_mode_names[flight_mode_index]

# print mode name
print("Mode name after:", flight_mode_name)
