# Telemetry forwarding
To forward telemetry stream using MAVProxy:

`mavproxy.py --master=X --out=Y` where X is source (your vehicle) and Y is the destination.

1. Connection addresses could be one of the followings:
   1. `/dev/ttyUSBX` for Linux and `COMX` for Windows serial connections.
   2. `tcp:IP:PORT` for local TCP connections.
   3. `udp:IP:PORT` or just `IP:PORT` for local UDP connections.
   4. `tcpout:IP:PORT` for remote TCP connections.
   5. `udpout:IP:PORT` for remote UDP connections.
2. If connection is a serial connection, baud rate can be specified as:
   1. `--baudrate=X` or 
   2. `--master=Y,X`, `--out=Y,X` where X is the baud rate.
3. Always use UDP connection for your telemetry streams for continuity, low latency and ease of use.
4. Deal with the redundancy and guaranteed message delivery on your application.
5. More than one master source (of the same vehicle) and/or output stream can be defined.

[Source](https://ardupilot.org/mavproxy/docs/getting_started/forwarding.html)