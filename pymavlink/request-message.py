"""
    AUTOPILOT_VERSION message includes flight_sw_version field contains firmware version
    It also includes git hash of the latest commit in flight_custom_version

    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#MAV_CMD_REQUEST_MESSAGE
    https://mavlink.io/en/messages/common.html#AUTOPILOT_VERSION
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

# create request message command
request_message_command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                                               target_component=vehicle.target_component,
                                                               command=dialect.MAV_CMD_REQUEST_MESSAGE,
                                                               confirmation=0,
                                                               param1=dialect.MAVLINK_MSG_ID_AUTOPILOT_VERSION,
                                                               param2=0,
                                                               param3=0,
                                                               param4=0,
                                                               param5=0,
                                                               param6=0,
                                                               param7=0)

# send command to the vehicle
vehicle.mav.send(request_message_command)

# infinite loop
while True:
    # catch AUTOPILOT_VERSION message
    message = vehicle.recv_match(type=dialect.MAVLink_autopilot_version_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # get flight software version
    print("Major:", message["flight_sw_version"] >> 24 & 0xFF)
    print("Minor:", message["flight_sw_version"] >> 16 & 0xFF)
    print("Patch:", message["flight_sw_version"] >> 8 & 0xFF)

    # get git commit hash
    print("Hash:", "".join([chr(i) for i in message["flight_custom_version"]]))
