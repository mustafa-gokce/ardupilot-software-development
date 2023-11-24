"""
    Source: https://www.ardusub.com/developers/pymavlink.html#run-pymavlink-on-the-surface-computer
            https://mavlink.io/en/messages/common.html

    To receive a message from MAVLink stream, recv_match() is used
        type: used for filtering a specific message, ex: SYSTEM_TIME
        blocking: used for this function blocks the execution or not
        timeout: used for defining maximum blocking time

    pymavlink.dialects contains all the MAVLink message dialects
    pymavlink.dialects.v20 contains all the MAVLink2 message dialects
    pymavlink.dialects.v20.all contains all the MAVLink2 message types and definitions
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

# infinite loop
while True:

    # try to receive a message
    try:

        # receive a message
        message = vehicle.recv_match(type=dialect.MAVLink_system_time_message.msgname, blocking=True)

        # convert received message to dictionary
        message = message.to_dict()

        # for each field name in field names of this message
        for field_name in dialect.MAVLink_system_time_message.fieldnames:

            # if the field is system boot time in milliseconds
            if field_name == "time_boot_ms":
                # print field name and contained field value
                print(field_name, message[field_name])

    # exit on Ctrl+C
    except KeyboardInterrupt:
        print("User interrupt received, exiting.")
        exit(0)

    # bare except to catch all the exceptions
    except Exception as e:

        # print error message
        print(f"Error occurred: {e}")

    # tiny sleep to cool down the terminal
    time.sleep(0.010)
