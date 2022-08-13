#!/bin/bash

# install necessary packages
sudo apt-get install nano screen terminator python3-pip python3-dev python3-opencv python3-wxgtk4.0 python3-matplotlib python3-lxml python3-pygame

# install python modules
/usr/bin/python3 -m pip install PyYAML MAVProxy dronekit

# add path to bashrc
echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc

# give permission to connect serial devices
sudo usermod -a -G dialout "$USER"

# go to home directory
cd "$HOME" || exit 1

# create simulation directory
mkdir -p "$HOME/ardu-sim/"

# get inside simulation directory
cd "$HOME/ardu-sim/" || exit 1

# clear directory
rm -r ./*

# get simulation binary
wget https://firmware.ardupilot.org/Copter/stable/SITL_x86_64_linux_gnu/arducopter

# make the binary executable
sudo chmod +x arducopter

# create parameters directory
mkdir -p "$HOME/ardu-sim/parameters/"

# get inside parameters directory
cd "$HOME/ardu-sim/parameters/" || exit 1

# get parameter file
wget https://raw.githubusercontent.com/ArduPilot/ardupilot/master/Tools/autotest/default_params/copter.parm

# get inside simulation directory
cd "$HOME/ardu-sim/" || exit 1

# create shell script
echo -e "#!/bin/bash" >> ardu-sim.sh
echo -e "screen -S vehicle -d -m bash -c \"./arducopter -w -S --model + --speedup 1 --defaults parameters/copter.parm -I0\"" >> ardu-sim.sh
echo -e "screen -S proxy -d -m bash -c \"mavproxy.py --master tcp:127.0.0.1:5760 --out 127.0.0.1:14550\"" >> ardu-sim.sh

# make the shell script executable
sudo chmod +x ardu-sim.sh
