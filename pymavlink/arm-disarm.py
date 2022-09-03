"""
    Source: https://mavlink.io/en/messages/common.html#SYS_STATUS
            https://mavlink.io/en/messages/common.html#HEARTBEAT
            https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM
            https://mavlink.io/en/messages/common.html#COMMAND_ACK

    onboard_control_sensors_health of SYS_STATUS message contains pre-arm status bit as MAV_SYS_STATUS_PREARM_CHECK
    base_mode of HEARTBEAT message contain armed status bit as MAV_MODE_FLAG_SAFETY_ARMED
    MAV_CMD_COMPONENT_ARM_DISARM can be sent with COMMAND_LONG to arm the vehicle
    If COMMAND_ACK has MAV_CMD_COMPONENT_ARM_DISARM in command and MAV_RESULT_ACCEPTED in result, armed or disarmed
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# arm disarm definitions
VEHICLE_ARM = 1
VEHICLE_DISARM = 0

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# vehicle arm message
vehicle_arm_message = dialect.MAVLink_command_long_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    command=dialect.MAV_CMD_COMPONENT_ARM_DISARM,
    confirmation=0,
    param1=VEHICLE_ARM,
    param2=0,
    param3=0,
    param4=0,
    param5=0,
    param6=0,
    param7=0
)

# vehicle disarm message
vehicle_disarm_message = dialect.MAVLink_command_long_message(
    target_system=vehicle.target_system,
    target_component=vehicle.target_component,
    command=dialect.MAV_CMD_COMPONENT_ARM_DISARM,
    confirmation=0,
    param1=VEHICLE_DISARM,
    param2=0,
    param3=0,
    param4=0,
    param5=0,
    param6=0,
    param7=0
)

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# check the pre-arm
while True:

    # observe the SYS_STATUS messages
    message = vehicle.recv_match(type=dialect.MAVLink_sys_status_message.msgname, blocking=True)

    # convert to dictionary
    message = message.to_dict()

    # get sensor health
    onboard_control_sensors_health = message["onboard_control_sensors_health"]

    # get pre-arm healthy bit
    prearm_status_bit = onboard_control_sensors_health & dialect.MAV_SYS_STATUS_PREARM_CHECK
    prearm_status = prearm_status_bit == dialect.MAV_SYS_STATUS_PREARM_CHECK

    # check prearm
    if prearm_status:

        # vehicle can be armable
        print("Vehicle is armable")

        # break the prearm check loop
        break


# do below always
while True:

    # arm the vehicle
    print("Vehicle is arming...")

    # send arm message
    vehicle.mav.send(vehicle_arm_message)

    # wait COMMAND_ACK message
    message = vehicle.recv_match(type=dialect.MAVLink_command_ack_message.msgname, blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # check if the vehicle is armed
    if message["result"] == dialect.MAV_RESULT_ACCEPTED and message["command"] == dialect.MAV_CMD_COMPONENT_ARM_DISARM:

        # print that vehicle is armed
        print("Vehicle is armed!")

    else:

        # print that vehicle is not armed
        print("Vehicle is not armed!")

    # wait some time
    time.sleep(10)

    # disarm the vehicle
    print("Vehicle is disarming...")

    # send disarm message
    vehicle.mav.send(vehicle_disarm_message)

    # check if the vehicle is disarmed
    if message["result"] == dialect.MAV_RESULT_ACCEPTED and message["command"] == dialect.MAV_CMD_COMPONENT_ARM_DISARM:

        # print that vehicle is disarmed
        print("Vehicle is disarmed!")

    else:

        # print that vehicle is not disarmed
        print("Vehicle is not disarmed!")

    # wait some time
    time.sleep(10)

"""
# do below always
while True:

    # arm the vehicle
    print("Vehicle is arming...")

    # send arm message
    vehicle.mav.send(vehicle_arm_message)

    # wait until vehicle is armed
    while True:

        # catch a heartbeat message
        message = vehicle.recv_match(type=dialect.MAVLink_heartbeat_message.msgname, blocking=True)

        # convert message to dictionary
        message = message.to_dict()

        # get base mode
        base_mode = message["base_mode"]

        # get armed status
        armed_bit = base_mode & dialect.MAV_MODE_FLAG_SAFETY_ARMED
        arm_status = armed_bit == dialect.MAV_MODE_FLAG_SAFETY_ARMED

        # check armed status
        if arm_status:

            # vehicle is armed, exit from infinite loop
            break

    # print arm status
    print("Vehicle is armed!")

    # wait some time
    time.sleep(10)

    # disarm the vehicle
    print("Vehicle is disarming...")

    # send disarm message
    vehicle.mav.send(vehicle_disarm_message)

    # wait until vehicle is disarmed
    while True:

        # catch a heartbeat message
        message = vehicle.recv_match(type=dialect.MAVLink_heartbeat_message.msgname, blocking=True)

        # convert message to dictionary
        message = message.to_dict()

        # get base mode
        base_mode = message["base_mode"]

        # get armed status
        armed_bit = base_mode & dialect.MAV_MODE_FLAG_SAFETY_ARMED
        arm_status = armed_bit == dialect.MAV_MODE_FLAG_SAFETY_ARMED

        # check armed status
        if not arm_status:

            # vehicle is disarmed, exit from infinite loop
            break

    # print arm status
    print("Vehicle is disarmed!")

    # wait some time
    time.sleep(10)
"""
