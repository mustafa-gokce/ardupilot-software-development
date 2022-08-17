# Geofencing in MAVProxy
1. ArduPilot supports fences to allow your vehicle to only fly at certain areas.
2. Start the MAVProxy using `mavproxy.py --master=127.0.0.1:14550 --console --map`.
3. To enable fences, `param set FENCE_ENABLE 1` or `fence enable`.
4. To disable fences, `param set FENCE_ENABLE 0` or `fence disable`.
5. `FENCE_TYPE` is a bitmask parameter and used to which fence types will be used.
   1. By default, `7`, maximum altitude, circle, and polygon fences are enabled.
   2. To enable minimum altitude, do `param set FENCE_TYPE 15`, and also set minimum altitude
   like `param set FENCE_ALT_MIN 10` but with doing this, vehicle can't take off if 
   `FENCE_ALT_MIN` is greater than zero. So for takeoff, `fence disable` must be done.
6. By default, there is a cylindrical fence centered at home location with minimum and maximum altitudes.
   1. Radius can be set using `param set FENCE_RADIUS 300`. By doing that vehicle can't go further than 300 meters.
   2. Maximum altitude can be set using `param set FENCE_ALT_MAX 50`. By doing that vehicle can't fly higher than 50 meters.
   3. Minimum altitude can also be set using `param set FENCE_ALT_MIN 10` but `param set FENCE_TYPE 15` must be done. By doing that
   vehicle can't go lower than 10 meters.
7. By default, vehicle do RTL when breaches fence but behavior can be set using FENCE_ACTION.
8. If you want to disable user input during landing, `param set LAND_REPOSITION 0`

[Source](https://ardupilot.org/copter/docs/parameters.html#fence-parameters)