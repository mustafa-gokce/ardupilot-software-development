# Creating simulation environment starter shell script

1. Install screen and nano packages from terminal.

`sudo apt-get install screen nano`

2. Change directory to simulation directory.

`cd && cd ardu-sim/`

3. Create a shell script.

`touch ardu-sim.sh`

4. Open the shell script in terminal using nano.

`nano ardu-sim.sh`

5. Type shell shebang (specifies bash binary location) to the first line of this script.

`#!/bin/bash`

6. Add simulation software binary and startup procedures to the script.

`screen -S vehicle -d -m bash -c "./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0"`

7. Add MAVProxy startup procedures.

`screen -S proxy -d -m bash -c "mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550"`

8. Save the script by pressing Ctrl+X, y and ENTER.

9. Below is the final version of the ardu-sim.sh shell script.

```
#!/bin/bash
screen -S vehicle -d -m bash -c "./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0"
screen -S proxy -d -m bash -c "mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550"
```

10. Give permissions to the script.

`sudo chmod +x ardu-sim.sh`

11. Run the script.

`./ardu-sim.sh`

12. Open another terminal and connect to the vehicle using MAVProxy.

`cd && cd ardu-sim/logs/`

`mavproxy.py --master 127.0.0.1:14550`

13. To retrieve simulation software binary session, do the below.

`screen -r vehicle`

14. To exit the simulation software binary session, press Ctrl+a, d and ENTER.

15. To retrieve MAVProxy session, do the below.

`screen -r proxy`

16. To exit the MAVProxy session, press Ctrl+a, d and ENTER.

17. To stop the simulation software binary session, do the below.

`screen -S vehicle -X quit`

18. To stop the MAVProxy session, do the below.

`screen -S proxy -X quit`

19. To stop both of them at the same time, do the below.

`killall screen`
