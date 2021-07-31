# Installing instructions for MAVProxy

1. Install required packages from terminal.

`sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame`

2. Install Python modules.

`python3 -m pip install PyYAML mavproxy --user`

3. Add path to bashrc.

`echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc`

4. Give permission to connect serial devices.

`sudo usermod -a -G dialout $USER`

## Updating the MAVProxy

1. To update the MAVProxy for using the latest version, run the command.

`python3 -m pip install mavproxy --user --upgrade`

[Source](https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html)