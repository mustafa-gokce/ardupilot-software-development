# Introduction to ArduPilot On-Board Scripting
* ArduPilot lets you run scripts on flight controllers those have at least 2MB of flash and 70kB of memory.
* With scripting, advanced autonomy can be achieved without companion computer.
  * Of course this limited with computational power of the flight controller. 
* The parameter [SCR_ENABLE](https://ardupilot.org/copter/docs/parameters.html#scr-enable) should be 1.
* Scripts are written in LUA programming language and in a form of *.lua files.
* Script files should be located inside `scripts/` folder where the simulation binary located.
* In real world case, script files should be located `APM/scripts/` of the SD card attached to flight controller.
* You can do:
  * Multiple scripts can be run at once.
  * Monitor the vehicle.
  * Control the vehicle.
* Scripts run at low priority in the system.
* If any script crashes:
  * All running scripts will be terminated.
  * The scripting engine will restart.
  * Reload all scripts from the disk.
  * This is allowed to happen at all flight stages, even while the vehicle is armed and flying.
* All the LUA bindings can be found in [LUA Docs](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/libraries/AP_Scripting/docs/docs.lua).
* If the `docs.lua` is in the same directory, some IDEs like PyCharm gives autocompletion and suggestions thanks to `LuaCheck` plugin.

[Source](https://ardupilot.org/copter/docs/common-lua-scripts.html)