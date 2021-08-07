"""
Source: https://dronekit-python.readthedocs.io/en/latest/automodule.html
"""

import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

print("Closing the vehicle...")
vehicle.close()
print("Closed the vehicle.")
