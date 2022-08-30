"""
    Fence can be enabled or disabled during flight using MAV_CMD_DO_FENCE_ENABLE as COMMAND_LONG
    0: DISABLE
    1: ENABLE
    2: DISABLE_FLOOR_ONLY

    https://mavlink.io/en/messages/common.html#COMMAND_LONG
    https://mavlink.io/en/messages/common.html#MAV_CMD_DO_FENCE_ENABLE

    Content of fence.txt

-35.363152	149.164795
-35.361019	149.161057
-35.360817	149.168533
-35.365364	149.168686
-35.365486	149.160919
-35.363792	149.160919
-35.363747	149.163574
-35.362366	149.163666
-35.362286	149.161011
-35.361019	149.161057
"""

import sys
import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# fence enable definition
fence_enable_definition = {"DISABLE": 0,
                           "ENABLE": 1,
                           "DISABLE_FLOOR_ONLY": 2}

# get the first argument
fence_enable = sys.argv[1].upper()

if fence_enable in fence_enable_definition.keys():
    print("Sending FENCE {0} to the vehicle".format(fence_enable))
else:
    print("Not supported operation")
    sys.exit()

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# create the message
message = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_FENCE_ENABLE,
                                               confirmation=0,
                                               param1=fence_enable_definition[fence_enable],
                                               param2=0,
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)

# send the message to the vehicle
vehicle.mav.send(message)
