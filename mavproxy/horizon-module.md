# Horizon Module in MAVProxy
1. Connect to the vehicle using `mavproxy.py --master=127.0.0.1:14550 --load-module="horizon,map,console"`.
2. Or after starting MAVProxy, `module load MODULE_NAME`, ex: `module load horizon`.
3. Let's take off the vehicle to the 50 meters:
   1. `mode GUIDED`
   2. `arm throttle`
   3. `takeoff 50`
4. Let's get back our vehicle to the ground using `mode LAND`.
5. Let's fly to a location in GUIDED mode using `guided -35.36217477 149.16507393 50`.
6. Let's change the mode to LOITER using `mode LOITER`.
7. By using `rc X Y`, MAVProxy periodically send RC Override to channel X with Y PWM value.
   1. `rc 1 X` overrides roll PWM with X value. 
      1. `X>1500` means roll right.
      2. `X<1500` means roll left.
      3. `X=1500` means no roll but still send RC Roll Override message.
   2. `rc 2 X` overrides pitch PWM with X value.
      1. `X>1500` means pitch backward.
      2. `X<1500` means pitch forward.
      3. `X=1500` means no pitch but still send RC Pitch Override message.
   3. `rc 3 X` overrides throttle PWM with X value.
      1. `X>1500` means gain altitude in LOITER mode.
      2. `X<1500` means lower altitude in LOITER mode.
      3. `X=1500` means maintain altitude in LOITER mode.
   4. `rc 4 X` overrides yaw PWM with X value.
      1. `X>1500` means yaw clockwise.
      2. `X<1500` means yaw counter-clockwise.
      3. `X=1500` means no yaw but still send RC Yaw Override message.
8. In GUIDED mode, copter can process RC Yaw Override message.
