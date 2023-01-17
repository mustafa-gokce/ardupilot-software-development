# Starting the simulation software individually
1. Create a simulation directory in home.

`cd && mkdir -p ardu-sim/parameters`

2. Copy simulation software binaries and default parameters to the directory.

`cp -a $HOME/ardupilot/build/sitl/bin/. $HOME/ardu-sim/`

`cp $HOME/ardupilot/Tools/autotest/default_params/copter.parm $HOME/ardu-sim/parameters/copter.parm`

`cp $HOME/ardupilot/Tools/autotest/models/plane.parm $HOME/ardu-sim/parameters/plane.parm`

`cp $HOME/ardupilot/Tools/autotest/default_params/rover.parm $HOME/ardu-sim/parameters/rover.parm`

`cp $HOME/ardupilot/Tools/autotest/default_params/sub.parm $HOME/ardu-sim/parameters/sub.parm`

3. Get into the simulation directory.

`cd && cd ardu-sim/`

5. Open another terminal and create logs directory.

`cd && mkdir -p ardu-sim/logs && cd ardu-sim/logs/`

6. Start MAVProxy command line ground control station.

`mavproxy.py --master tcp:127.0.0.1:5760`
## Starting a copter simulation individually
`./arducopter -S --model + --speedup 1 --defaults parameters/copter.parm -I0`
## Starting a plane simulation individually
`./arduplane -S --model plane --speedup 1 --defaults parameters/plane.parm -I0`
## Starting a rover simulation individually
`./ardurover -S --model rover --speedup 1 --defaults parameters/rover.parm -I0`
## Starting a submarine simulation individually
`./ardusub -S --model vectored --speedup 1 --defaults parameters/sub.parm -I0`
## Starting an antenna tracker simulation individually
`./antennatracker -S --model tracker --speedup 1 -I0`

[Source](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html)