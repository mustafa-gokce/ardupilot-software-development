"""
    Source: https://mavlink.io/en/mavgen_python/#connection_string
    pymavlink is the library to communicate with ArduPilot firmware in Python using MAVLink
    MAVProxy and Dronekit Python are implemented using pymavlink library
    To connect to the vehicle pymavlink.mavutil.mavlink_connection() is used
    It uses the same connection string as MAVProxy and Dronekit Python
    For serial connection:
        device="COMX" for Windows
        device="/dev/ttyUSB0" for Linux
        Baud rate must be set using baud=X where X is the baud rate
    For UDP connection:
        device="udp:address:port" (legacy) or device="udpin:address:port" to connect to a stream
        device="udpout:address:port" to create a stream
        device="udpbcast:address:port" to broadcast a stream
    For TCP connection:
        device="tcp:address:port" to create a stream
        device="tcpin:address:port" to connect to a stream
"""

import pymavlink.mavutil

# connect to vehicle
vehicle = pymavlink.mavutil.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat(timeout=5)

# debugging messages
print("Connected to the vehicle")
print("Target system:", vehicle.target_system, "Target component:", vehicle.target_component)
