# Setting up the build environment in Linux

1. Update and upgrade software packages.

`sudo apt-get update && sudo apt-get upgrade`

2. Install git to the computer.

`sudo apt-get install git gitk git-gui`

3. Configure git to use HTTPS instead of git.

`git config --global url."https://github.com/".insteadOf git@github.com:`

`git config --global url."https://".insteadOf git://`

4. Clone the ardupilot repository from github.

`cd && git clone https://github.com/ArduPilot/ardupilot.git`

5. Perform submodule updates.

`cd ardupilot/`

`git submodule update --init --recursive`

6. Install required packages.

`Tools/environment_install/install-prereqs-ubuntu.sh -y`

7. Update profile.

`. ~/.profile`

[Source](https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux)