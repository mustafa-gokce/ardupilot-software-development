# Rally Points in MAVProxy
1. Start the MAVProxy using `mavproxy.py --master=127.0.0.1:14550 --console --map`.
2. `param set RALLY_LIMIT_KM 0` to use the closest rally point.
3. Rally points have terminal commands:
   1. `rally list` is used to list rally points on flight controller.
   2. `rally load FILE_NAME` loads rally points from a file to flight controller.
   3. `rally save FILE_NAME` saves rally points from flight controller to a file.
   4. `rally clear` deletes all rally points from flight controller.
   5. `rally add` is used to add rally point to the clicked location on map.
   6. `rally remove INDEX` is used to remove a rally points listed at a specific index.
   7. `set rallyalt 50` sets default rally point altitude to 50 meters.
