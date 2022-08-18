# Set Servo using MAVProxy

1. Start the simulated vehicle as usual.
2. Connect to it using MAVProxy with loading graph module like: `mavproxy.py --master=127.0.0.1:14550 --load-module="graph"`
3. Make sure that `SERVOx_FUNCTION` is set to `0`.
4. Select a channel that is not used for flight operations.
5. To set a specific servo to a specific value: `servo set CHANNEL VALUE`.
6. To create a cycle: `servo repeat CHANNEL VALUE COUNT PERIOD`
7. The cycle will be between `VALUE` and `SERVOx_TRIM` every `PERIOD` seconds `COUNT` times.
8. Observe the output with `graph SERVO_OUTPUT_RAW.servox_raw` where `x` is the selected channel.