"""
Source: https://dronekit-python.readthedocs.io/en/latest/automodule.html
        https://ardupilot.org/copter/docs/parameters.html
"""

import time
import dronekit_python310_compat
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

# get a vehicle parameter
print("ID of this vehicle: ", vehicle.parameters["SYSID_THISMAV"])

time.sleep(5)

# set a vehicle parameter
vehicle.parameters["SYSID_THISMAV"] = 2

time.sleep(5)

# get a vehicle parameter
print("ID of this vehicle: ", vehicle.parameters["SYSID_THISMAV"])

time.sleep(5)

print("Closing the vehicle...")
vehicle.close()
print("Closed the vehicle.")
