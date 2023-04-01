"""
    Sometimes you may want to check if a terrain data is available for an area or location.
    This script will check if a terrain database is available for a particular location.
    ArduPilot is capable of terrain following in autonomous flights.
    But it requires a terrain database to be loaded into the autopilot.
    Terrain database is available from the https://terrain.ardupilot.org/ website.
    Select the area of interest and download the database.
    Put the files in the /APM/terrain/ directory on the SD card (or /terrain of simulation).

    https://mavlink.io/en/messages/common.html#TERRAIN_CHECK
    https://mavlink.io/en/messages/common.html#TERRAIN_REPORT
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# define the location
terrain_location = (-35.36166212, 149.16117570)
terrain_location = (int(terrain_location[0] * 1e7), int(terrain_location[1] * 1e7))
print("Terrain location (lat, lon):", terrain_location)

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create terrain check message
message = dialect.MAVLink_terrain_check_message(lat=terrain_location[0],
                                                lon=terrain_location[1])

# send the message to the vehicle
vehicle.mav.send(message)

# infinite loop
while True:

    # capture TERRAIN_REPORT messages
    message = vehicle.recv_match(type=dialect.MAVLink_terrain_report_message.msgname,
                                 blocking=True)

    # convert the captured message to dictionary
    message = message.to_dict()

    # check the message is specifically sent for our terrain location
    if message["lat"] == terrain_location[0] and message["lon"] == terrain_location[1]:
        break

# print the capture message
print(message)
