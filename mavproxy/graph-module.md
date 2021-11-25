# Graph Module in MAVProxy
1. Graph module plots live data from vehicle for monitoring vehicle state.
2. Connect to the vehicle using `mavproxy.py --master=127.0.0.1:14550`.
3. After starting MAVProxy `module load graph`.
4. `graph MESSAGE_NAME.FIELD_NAME` is used to graph specific data field.
5. Multiple data can be plotted to the same graph as:
   1. `graph MESSAGE_NAME1.FIELD_NAME1 MESSAGE_NAME2.FIELD_NAME2 MESSAGE_NAME3.FIELD_NAME3`.
6. `graph legend MESSAGE_NAME1.FIELD_NAME1 LEGEND_NAME` is used to add legend to graph.
7. Use `graph timespan X` to change the time space to X seconds on axis-x.
8. Use `graph tickresolution X` to change the tick resolution to X seconds on axis-x.
9. Mathematical operations are allowed in data.
10. Multiple graphs are allowed.
11. Let's plot altitude using [VFR_HUD](https://mavlink.io/en/messages/common.html):
    1. `graph legend (VFR_HUD.alt-584) "Relative Altitude"`
    2. `graph (VFR_HUD.alt-584)`
12. Let's plot relative altitude using [GLOBAL_POSITION_INT](https://mavlink.io/en/messages/common.html#GLOBAL_POSITION_INT)
    1. `graph legend (GLOBAL_POSITION_INT.relative_alt/1000.0) "Relative Altitude"`
    2. `graph (GLOBAL_POSITION_INT.relative_alt/1000.0)`
13. Let's plot [VIBRATION](https://mavlink.io/en/messages/common.html#VIBRATION) on all axes:
    1. `graph legend VIBRATION.vibration_x "Vibration on X axis"`
    2. `graph legend VIBRATION.vibration_y "Vibration on Y axis"`
    3. `graph legend VIBRATION.vibration_z "Vibration on Z axis"`
    4. `graph VIBRATION.vibration_x VIBRATION.vibration_y VIBRATION.vibration_z`
14. Homework:
    1. Takeoff to 10 meters.
    2. Fly to a location in GUIDED mode on 10 meters and observe the graphs.
    3. On different graphs plot:
       1. Desired roll vs. roll
       2. Desired pitch vs. pitch
       3. Desired yaw vs. yaw
    4. Each plots must be in float degrees.
    5. Add legend to all the graphs before plotting (like specified in 3rd step).
    6. Set time span to 10 seconds before plotting.
    7. Set tick resolution to 0.1 seconds before plotting.
    8. Hint: [NAV_CONTROLLER_OUTPUT](https://mavlink.io/en/messages/common.html#NAV_CONTROLLER_OUTPUT), 
[ATTITUDE](https://mavlink.io/en/messages/common.html#ATTITUDE)

[Source](https://ardupilot.org/mavproxy/docs/modules/graph.html)
