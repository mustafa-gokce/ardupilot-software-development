"""
Source: https://dronekit-python.readthedocs.io/en/latest/automodule.html
"""

import time
import dronekit_python310_compat
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

while vehicle.mode.name != "GUIDED":
    vehicle.mode = dronekit.VehicleMode("GUIDED")
    time.sleep(1)

print("Vehicle mode:", vehicle.mode.name)

vehicle.send_calibrate_barometer()

while not vehicle.is_armable:
    time.sleep(1)

print("Vehicle is armable:", vehicle.is_armable)

while not vehicle.armed:
    vehicle.armed = True
    time.sleep(1)

print("Vehicle is armed:", vehicle.armed)

while vehicle.location.global_relative_frame.alt < 5.0:
    vehicle.simple_takeoff(20)
    print("Altitude:", vehicle.location.global_relative_frame.alt)
    time.sleep(1)

print("Vehicle takeoff successful")
time.sleep(20)

while vehicle.mode.name != "LAND":
    vehicle.mode = dronekit.VehicleMode("LAND")
    time.sleep(1)

print("Vehicle land successful")

try:
    while True:
        print("Altitude:", vehicle.location.global_relative_frame.alt)
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing the vehicle...")
    vehicle.close()
    print("Closed the vehicle.")
