"""
    Source: https://mavlink.io/en/messages/common.html#COMMAND_LONG
            https://mavlink.io/en/messages/common.html#MAV_CMD_NAV_TAKEOFF
            https://mavlink.io/en/messages/common.html#MAV_CMD_NAV_LAND
            https://mavlink.io/en/messages/common.html#GLOBAL_POSITION_INT

"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# takeoff altitude definition
TAKEOFF_ALTITUDE = 50

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# create takeoff command
takeoff_command = dialect.MAVLink_command_long_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    command=dialect.MAV_CMD_NAV_TAKEOFF,
    confirmation=0,
    param1=0,
    param2=0,
    param3=0,
    param4=0,
    param5=0,
    param6=0,
    param7=TAKEOFF_ALTITUDE
)

# create land command
land_command = dialect.MAVLink_command_long_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    command=dialect.MAV_CMD_NAV_LAND,
    confirmation=0,
    param1=0,
    param2=0,
    param3=0,
    param4=0,
    param5=0,
    param6=0,
    param7=0
)

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# takeoff the vehicle
vehicle.mav.send(takeoff_command)

# inform user
print("Sent takeoff command to vehicle")

# check the pre-arm
while True:

    # catch GLOBAL_POSITION_INT message
    message = vehicle.recv_match(type=dialect.MAVLink_global_position_int_message.msgname,
                                 blocking=True)

    # convert message to dictionary
    message = message.to_dict()

    # get relative altitude
    relative_altitude = message["relative_alt"] * 1e-3

    # print out the message
    print("Relative Altitude", relative_altitude, "meters")

    # check if reached the target altitude
    if TAKEOFF_ALTITUDE - relative_altitude < 1:

        # print out that takeoff is successful
        print("Takeoff to", TAKEOFF_ALTITUDE, "meters is successful")

        # break the loop
        break

# wait 10 seconds
print("Waiting 10 seconds")
time.sleep(10)

# land the vehicle
vehicle.mav.send(land_command)

# inform user
print("Sent land command to vehicle")

# check the pre-arm
while True:

    # catch GLOBAL_POSITION_INT message
    message = vehicle.recv_match(type=dialect.MAVLink_global_position_int_message.msgname,
                                 blocking=True)

    # convert message to dictionary
    message = message.to_dict()

    # get relative altitude
    relative_altitude = message["relative_alt"] * 1e-3

    # print out the message
    print("Relative Altitude", relative_altitude, "meters")

    # check if reached the target altitude
    if relative_altitude < 1:

        # break the loop
        break

# wait some seconds to land
time.sleep(10)

# print out that land is successful
print("Landed successfully")
