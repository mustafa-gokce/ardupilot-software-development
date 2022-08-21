"""
    Since no physical device to test relay on SITL, there is a parameter called SIM_PIN_MASK
    Each bit of this parameter is logical input/output state for individual channels
    In SITL, these channels are different from servo outputs
    Before doing relay operations, make sure to set RELAY_PINx (up to 6) to an appropriate value
    For example, `RELAY_PIN = 0` means that:
        Changing the value of first relay instance will change the 0th bit of the SIM_PIN_MASK
        Setting the first relay to on will result to SIM_PIN_MASK = 1 (= 1 * 2^0)
        Setting the first relay to off will result to SIM_PIN_MASK = 0 (= 0 * 2^0)
    In real world, must set RELAY_PINx to an appropriate value as in the documentation

    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_RELAY
    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_REPEAT_RELAY
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
# create set relay command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_SET_RELAY,
                                               confirmation=0,
                                               param1=2,  # relay pin instance number, starts from 0, 0 = first relay
                                               param2=0,  # 1 = ON, 0 = OFF
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send command to the vehicle
vehicle.mav.send(command)
"""

# create repeat relay command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_REPEAT_RELAY,
                                               confirmation=0,
                                               param1=0,  # relay pin instance number, starts from 0, 0 = first relay
                                               param2=3,  # cycle count
                                               param3=10,  # cycle period
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send command to the vehicle
vehicle.mav.send(command)
