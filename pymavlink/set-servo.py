"""
    Start the simulated vehicle as usual
    Connect to it using MAVProxy with loading graph module like:
        mavproxy.py --master=127.0.0.1:14550 --load-module="graph"
    Make sure that SERVOx_FUNCTION is set to 0
    Select a channel that is not used for flight operations
    Observe the output with:
        graph SERVO_OUTPUT_RAW.servox_raw
    Where x is the selected channel

    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO
    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_REPEAT_SERVO
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

"""
# create set servo command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_SET_SERVO,
                                               confirmation=0,
                                               param1=6,  # servo channel
                                               param2=1900,  # PWM value
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send the command to the vehicle
vehicle.mav.send(command)
"""

# create repeat servo command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_REPEAT_SERVO,
                                               confirmation=0,
                                               param1=6,  # servo channel
                                               param2=1900,  # PWM value
                                               param3=4,  # count
                                               param4=4,  # period
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send the command to the vehicle
vehicle.mav.send(command)
