# Startup Options
1. `--master:X` specifies connection address to your vehicle. It could be one of the followings:
   1. `/dev/ttyUSBX` for Linux and `COMX` for Windows serial connections.
   2. `tcp:IP:PORT` for local TCP connections.
   3. `udp:IP:PORT` or just `IP:PORT` for local UDP connections.
   4. `tcpout:IP:PORT` for remote TCP connections.
   5. `udpout:IP:PORT` for remote UDP connections.
   6. Multiple master connection can be defined to the same vehicle for redundant data links.
2. If master is a serial connection, baud rate can be specified as:
   1. `--baudrate=X` or 
   2. `--master=Y,X` where X is the baud rate.
3. `--console` opens the MAVProxy ground control station Console.
4. `--map` opens the interactive map interface.
5. `--quadcopter` is used for quadcopter controls.
6. `--out` is used to forward the MAVLink packets to a remote device (serial, USB or network address/port). Useful if using multiple ground station computers or relaying the stream through an intermediate node.
   1. `/dev/ttyUSBX` for Linux and `COMX` for Windows serial connections.
   2. `tcp:IP:PORT` for local TCP connections.
   3. `udp:IP:PORT` or just `IP:PORT` for local UDP connections.
   4. `tcpout:IP:PORT` for remote TCP connections.
   5. `udpout:IP:PORT` for remote UDP connections.
   6. Multiple stream outputs can be defined.
7. `--sitl` is used to host and port to send simulated RC input for the Software in the loop (SITL) simulator. 
   1. Usually `--sitl=127.0.0.1:5501`.
8. `--streamrate` is used to configure the stream rate of the connection.
9. `--source-system` defines system ID of this GCS.
10. `--source-component` defines component ID of this GCS.
11. `--target-system` defines target master system ID.
12. `--target-component` defines target master component ID.
13. `--logfile` defines the master logfile name.
14. `--append-log` used to append new logs to the older one.
15. `--nodtr` disables DTR drop on close.
16. `--show-errors` used to show MAVLink error messages.
17. `--speech` enables text to speech.
18. `--aircraft` name of the aircraft being flown. If used, logfiles will be stored in `/Logs/AircraftName/Date/flightNumber/flight.tlog`. 
19. `--cmd` initial commands to run in MAVProxy and delimited by `;`.
20. `--load-module` loads a desired MAVProxy module on startup.
21. `--mavversion` specifies the MAVLink version.
22. `--auto-protocol` used to auto detect MAVLink protocol version.
23. `--continue` continue to the logs.
24. `--nowait` used for not waiting a heartbeat message at startup.
25. `--dialect` used to specify MAVLink dialect. Uses the APM dialect by default.
26. `--rtscts` used for RTS/CTS hardware flow control of master connection.
27. `--mission` used to give the current mission a name. If used, the flight log will be stored as `/Logs/aircraftname/missionname` rather than the default `/Logs/aircraftname/currentdatetime`.
28. `--daemon` used to start MAVProxy in daemon mode (as a background process). No interactive shell will be started.
29. `--state-basedir` defines the base directory that logs will be stored, if it is not the current directory.
30. `--version` show current MAVProxy version.
31. `--moddebug` is debugging messages level. Default is 0 (no debug output). A value of 3 is useful for debugging crashes or errors in MAVProxy and its modules.
32. `--default-modules` is a comma separated list of the modules to load on startup by default.
33. `--non-interactive` is used for not starting interactive shell.
34. `--force-connected` is used for using master even if initial connection fails.

[Source](https://ardupilot.org/mavproxy/docs/getting_started/starting.html)