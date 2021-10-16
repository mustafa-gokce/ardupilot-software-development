# Changing flight mode of the vehicle using MAVProxy
1. Connect to the vehicle using `mavproxy.py --master=127.0.0.1:14550 --console --map`.
2. To change the flight mode `mode MODE_NAME` in command line.
3. Example `mode GUIDED`.
4. Let's take off the vehicle to the 10 meters:
   1. `mode GUIDED`
   2. `arm throttle`
   3. `takeoff 10`
5. Let's get back our vehicle to the ground.
   1. `mode RTL` or `mode LAND`
6. Let's fly to a location in GUIDED mode.
   1. `guided -35.36217477 149.16507393 10`