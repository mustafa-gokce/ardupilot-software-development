# Quickstart
To start the MAVProxy:

`mavproxy.py --master=X --console --map` where X is the connection string to your vehicle.

1. `--master=X` specifies connection address to your vehicle. It could be one of the followings:
   1. `/dev/ttyUSBX` for Linux and `COMX` for Windows serial connections.
   2. `tcp:IP:PORT` for local TCP connections.
   3. `udp:IP:PORT` or just `IP:PORT` for local UDP connections.
   4. `tcpout:IP:PORT` for remote TCP connections.
   5. `udpout:IP:PORT` for remote UDP connections.
2. If master is a serial connection, baud rate can be specified as:
   1. `--baudrate=X` or 
   2. `--master=Y,X` where X is the baud rate.
3. `--console` opens the MAVProxy ground control station Console.
4. `--map` opens the interactive map interface.

[Source](https://ardupilot.org/mavproxy/docs/getting_started/quickstart.html)