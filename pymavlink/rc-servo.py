"""
    It may be desired to execute certain tasks on a system based on RC channels.
    For example, controlling on-board flight computer software task using an RC transmitter.
    Or you might want to do a certain task based on servo output channels.
    For example, warn user if servo outputs are inconsistent, too high, at certain value, range, etc.
    RC_CHANNELS message contains 18 RC input channels.
    These values can be received from RC transmitter or can be overridden with a MAVLink message.
    SERVO_OUTPUT_RAW message contains 16 output servo channels from autopilot.
    Each channel corresponds a PWM value between 1000-2000 microseconds.

    https://mavlink.io/en/messages/common.html#RC_CHANNELS
    https://mavlink.io/en/messages/common.html#SERVO_OUTPUT_RAW
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect


def task_1():
    print("Running task 1...")


def task_2():
    print("Running task 2...")


# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# infinite loop
while True:

    # capture RC_CHANNELS message
    message = vehicle.recv_match(type=dialect.MAVLink_rc_channels_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # 16th channel's PWM value satisfies to run task task 1
    if 1200 < message["chan16_raw"] < 1500:

        # call task 1
        task_1()

    # 16th channel's PWM value satisfies to run task task 2
    elif 1500 < message["chan16_raw"] < 1700:

        # call task 2
        task_2()

    # invalid 16th channel's PWM value
    else:

        # do nothing
        print("Invalid channel 16 value:", message["chan16_raw"])

"""
# infinite loop
while True:

    # capture SERVO_OUTPUT_RAW message
    message = vehicle.recv_match(type=dialect.MAVLink_servo_output_raw_message.msgname,
                                 blocking=True)

    # convert the message to dictionary
    message = message.to_dict()

    # print the message
    print("Motor 1:", message["servo1_raw"],
          "Motor 2:", message["servo2_raw"],
          "Motor 3:", message["servo3_raw"],
          "Motor 4:", message["servo4_raw"])
"""
