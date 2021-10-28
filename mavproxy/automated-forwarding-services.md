# Automated forwarding services

1. Install screen and nano packages from terminal.

`sudo apt-get install screen nano`

2. Install MAVProxy to the root user.

`sudo python3 -m pip install MAVProxy`

4. To forward telemetry stream using MAVProxy:

`mavproxy.py --master=X --out=Y` where X is source (your vehicle) and Y is the destination.

3. Run `sudo nano ~/startup.sh`.

4. Add the following:

```
#!/bin/bash
export LOCALAPPDATA="LOCALAPPDATA"
screen -L -Logfile vehicle_proxy.log -S vehicle_proxy -d -m bash -c "mavproxy.py --force-connected --master=127.0.0.1:14550 --out=127.0.0.1:10000 --out=127.0.0.1:20000 --daemon"
```
6. To explain above command:
   1. `-L` log the screen session.
   2. `-Logfile file_name.ext` specify the log file name with extension.
   3. `-S screen_name` specify the session name. It makes easier to resume session like `screen -r screen_name`.
   4. `-d` used to start the screen session as detached.
   5. `-m executable_name -c "commands"` used to run an executable with arguments.

7. Save the script by pressing Ctrl+X, y and ENTER.

8. Give permissions to the script.

`sudo chmod +x ~/startup.sh`

9. Run the following and copy the path:

`echo $(pwd)"/startup.sh"`

10. To run a command at start up:
    1. Run `sudo nano /etc/rc.local`.
    2. Paste your copied text before `exit 0` like the following:

`sh /home/m/startup.sh &`

where `/home/m/startup.sh` is my copied full path for example.

11. This is my complete `rc.local` script:
```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
sh /home/m/startup.sh &
exit 0
```
12. Save the script by pressing Ctrl+X, y and ENTER.
13. Make the `rc.local` executable:
`sudo chmod +x /etc/rc.local`
14. Enable the service using `sudo systemctl enable rc-local.service`.
15. Start the service using `sudo systemctl start rc-local.service` or `reboot`.
16. Monitor the service using `sudo systemctl status rc-local.service`.
17. After this operation, if you don't want to start this script to start every boot, put `#` before `sh /home/m/startup.sh &`. So the `rc.local` will be:
```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
# sh /home/m/startup.sh &
exit 0
```

[Source](https://ardupilot.org/mavproxy/docs/getting_started/forwarding.html)