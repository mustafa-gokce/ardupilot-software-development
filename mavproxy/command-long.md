# "long" command in MAVProxy
1. Long command enables user to send [MAV_CMD_*](https://mavlink.io/en/messages/common.html#mav_commands) commands to vehicle.
2. It is used to send [COMMAND_LONG](https://mavlink.io/en/messages/common.html#COMMAND_LONG) messages to the vehicle to
give commands during flight.
3. All the parameters are in float.
4. It uses [command](https://mavlink.io/en/services/command.html) service of the MAVLink.
5. Usage is: `long COMMAND_NAME PARAM1 PARAM2 PARAM3 PARAM4 PARAM5 PARAM6 PARAM7`
6. Lets takeoff in guided mode using [MAV_CMD_NAV_TAKEOFF](https://mavlink.io/en/messages/common.html#MAV_CMD_NAV_TAKEOFF):
   1. `long MAV_CMD_NAV_TAKEOFF 0 0 0 0 0 0 10`
   2. This command needs takeoff altitude in meters as its 7th parameter.
7. Not all the commands are supported in `COMMAND_LONG` form but will be implemented and supported near future.

[Source](https://mavlink.io/en/messages/common.html#COMMAND_LONG)