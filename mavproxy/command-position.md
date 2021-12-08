# "position" Command in MAVProxy
1. Start the MAVProxy using `mavproxy.py --master=127.0.0.1:14550 --console --map`.
2. Position command in MAVProxy is used to move the vehicle relative to current location and heading.
3. Usage: `position x y z`
   1. Positive `x` means move `x` meters forward.
   2. Negative `x` means move `x` meters backward.
   3. Positive `y` means move `y` meters right.
   4. Negative `y` means move `y` meters left.
   5. Positive `z` means lose `z` meters altitude.
   6. Negative `z` means gain `z` meters altitude.
