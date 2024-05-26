# Quickstart (Windows)
If you don't want to develop embedded firmware code, you can use prebuilt simulated vehicle binaries.

## Install required software
1. Install [Git](https://github.com/git-for-windows/git/releases/download/v2.45.1.windows.1/Git-2.45.1-64-bit.exe).
2. Install [Python 3.11](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe).
3. Install [MAVProxy](https://firmware.ardupilot.org/Tools/MAVProxy/MAVProxySetup-latest.exe).
4. Install [Mission Planner](https://firmware.ardupilot.org/Tools/MissionPlanner/MissionPlanner-latest.msi).

## Download prebuilt binaries
1. Download [ArduCopter.elf](https://firmware.ardupilot.org/Tools/MissionPlanner/sitl/CopterStable/ArduCopter.elf) and save it to the `C:\ardu-sim` folder and rename it to `arducopter.exe`.
2. Download [cygwin1.dll](https://firmware.ardupilot.org/Tools/MissionPlanner/sitl/CopterStable/cygwin1.dll) and save it to the `C:\ardu-sim` folder.
3. Download [cygstdc++-6.dll](https://firmware.ardupilot.org/Tools/MissionPlanner/sitl/CopterStable/cygstdc++-6.dll) and save it to the `C:\ardu-sim` folder.
4. Download [cyggcc_s-seh-1.dll](https://firmware.ardupilot.org/Tools/MissionPlanner/sitl/CopterStable/cyggcc_s-seh-1.dll) and save it to the `C:\ardu-sim` folder.

## Download parameter file
1. Download [copter.parm](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/Tools/autotest/default_params/copter.parm) and save it to the `C:\ardu-sim\parameters` folder.

## Clone the repository
1. Get inside the `C:\` folder.
2. Open a command prompt and run the below code:
```shell
git clone https://github.com/mustafa-gokce/ardupilot-software-development.git
```

## Run the simulator
1. Open a command prompt in the `C:\ardu-sim` folder and run the below code:
```shell
arducopter -w -S --model + --speedup 1 --defaults parameters/copter.parm -I0
```
2. Open another command prompt in the `C:\ardu-sim` folder and run the below code:
```shell
mavproxy --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550 --out 127.0.0.1:14560 --daemon --no-console --non-interactive
```
3. Open Mission Planner and connect to the UDP port 14550 or run the below code in another command prompt started in the `C:\ardu-sim` folder:
```shell
mavproxy --master=127.0.0.1:14550
```

## Install required Python modules
1. Open a command prompt in the `C:\ardu-sim` folder and run the below code:
```shell
python -m pip install pymavlink==2.4.39 dronekit==2.9.2 geopy==2.3.0 get-key==1.60.0
```

## Run the example
1. Open a command prompt in the `C:\ardupilot-software-development` folder and run the below code:
```shell
python pymavlink/vehicle-connection.py
```
