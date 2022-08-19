# Set Relay using MAVProxy

1. To open the first relay: `relay set 0 1`.
2. To close the first relay: `relay set 0 0`.
3. To create a cycle on the first relay: `relay repeat 0 COUNT PERIOD`
4. Since there is no physical device to test relay on SITL, there is a special parameter called `SIM_PIN_MASK`.
5. Each bit of this parameter contains logical input/output state for individual channels (in SITL, these channels are
   different than servo outputs).
6. Before doing relay operations, make sure to set `RELAY_PINx` (up to 6) to an appropriate value.
7. For example, `RELAY_PIN = 0` means that:
   1. Changing the value of first relay instance will change the 0th bit of the `SIM_PIN_MASK`.
   2. `relay set 0 1` will result to `SIM_PIN_MASK = 1`.
   3. `relay set 0 0` will result to `SIM_PIN_MASK = 0`.
8. In real world applications, you need to set `RELAY_PINx` to an appropriate value as stated in the documentation.
