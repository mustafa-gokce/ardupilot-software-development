"""
    You can use MAVLink for communicating between processes.
    You don't even need an autopilot or a proxy server (e.g. MAVProxy) for that.

    One process should act as a "MASTER" and another one is "SLAVE".
    "MASTER" process should create a MAVLink connection with "udpout or tcpin".
    "SLAVE" process should create a MAVLink connection with "udpin or tcp".
    The communication is bidirectional.
    You can also use serial devices for interprocess communication, too.

    Master: python3 send-receive.py master
    Slave: python3 send-receive.py slave

    https://mavlink.io/en/messages/common.html#HEARTBEAT
    https://ardupilot.org/mavproxy/docs/getting_started/starting.html#master
    https://ardupilot.org/mavproxy/docs/getting_started/starting.html#out
"""

import sys
import time
import threading
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect


def send_heartbeat(master):
    while True:
        heartbeat = dialect.MAVLink_heartbeat_message(type=dialect.MAV_TYPE_ONBOARD_CONTROLLER,
                                                      autopilot=dialect.MAV_AUTOPILOT_INVALID,
                                                      base_mode=0,
                                                      custom_mode=0,
                                                      system_status=dialect.MAV_STATE_ACTIVE,
                                                      mavlink_version=3)
        master.mav.send(heartbeat)
        time.sleep(1)


# helper variables
MASTER = "master"
SLAVE = "slave"

# get the argument
argument = sys.argv[1]

# check the argument is master
if argument == MASTER:
    print("This script is running as master")

    # create master MAVLink connection
    master = utility.mavlink_connection(device="udpout:127.0.0.1:6000",
                                        source_system=1,
                                        source_component=1)

    # start heartbeat thread
    threading.Thread(target=send_heartbeat, args=(master,)).start()

    # infinite loop
    while True:

        # receive a message
        message = master.recv_match(type=dialect.MAVLink_named_value_float_message.msgname,
                                    blocking=True)

        # convert this message to dictionary
        message = message.to_dict()

        # show the message
        print("MASTER", message)

        # check the message
        if message["name"] == "REQSR":
            # calculate the result
            result = message["value"] ** 0.5

            # create the message
            message = dialect.MAVLink_named_value_float_message(time_boot_ms=0,
                                                                name="REPSR".encode("utf-8"),
                                                                value=result)

            # send the message
            master.mav.send(message)


# check the argument is slave
elif argument == SLAVE:
    print("This script is running as slave")

    # create slave MAVLink connection
    slave = utility.mavlink_connection(device="udpin:127.0.0.1:6000",
                                       source_system=1,
                                       source_component=2,
                                       force_connected=True)

    # wait heartbeat
    slave.wait_heartbeat()

    # infinite loop
    i = 1
    while True:

        # create the message
        message = dialect.MAVLink_named_value_float_message(time_boot_ms=0,
                                                            name="REQSR".encode("utf-8"),
                                                            value=i)

        # send the message
        slave.mav.send(message)

        # receive a message
        message = slave.recv_match(type=dialect.MAVLink_named_value_float_message.msgname,
                                   blocking=True)

        # convert this message to dictionary
        message = message.to_dict()

        # show the message
        print("SLAVE", message)

        # check the message
        if message["name"] == "REPSR":
            # show the response
            print("Squared root of", i, "is", message["value"])

        # increment the counter
        i += 1

        # sleep a bit
        time.sleep(3)

# raise exception on others
else:
    raise NotImplementedError
