# Creating simulation environment starter shell script

1. Install screen package from terminal.

`sudo apt-get install screen`

2. Change directory to simulation directory

`cd && cd ardu-sim/`

3. Create a shell script.

`touch ardu-sim.sh`

4. Open the shell script in terminal using nano.

`nano ardu-sim.sh`

5. Type shell shebang to the first line of this script.

`#!/bin/bash`

6. Add simulation software binary and startup procedures to the script.

`screen -S vehicle -d -m bash -c "./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0"`

7. Add MAVProxy startup procedures.

`screen -S proxy -d -m bash -c "mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550"`

8. Save the script using pressing Ctrl+X, y and ENTER.

9. Give permissions to the script.

`sudo chmod +x ardu-sim.sh`

11. Open another terminal and connect to the vehicle using MAVProxy.

`mavproxy.py --master 127.0.0.1:14550`

Below is the final version of the ardu-sim.sh shell script.

```
#!/bin/bash
screen -S vehicle -d -m bash -c "./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0"
screen -S proxy -d -m bash -c "mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550"`
```