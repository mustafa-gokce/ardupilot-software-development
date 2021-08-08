"""
Source: https://dronekit-python.readthedocs.io/en/latest/automodule.html

To bind a function to an attribute change
vehicle.add_attribute_listener(attribute_name, observer_function_name)
Attributes that represent sensor values or which are used to monitor connection
status are updated whenever a message is received from the vehicle.
Attributes which reflect vehicle “state” are only updated when their values change,
for example vehicle.system_status, vehicle.armed, and vehicle.mode.
To remove the attribute listener:
vehicle.remove_attribute_listener(attribute_name, observer_function_name)

You can add attribute listener to parameters.
vehicle.parameters.add_attribute_listener("PARAMETER_NAME", observer_function_name)
To remove the attribute listener:
vehicle.parameters.remove_attribute_listener("PARAMETER_NAME", observer_function_name)
Parameters for Ardupilot Copter firmware can be found in the copter documentation:
https://ardupilot.org/copter/docs/parameters.html

You can add message listeners to the script and the listener function will be called
whenever the specific message is received.
vehicle.add_message_listener("MESSAGE_NAME", observer_function_name)
To remove the attribute listener:
vehicle.remove_message_listener("MESSAGE_NAME", observer_function_name)
Message names can be found in MAVLink documentation:
https://mavlink.io/en/messages/common.html
"""

import time
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")


# dummy loop waiting for keyboard interrupt
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Closing the vehicle...")
    vehicle.close()
    print("Closed the vehicle.")
