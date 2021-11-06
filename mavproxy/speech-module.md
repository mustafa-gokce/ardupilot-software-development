# Speech Module in MAVProxy
1. Make sure you have speechd installed in your computer
   1. `sudo apt-get install speech-dispatcher`
2. Edit the file pulse audio defaults
   1. `sudo nano /etc/pulse/default.pa`
   2. Paste `load-module module-udev-detect tsched=0` at the end of the and save the file
   3. Run `systemctl --user restart pulseaudio.service`
   4. Run `systemctl --user restart pulseaudio.socket`
3. Connect to the vehicle using one of the following
   1. `mavproxy.py --master=127.0.0.1:14550 --load-module="speech"`
   2. `mavproxy.py --master=127.0.0.1:14550` and then `module load speech`