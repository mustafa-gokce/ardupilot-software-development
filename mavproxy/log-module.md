# Log Module in MAVProxy
1. Connect to the vehicle using: `mavproxy.py --master=127.0.0.1:14550`
2. Load the module using: `module load log`
3. Display help screen: `log help`
4. List on-board data flash logs: `log list`
5. Download logs: `log download X Y` where `X` is the log index and `Y` is the filename to be saved as *.bin.
6. Erase on-board logs: `log erase`
7. Resume log downloading: `log resume`
8. Show log download status: `log status`
9. Abort downloading logs: `log cancel`

[Source](https://ardupilot.org/mavproxy/docs/modules/log.html)