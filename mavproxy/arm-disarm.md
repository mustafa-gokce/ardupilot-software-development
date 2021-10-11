# Arming and disarming the vehicle using MAVProxy
1. Connect to the vehicle using `mavproxy.py --master=127.0.0.1:14550 --console --map`.
2. To arm the vehicle type `arm throttle` in command line.
3. To disarm the vehicle type `disarm` in command line.
4. If you arm the vehicle and do nothing it automatically disarms after `DISARM_DELAY` seconds.
5. To show disarm delay parameter `param show DISARM_DELAY`.
6. To set disarm delay parameter to 10 seconds `param set DISARM_DELAY 10`.
