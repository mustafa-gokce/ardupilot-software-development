"""
    Source: https://mavlink.io/en/messages/common.html#PARAM_REQUEST_LIST
            https://mavlink.io/en/messages/common.html#PARAM_REQUEST_READ
            https://mavlink.io/en/messages/common.html#PARAM_VALUE
            https://mavlink.io/en/messages/common.html#PARAM_SET

    PARAM_REQUEST_LIST: Get all the on-board parameters, vehicle will emit PARAM_VALUE messages back
    PARAM_REQUEST_READ: Request a value of specific parameter
    PARAM_VALUE: Contains a parameter value, only sent when requested or a parameter change
    PARAM_SET: Used to set a specific parameter value
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# introduce system id parameter name
SYSID_THISMAV = "SYSID_THISMAV"

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# create parameter request list message
parameter_request_list_message = dialect.MAVLink_param_request_list_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component
)

# create parameter request message
parameter_request_message = dialect.MAVLink_param_request_read_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    param_id=SYSID_THISMAV.encode("utf-8"),
    param_index=-1
)

# create parameter set message
parameter_set_message = dialect.MAVLink_param_set_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    param_id=SYSID_THISMAV.encode("utf-8"),
    param_value=2,
    param_type=dialect.MAV_PARAM_TYPE_REAL32
)

# wait for a heartbeat
vehicle.wait_heartbeat()

# send param request list message to the vehicle
# vehicle.mav.send(parameter_request_list_message)

# send param request message to the vehicle
vehicle.mav.send(parameter_request_message)

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# do below always
while True:

    # receive parameter value messages
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname, blocking=True)

    # convert message to dictionary
    message = message.to_dict()

    # filter only system id param value message
    if message["param_id"] == SYSID_THISMAV:

        # print the message to the screen
        print(message["param_id"], message["param_value"])

        # break this loop
        break

# send param set message to the vehicle
vehicle.mav.send(parameter_set_message)

# do below always
while True:

    # receive parameter value messages
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname, blocking=True)

    # convert message to dictionary
    message = message.to_dict()

    # filter only system id param value message
    if message["param_id"] == SYSID_THISMAV:

        # print the message to the screen
        print(message["param_id"], message["param_value"])

        # break this loop
        break
