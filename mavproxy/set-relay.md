# Set Relay using MAVProxy

1. To open the first relay: `relay set 1 1`.
2. To close the first relay: `relay set 1 0`.
3. To create a cycle: `relay repeat 1 COUNT PERIOD`
4. Since there is no physical device to test relay on SITL, there is a special parameter called `SIM_PIN_MASK`.