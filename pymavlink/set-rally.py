"""
    Set RALLY_TOTAL parameter to length on rally point list
    Send RALLY_POINT messages RALLY_TOTAL many times

    https://mavlink.io/en/messages/common.html#PARAM_REQUEST_READ
    https://mavlink.io/en/messages/common.html#PARAM_VALUE
    https://mavlink.io/en/messages/ardupilotmega.html#RALLY_FETCH_POINT
    https://mavlink.io/en/messages/ardupilotmega.html#RALLY_POINT
    https://ardupilot.org/copter/docs/parameters.html#rally-total-rally-total
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# introduce RALLY_TOTAL as byte array and do not use parameter index
RALLY_TOTAL = "RALLY_TOTAL".encode(encoding="utf-8")
PARAM_INDEX = -1

# create rally point item list
rally_list = [(-35.361235, 149.161052, 100.000000),
              (-35.362089, 149.164452, 100.000000),
              (-35.364099, 149.161712, 100.000000),
              (-35.363649, 149.166642, 100.000000),
              (-35.359978, 149.168170, 100.000000)]

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# run until parameter set successfully
while True:

    # create parameter set message
    message = dialect.MAVLink_param_set_message(target_system=vehicle.target_system,
                                                target_component=vehicle.target_component,
                                                param_id=RALLY_TOTAL,
                                                param_value=len(rally_list),
                                                param_type=dialect.MAV_PARAM_TYPE_REAL32)

    # send parameter set message to the vehicle
    vehicle.mav.send(message)

    # wait for PARAM_VALUE message
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this parameter value message is for RALLY_TOTAL
    if message["param_id"] == "RALLY_TOTAL":

        # make sure that parameter value set successfully
        if int(message["param_value"]) == len(rally_list):
            print("RALLY_TOTAL set to {0} successfully".format(len(rally_list)))

            # break the loop
            break

        # should send param set message again
        else:
            print("Failed to set RALLY_TOTAL to {0}".format(len(rally_list)))

# initialize rally point item index counter
idx = 0

# run until all the rally point items uploaded successfully
while idx < len(rally_list):

    # create RALLY_POINT message
    message = dialect.MAVLink_rally_point_message(target_system=vehicle.target_system,
                                                  target_component=vehicle.target_component,
                                                  idx=idx,
                                                  count=len(rally_list),
                                                  lat=int(rally_list[idx][0] * 1e7),
                                                  lng=int(rally_list[idx][1] * 1e7),
                                                  alt=int(rally_list[idx][2]),
                                                  break_alt=0,
                                                  land_dir=0,
                                                  flags=0)

    # send RALLY_POINT message to the vehicle
    vehicle.mav.send(message)

    # create RALLY_FETCH_POINT message
    message = dialect.MAVLink_rally_fetch_point_message(target_system=vehicle.target_system,
                                                        target_component=vehicle.target_component,
                                                        idx=idx)

    # send this message to vehicle
    vehicle.mav.send(message)

    # wait for RALLY_POINT message
    message = vehicle.recv_match(type=dialect.MAVLink_rally_point_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this RALLY_POINT message is for the same rally point item
    if message["idx"] == idx and \
            message["count"] == len(rally_list) and \
            message["lat"] == int(rally_list[idx][0] * 1e7) and \
            message["lng"] == int(rally_list[idx][1] * 1e7) and \
            message["alt"] == int(rally_list[idx][2]):

        # increment rally point item index counter
        idx += 1

        # inform user
        print("Rally point {0} uploaded successfully".format(idx))

    # should send RALLY_POINT message again
    else:
        print("Failed to upload rally point {0}".format(idx))

print("All the rally point items uploaded successfully")
