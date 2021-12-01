# "command_int" command in MAVProxy
1. Int command enables user to send [MAV_CMD_*](https://mavlink.io/en/messages/common.html#mav_commands) commands to vehicle.
2. It is used to send [COMMAND_INT](https://mavlink.io/en/messages/common.html#COMMAND_INT) messages to the vehicle to
give commands during flight.
3. It uses [command](https://mavlink.io/en/services/command.html) service of the MAVLink.
4. Usage is: `command_int FRAME_TYPE COMMAND_NAME CURRENT AUTOCONTINUE PARAM1 PARAM2 PARAM3 PARAM4 X Y Z`
5. [Frame type](https://mavlink.io/en/messages/common.html#MAV_FRAME) and [command name](https://mavlink.io/en/messages/common.html#mav_commands) 
must be specified.
6. PARAM1-4 and Z are float, X and Y are int32.
7. Lets fly to a location in guided mode using [MAV_CMD_DO_REPOSITION](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_REPOSITION):
   1. `command_int MAV_FRAME_GLOBAL_RELATIVE_ALT_INT MAV_CMD_DO_REPOSITION 0 0 0 0 0 0 -353613322 1491611469 10`
   2. This command needs altitude in meters as its 7th parameter.
   3. 5th, 6th parameters are latitude, longitude and they must be integers (lat\*1e7, lon\*1e7)
8. Not all the commands are supported in `COMMAND_INT` form but will be implemented and supported near future.

[Source](https://mavlink.io/en/messages/common.html#COMMAND_INT)