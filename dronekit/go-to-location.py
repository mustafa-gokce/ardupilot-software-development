"""
Source: https://dronekit-python.readthedocs.io/en/latest/automodule.html
python3 -m pip install geographiclib
python3 -m pip install geopy
"""

import time
import dronekit_python310_compat
import dronekit
import geopy.distance


def location_callback(self, attribute_name, message):
    global target_location
    distance = geopy.distance.GeodesicDistance(target_location,
                                               (self.location.global_relative_frame.lat,
                                                self.location.global_relative_frame.lon)).meters
    self.target_distance = distance


target_location = (-35.364262, 149.165637)

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")
vehicle.target_distance = -1.0
vehicle.add_attribute_listener("location", location_callback)
vehicle.parameters["RTL_ALT"] = 3000  # 3000 centimeters = 30 meters

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
    print("Altitude:", vehicle.location.global_relative_frame.alt,
          "Target Distance:", vehicle.target_distance)
    time.sleep(1)

while vehicle.location.global_relative_frame.alt < 19.0:
    print("Altitude:", vehicle.location.global_relative_frame.alt,
          "Target Distance:", vehicle.target_distance)
    time.sleep(1)

distance = geopy.distance.GeodesicDistance(target_location,
                                           (vehicle.location.global_relative_frame.lat,
                                            vehicle.location.global_relative_frame.lon)).meters

while distance - vehicle.target_distance < 5.0:
    location = dronekit.LocationGlobalRelative(lat=target_location[0],
                                               lon=target_location[1],
                                               alt=20.0)
    vehicle.simple_goto(location)
    print("Altitude:", vehicle.location.global_relative_frame.alt,
          "Target Distance:", vehicle.target_distance)
    time.sleep(1)

while vehicle.target_distance > 5.0:
    print("Altitude:", vehicle.location.global_relative_frame.alt,
          "Target Distance:", vehicle.target_distance)
    time.sleep(1)

while vehicle.mode.name != "RTL":
    vehicle.mode = dronekit.VehicleMode("RTL")
    time.sleep(1)

print("Vehicle mode changed to RTL successful")

try:
    while True:
        print("Altitude:", vehicle.location.global_relative_frame.alt,
              "Target Distance:", vehicle.target_distance)
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing the vehicle...")
    vehicle.close()
    print("Closed the vehicle.")
