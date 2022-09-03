"""
    Source: https://mavlink.io/en/messages/common.html#MISSION_ITEM_INT
            https://mavlink.io/en/messages/common.html#MAV_FRAME
            https://mavlink.io/en/messages/common.html#MAV_CMD_NAV_WAYPOINT
            https://mavlink.io/en/messages/common.html#POSITION_TARGET_GLOBAL_INT
            https://mavlink.io/en/messages/common.html#GLOBAL_POSITION_INT
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect
import geopy.distance

# define some target locations
TARGET_LOCATIONS = [
    {
        "latitude": -35.36130812,
        "longitude": 149.16114736,
        "altitude": 30
    },
    {
        "latitude": -35.36579988,
        "longitude": 149.16302080,
        "altitude": 40
    }
]

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# vehicle's current location
current_location = {
    "latitude": 0.0,
    "longitude": 0.0
}

# vehicle's target location
target_location = {
    "latitude": 0.0,
    "longitude": 0.0,
    "distance": 0.0
}

# create target location message
message = dialect.MAVLink_mission_item_int_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    seq=0,
    frame=dialect.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
    command=dialect.MAV_CMD_NAV_WAYPOINT,
    current=2,
    autocontinue=0,
    param1=0,
    param2=0,
    param3=0,
    param4=0,
    x=int(TARGET_LOCATIONS[0]["latitude"] * 1e7),
    y=int(TARGET_LOCATIONS[0]["longitude"] * 1e7),
    z=TARGET_LOCATIONS[0]["altitude"]
)

# send target location command to the vehicle
vehicle.mav.send(message)

# create target counter
target_counter = 0

# do below always
while True:

    # catch a message
    message = vehicle.recv_match(type=[dialect.MAVLink_position_target_global_int_message.msgname,
                                       dialect.MAVLink_global_position_int_message.msgname],
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # get vehicle's current location
    if message["mavpackettype"] == dialect.MAVLink_global_position_int_message.msgname:
        current_location["latitude"] = message["lat"] * 1e-7
        current_location["longitude"] = message["lon"] * 1e-7

        # debug message
        print("Vehicle current location",
              "Latitude:", current_location["latitude"],
              "Longitude:", current_location["longitude"])

    # get vehicle's target location
    if message["mavpackettype"] == dialect.MAVLink_position_target_global_int_message.msgname:
        target_location["latitude"] = message["lat_int"] * 1e-7
        target_location["longitude"] = message["lon_int"] * 1e-7

        # calculate target location distance
        distance = geopy.distance.GeodesicDistance((current_location["latitude"],
                                                    current_location["longitude"]),
                                                   (target_location["latitude"],
                                                    target_location["longitude"])).meters
        target_location["distance"] = distance

        # reached target location
        if distance < 1:

            # increase target counter
            target_counter += 1

            # create target location message
            message = dialect.MAVLink_mission_item_int_message(
                target_system=vehicle.target_system,
                target_component=vehicle.target_component,
                seq=0,
                frame=dialect.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                command=dialect.MAV_CMD_NAV_WAYPOINT,
                current=2,
                autocontinue=0,
                param1=0,
                param2=0,
                param3=0,
                param4=0,
                x=int(TARGET_LOCATIONS[target_counter % 2]["latitude"] * 1e7),
                y=int(TARGET_LOCATIONS[target_counter % 2]["longitude"] * 1e7),
                z=TARGET_LOCATIONS[target_counter % 2]["altitude"]
            )

            # send target location command to the vehicle
            vehicle.mav.send(message)

        # debug message
        print("Vehicle target location",
              "Latitude:", target_location["latitude"],
              "Longitude:", target_location["longitude"],
              "Distance:", target_location["distance"])
