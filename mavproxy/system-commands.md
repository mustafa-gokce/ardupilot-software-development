# System Commands in MAVProxy
1. Connect to the vehicle using: `mavproxy.py --master=127.0.0.1:14550`
2. `reboot` command is used to soft restart flight controller.
3. `time` is used to show time on flight controller and computer.
4. `script SCRIPT_FILE_NAME.EXTENSION` is used to run a text file contains MAVProxy commands.
5. `shell` is used to run a shell command.
6. `status` command shows the latest packets.
7. `watch MESSAGE_NAME` is used to watch an updating message.
8. `exit` is used to exit from MAVProxy. `set requireexit True` enables this command.

[Source](https://ardupilot.org/mavproxy/docs/uav_configuration/system.html)