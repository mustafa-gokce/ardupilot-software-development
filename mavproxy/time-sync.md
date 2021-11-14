# Time Synchronization in MAVProxy
1. Connect to the vehicle using: `mavproxy.py --master=127.0.0.1:14550`
2. Load the module `module load system_time`
3. Set the parameter `param set BRD_RTC_TYPES=1` (1st bit is enough).
4. After loading the module MAVProxy automatically sends `SYSTEM_TIME` messages to autopilot.
5. By default, MAVProxy sends messages every 10s and can be changed using:
   1. `system_time set interval_timesync X` where `X` is interval in seconds to send `TIMESYNC` message.
   2. `system_time set interval X` where `X` is interval in seconds to send `SYSTEM_TIME` message.
6. `system_time set verbose true` to show messages on air.
7. `system_time set verbose false` to hide messages on air.

[Source](https://ardupilot.org/mavproxy/docs/modules/systemtime.html)