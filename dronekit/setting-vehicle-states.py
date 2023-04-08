"""
Source: https://dronekit-python.readthedocs.io/en/latest/automodule.html

To arm the vehicle
vehicle.arm(wait=True, timeout=None)
vehicle.armed = True

To disarm the vehicle
vehicle.disarm(wait=True, timeout=None)  # or
vehicle.armed = False

To set flight air speed (in m/s)
vehicle.airspeed = 10.0

To set flight ground speed (in m/s)
vehicle.groundspeed = 10.0

To give takeoff command
vehicle.simple_takeoff(10.0)

To go to a location
vehicle.simple_goto(location=dronekit.LocationGlobalRelative(-34.364114, 149.166022, 30),
                    airspeed=10.0, groundspeed=10.0)

To set vehicle home location
vehicle.home_location = dronekit.LocationGlobal(-34.364114, 149.166022, 584)
"""

import time
import dronekit_python310_compat
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

# arm the vehicle
vehicle.armed = True
print("Sent arm command.")

time.sleep(5)
print("Arm status:", vehicle.armed)

# disarm the vehicle
vehicle.armed = False
print("Sent disarm command.")

time.sleep(5)
print("Arm status:", vehicle.armed)

# change flight mode
vehicle.mode = dronekit.VehicleMode("GUIDED")
print("Sent change mode command.")

time.sleep(5)
print("Vehicle mode:", vehicle.mode.name)

print("Closing the vehicle...")
vehicle.close()
print("Closed the vehicle.")
