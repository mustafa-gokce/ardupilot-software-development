"""
    Get vehicle's FENCE_ACTION parameter
    Disable the fence action (set FENCE_ACTION parameter to zero)
    Set FENCE_TOTAL parameter to zero to clear the old fence
    Set FENCE_TOTAL parameter to length on fence list
    Send FENCE_POINT messages FENCE_TOTAL many times
    Enable the fence action (set to original value)

    https://mavlink.io/en/messages/common.html#PARAM_REQUEST_READ
    https://mavlink.io/en/messages/common.html#PARAM_VALUE
    https://mavlink.io/en/messages/ardupilotmega.html#FENCE_POINT
    https://ardupilot.org/copter/docs/parameters.html#fence-action-fence-action
    https://ardupilot.org/copter/docs/parameters.html#fence-total-fence-polygon-point-total
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# introduce FENCE_TOTAL and FENCE_ACTION as byte array and do not use parameter index
FENCE_TOTAL = "FENCE_TOTAL".encode(encoding="utf-8")
FENCE_ACTION = "FENCE_ACTION".encode(encoding="utf8")
PARAM_INDEX = -1

# create fence item list
fence_list = [(-35.363152, 149.164795),  # 0th index: return point of this fence
              (-35.361019, 149.161057),  # 1st index: same as the Nth index
              (-35.360817, 149.168533),
              (-35.365364, 149.168686),
              (-35.365486, 149.160919),
              (-35.363792, 149.160919),
              (-35.363747, 149.163574),
              (-35.362366, 149.163666),
              (-35.362286, 149.161011),
              (-35.361019, 149.161057)]  # Nth index: same as the 1st index

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create PARAM_REQUEST_READ message
message = dialect.MAVLink_param_request_read_message(target_system=vehicle.target_system,
                                                     target_component=vehicle.target_component,
                                                     param_id=FENCE_ACTION,
                                                     param_index=PARAM_INDEX)

# send PARAM_REQUEST_READ message to the vehicle
vehicle.mav.send(message)

# wait until get FENCE_ACTION
while True:

    # wait for PARAM_VALUE message
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this parameter value message is for FENCE_ACTION
    if message["param_id"] == "FENCE_ACTION":
        # get the original fence action parameter from vehicle
        fence_action_original = int(message["param_value"])

        # break the loop
        break

# debug parameter value
print("FENCE_ACTION parameter original:", fence_action_original)

# run until parameter set successfully
while True:

    # create parameter set message
    message = dialect.MAVLink_param_set_message(target_system=vehicle.target_system,
                                                target_component=vehicle.target_component,
                                                param_id=FENCE_ACTION,
                                                param_value=dialect.FENCE_ACTION_NONE,
                                                param_type=dialect.MAV_PARAM_TYPE_REAL32)

    # send parameter set message to the vehicle
    vehicle.mav.send(message)

    # wait for PARAM_VALUE message
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this parameter value message is for FENCE_ACTION
    if message["param_id"] == "FENCE_ACTION":

        # make sure that parameter value reset successfully
        if int(message["param_value"]) == dialect.FENCE_ACTION_NONE:
            print("FENCE_ACTION reset to 0 successfully")

            # break the loop
            break

        # should send param set message again
        else:
            print("Failed to reset FENCE_ACTION to 0, trying again")

# run until parameter reset successfully
while True:

    # create parameter reset message
    message = dialect.MAVLink_param_set_message(target_system=vehicle.target_system,
                                                target_component=vehicle.target_component,
                                                param_id=FENCE_TOTAL,
                                                param_value=0,
                                                param_type=dialect.MAV_PARAM_TYPE_REAL32)

    # send parameter reset message to the vehicle
    vehicle.mav.send(message)

    # wait for PARAM_VALUE message
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this parameter value message is for FENCE_TOTAL
    if message["param_id"] == "FENCE_TOTAL":

        # make sure that parameter value set successfully
        if int(message["param_value"]) == 0:
            print("FENCE_TOTAL reset to 0 successfully")

            # break the loop
            break

        # should send param reset message again
        else:
            print("Failed to reset FENCE_TOTAL to 0")

# run until parameter set successfully
while True:

    # create parameter set message
    message = dialect.MAVLink_param_set_message(target_system=vehicle.target_system,
                                                target_component=vehicle.target_component,
                                                param_id=FENCE_TOTAL,
                                                param_value=len(fence_list),
                                                param_type=dialect.MAV_PARAM_TYPE_REAL32)

    # send parameter set message to the vehicle
    vehicle.mav.send(message)

    # wait for PARAM_VALUE message
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this parameter value message is for FENCE_TOTAL
    if message["param_id"] == "FENCE_TOTAL":

        # make sure that parameter value set successfully
        if int(message["param_value"]) == len(fence_list):
            print("FENCE_TOTAL set to {0} successfully".format(len(fence_list)))

            # break the loop
            break

        # should send param set message again
        else:
            print("Failed to set FENCE_TOTAL to {0}".format(len(fence_list)))

# initialize fence item index counter
idx = 0

# run until all the fence items uploaded successfully
while idx < len(fence_list):

    # create FENCE_POINT message
    message = dialect.MAVLink_fence_point_message(target_system=vehicle.target_system,
                                                  target_component=vehicle.target_component,
                                                  idx=idx,
                                                  count=len(fence_list),
                                                  lat=fence_list[idx][0],
                                                  lng=fence_list[idx][1])

    # send this message to vehicle
    vehicle.mav.send(message)

    # create FENCE_FETCH_POINT message
    message = dialect.MAVLink_fence_fetch_point_message(target_system=vehicle.target_system,
                                                        target_component=vehicle.target_component,
                                                        idx=idx)

    # send this message to vehicle
    vehicle.mav.send(message)

    # wait until receive FENCE_POINT message
    message = vehicle.recv_match(type=dialect.MAVLink_fence_point_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # get the latitude and longitude from the fence item
    latitude = message["lat"]
    longitude = message["lng"]

    # check the fence point is uploaded successfully
    if latitude != 0.0 and longitude != 0:
        # increase the index of the fence item
        idx += 1

print("All the fence items uploaded successfully")

# run until parameter set successfully
while True:

    # create parameter set message
    message = dialect.MAVLink_param_set_message(target_system=vehicle.target_system,
                                                target_component=vehicle.target_component,
                                                param_id=FENCE_ACTION,
                                                param_value=fence_action_original,
                                                param_type=dialect.MAV_PARAM_TYPE_REAL32)

    # send parameter set message to the vehicle
    vehicle.mav.send(message)

    # wait for PARAM_VALUE message
    message = vehicle.recv_match(type=dialect.MAVLink_param_value_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # make sure this parameter value message is for FENCE_ACTION
    if message["param_id"] == "FENCE_ACTION":

        # make sure that parameter value set successfully
        if int(message["param_value"]) == fence_action_original:
            print("FENCE_ACTION set to original value {0} successfully".format(fence_action_original))

            # break the loop
            break

        # should send param set message again
        else:
            print("Failed to set FENCE_ACTION to original value {0} ".format(fence_action_original))
