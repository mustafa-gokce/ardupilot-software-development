"""
Source: https://dronekit-python.readthedocs.io/en/latest/examples/vehicle_state.html
"""

import math
import dronekit_python310_compat
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

print("Global location > Latitude: {0}".format(vehicle.location.global_frame.lat))
print("Global location > Longitude: {0}".format(vehicle.location.global_frame.lon))
print("Global location > Altitude: {0}".format(vehicle.location.global_frame.alt))
print("Global relative location > Latitude: {0}".format(vehicle.location.global_relative_frame.lat))
print("Global relative location > Longitude: {0}".format(vehicle.location.global_relative_frame.lon))
print("Global relative location > Altitude: {0}".format(vehicle.location.global_relative_frame.alt))
print("Attitude > Roll: {0}".format(math.degrees(vehicle.attitude.roll)))
print("Attitude > Pitch: {0}".format(math.degrees(vehicle.attitude.pitch)))
print("Attitude > Yaw: {0}".format(math.degrees(vehicle.attitude.yaw)))
print("Heading: {0}".format(vehicle.heading))
print("Visible satellites count: {0}".format(vehicle.gps_0.satellites_visible))
print("Battery > Level: {0}".format(vehicle.battery.level))
print("Battery > Voltage: {0}".format(vehicle.battery.voltage))
print("Battery > Current: {0}".format(vehicle.battery.current))
print("EKF is healthy: {0}".format(vehicle.ekf_ok))
print("Last heartbeat: {0}".format(vehicle.last_heartbeat))
print("Vehicle is armable: {0}".format(vehicle.is_armable))
print("Vehicle is armed: {0}".format(vehicle.armed))
print("Speed > Ground speed: {0}".format(vehicle.groundspeed))
print("Speed > Air speed: {0}".format(vehicle.airspeed))
print("Vehicle mode: " + vehicle.mode.name)

while not vehicle.home_location:
    mission_items = vehicle.commands
    mission_items.download()
    mission_items.wait_ready()
    if not vehicle.home_location:
        print("Waiting for home location ...")

print("Global home location > Latitude: {0}".format(vehicle.home_location.lat))
print("Global home location > Longitude: {0}".format(vehicle.home_location.lon))
print("Global home location > Altitude: {0}".format(vehicle.home_location.alt))

print("Closing the vehicle...")
vehicle.close()
print("Closed the vehicle.")
