# Mission Editor in MAVProxy
1. Start the MAVProxy using `mavproxy.py --master=127.0.0.1:14550 --console --map`.
2. To load mission editor `module load misseditor`.
3. Mission editor also has some useful terminal commands:
   1. `wp clear` clear mission items.
   2. `wp ftp` fetches mission item list from vehicle using FTP and saves it to `way.txt`.
   3. `wp ftpload FILE_NAME` sends mission item list to vehicle using FTP.
   4. `wp list` fetches mission item list from vehicle.
   5. `wp load FILE_NAME` sends mission item list to vehicle.
   6. `wp save FILE_NAME` saves mission item list to `FILE_NAME`.
4. Note: 0th waypoint is home location.
5. To start a mission (without radio) `long MAV_CMD_MISSION_START 0 0 0 0 0 0 0 0`
6. After this lecture do `param set SIM_SPEEDUP 1` to come back to real time SITL speed.
