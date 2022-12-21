"""
    By default, firmware does not send any stream from a MAVLink channel (except sync messages).
    In order to get default message streams, they should be requested from the autopilot.
    REQUEST_DATA_STREAM message is used to request default streams from the vehicle.
    If you want to get all available default message streams, req_stream_id=0.
    Message rate (frequency) can be configured with req_message_rate.

    https://mavlink.io/en/messages/common.html#REQUEST_DATA_STREAM
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="tcp:127.0.0.1:5760")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create request data stream message
message = dialect.MAVLink_request_data_stream_message(target_system=vehicle.target_system,
                                                      target_component=vehicle.target_component,
                                                      req_stream_id=0,
                                                      req_message_rate=4,
                                                      start_stop=1)

# send request data stream message to the vehicle
vehicle.mav.send(message)

# infinite loop to catch all messages from simulated vehicle
while True:

    # catch all messages
    message = vehicle.recv_match(blocking=True)

    # convert this messages to dictionary
    message = message.to_dict()

    # debug the message
    print(message)
