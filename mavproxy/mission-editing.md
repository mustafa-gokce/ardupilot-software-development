# Mission Editor in MAVProxy
Connect to the vehicle using one of the following:
1. Start the MAVProxy using `mavproxy.py --master=127.0.0.1:14550 --map`.
2. To load mission editor `module load map`.
3. Mission editor also has some useful terminal commands:
   1. `wp clear` clear mission items.
   2. `wp ftp` fetches mission item list from vehicle using FTP and saves it to `way.txt`.
   3. `wp ftpload FILE_NAME` sends mission item list to vehicle using FTP.
   4. `wp list` fetches mission item list from vehicle.
   5. `wp load FILE_NAME` sends mission item list to vehicle.
   6. `wp save FILE_NAME` saves mission item list to `FILE_NAME`.
4. Note: 0th waypoint is home location.
5. To start a mission (without radio) `long MAV_CMD_MISSION_START 0 0 0 0 0 0 0 0`