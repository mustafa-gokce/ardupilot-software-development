"""
Connecting to the vehicle using Dronekit
Use "import dronekit" for importing the module
Use "dronekit.connect()" to connect the vehicle
Use "dronekit.close()" to close the connection

Dronekit connection arguments
ip = Connection string for vehicle
wait_ready = Wait for parameters and other attributes to be downloaded
baud = Serial connection baud rate of the vehicle (used for USB and serial connections to autopilot)

Connection strings
For serial or USB connections, find and use the connection path like /dev/ttyUSB0 (for Linux) or
    COM1 (for Windows) for ip argument of the dronekit.connect() function
When using serial or USB connections, use the appropriate baud rate by setting baud argument baud=X
    on the dronekit.connect() function
For TCP connection to the vehicle (routed by MAVProxy), set ip argument of the dronekit.connect()
    function like "tcp:<ip>:<port>", for example, "tcp:127.0.0.1:5760"
For UDP connection to the vehicle (routed by MAVProxy), set ip argument of the dronekit.connect()
    function like "<ip>:<port>", for example, "127.0.0.1:14550"
"""

import dronekit_python310_compat
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")
print("Vehicle mode: " + vehicle.mode.name)
vehicle.close()
