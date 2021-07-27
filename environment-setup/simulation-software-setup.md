# Setting up the simulation software in Linux
1. Get into the ardupilot project directory.

`cd && cd ardupilot/`

2. Update profile.

`. ~/.profile`
## Copter simulation in Linux
1. Go into the ArduCopter directory.

`cd && cd ardupilot/ArduCopter/`

2. Start the simulation with wiping the virtual EEPROM option to load correct parameters.

`sim_vehicle.py -w`

3. After simulation has started, press Ctrl+C and start the simulation normally.

`sim_vehicle.py --console --map`
## Plane simulation in Linux
1. Go into the ArduPlane directory.

`cd && cd ardupilot/ArduPlane/`

2. Start the simulation with wiping the virtual EEPROM option to load correct parameters.

`sim_vehicle.py -w`

3. After simulation has started, press Ctrl+C and start the simulation normally.

`sim_vehicle.py --console --map`
## Rover simulation in Linux
1. Go into the Rover directory.

`cd && cd ardupilot/Rover/`

2. Start the simulation with wiping the virtual EEPROM option to load correct parameters.

`sim_vehicle.py -w`

3. After simulation has started, press Ctrl+C and start the simulation normally.

`sim_vehicle.py --console --map`
## Submarine simulation in Linux
1. Go into the ArduSub directory.

`cd && cd ardupilot/ArduSub/`

2. Start the simulation with wiping the virtual EEPROM option to load correct parameters.

`sim_vehicle.py -w`

3. After simulation has started, press Ctrl+C and start the simulation normally.

`sim_vehicle.py --console --map`
## Antenna Tracker simulation in Linux
1. Go into the AntennaTracker directory.

`cd && cd ardupilot/AntennaTracker/`

2. Start the simulation with wiping the virtual EEPROM option to load correct parameters.

`sim_vehicle.py -w`

3. After simulation has started, press Ctrl+C and start the simulation normally.

`sim_vehicle.py --console --map`

[Source](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html)