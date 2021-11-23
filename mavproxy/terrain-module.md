# Terrain Module in MAVProxy
1. Terrain module in MAVProxy provides terrain data by downloading them from internet and cache inside SD card of 
flight controller to use in terrain data related flight modes (any commands framed as 
[MAV_FRAME_GLOBAL_TERRAIN_ALT](https://mavlink.io/en/messages/common.html#MAV_FRAME_GLOBAL_TERRAIN_ALT) 
or [MAV_FRAME_GLOBAL_TERRAIN_ALT_INT](https://mavlink.io/en/messages/common.html#MAV_FRAME_GLOBAL_TERRAIN_ALT_INT)).
2. Connect to the vehicle using `mavproxy.py --master=127.0.0.1:14550 --load-module="map"`.
3. After starting MAVProxy `module load terrain`.
4. `terrain status` is used to show requested or supplied terrain data.
5. `terrain check` is used to query flight stack to show terrain related information of the position clicked on map.
6. `terrain check LATITUDE LONGITUDE` is used to query flight stack to show terrain related information of the position.

[Source](https://ardupilot.org/mavproxy/docs/modules/terrain.html)
