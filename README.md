# Software Development for Ardupilot Powered Unmanned Systems

Source codes of Software Development for Ardupilot Powered Unmanned Systems course.

## Setting up the build and simulation environment

This section includes how to install the build environment and simulation software from Ardupilot source code and running the simulation with different vehicles for software development.

1. [Introduction]()
   
2. [Quickstart](environment-setup/quickstart.md)

3. [Setting up the build environment](environment-setup/build-environment-setup.md)

4. [Setting up the simulation software](environment-setup/simulation-software-setup.md)

5. [Starting the simulation software individually](environment-setup/simulation-software-individually.md)

6. [Creating simulation environment starter shell script](environment-setup/simulation-starter-script.md)

## MAVProxy command line ground control station

This section includes use cases of MAVProxy command line ground control station and shell scripting.

7. [Introduction]()

8. [Installing instructions](mavproxy/installing-mavproxy.md)

9. [Quickstart](mavproxy/mavproxy-quickstart.md)

10. [Startup options](mavproxy/mavproxy-startup-options.md)

11. [Telemetry forwarding](mavproxy/telemetry-forwarding.md)

12. [Creating MAVProxy shell scripts for automated proxy and forwarding services](mavproxy/automated-forwarding-services.md)

13. [Arming and disarming the vehicle](mavproxy/arm-disarm.md)

14. [Mission editing](mavproxy/mission-editing.md)

15. [Geofencing](mavproxy/geofencing.md)

16. [Rally point operations](mavproxy/rally-points.md)

17. [Changing the flight mode of the vehicle](mavproxy/flight-mode.md)

18. ["command_int" Command](mavproxy/command-int.md)

19. [System commands](mavproxy/system-commands.md)

20. [Log management](mavproxy/log-module.md)

21. [Graphing live data from the vehicle](mavproxy/graph-module.md)

22. [Horizon module](mavproxy/horizon-module.md)

23. [Link management](mavproxy/link-management.md)

24. ["long" command](mavproxy/command-long.md)

25. [Map module](mavproxy/map-module.md)

26. ["position" command](mavproxy/command-position.md)

27. [Polygon fence](mavproxy/geofencing.md)

28. [Set servo](mavproxy/set-servo.md)

29. [Set relay](mavproxy/set-relay.md)

30. [Sensor reporting](mavproxy/sensors-module.md)

31. [Text-to-speech module](mavproxy/speech-module.md)

32. [Time sync](mavproxy/time-sync.md)

33. [Terrain data handling](mavproxy/terrain-module.md)

## Software development with Python using Dronekit library

This section includes how to control and monitor the vehicle states in Python programming language using Dronekit library

34. [Introduction]()

35. [Installing instructions](dronekit/installing-dronekit.md)

36. [Connecting to the vehicle](dronekit/vehicle-connection.py)

37. [Getting the vehicle states](dronekit/getting-vehicle-states.py)

38. [Setting the vehicle states](dronekit/setting-vehicle-states.py)

39. [Creating vehicle state observers](dronekit/vehicle-state-observers.py)

40. [Getting and setting vehicle parameters](dronekit/get-set-parameters.py)

41. [Taking off and landing the vehicle](dronekit/takeoff-land.py)

42. [Flying the vehicle to a location](dronekit/go-to-location.py)

43. [Dealing with the autonomous missions](dronekit/mission-editing.py)

44. [Calibrating the vehicle](dronekit/vehicle-calibrations.py)

## Software development with Python using PyMAVLink library

This section includes how to control and monitor the vehicle states in Python programming language using PyMAVLink library.

45. [MAVLink messaging protocol basics]()

46. [Introduction]()

47. [Installing instructions](pymavlink/installing-pymavlink.md)

48. [Connecting to the vehicle](pymavlink/vehicle-connection.py)

49. [Receiving messages from vehicle](pymavlink/receive-message.py)

50. [Sending messages to vehicle](pymavlink/send-message.py)

51. [Sending message stream requests to vehicle](pymavlink/request-stream.py)

52. [Getting and setting vehicle parameters](pymavlink/get-set-parameter.py)

53. [Sending message requests to vehicle](pymavlink/request-message.py)

54. [Arming and disarming the vehicle](pymavlink/arm-disarm.py)

55. [Changing the flight mode of the vehicle](pymavlink/change-mode.py)

56. [Taking off and landing the vehicle](pymavlink/takeoff-land.py)

57. [Flying the vehicle to a location](pymavlink/goto-location.py)

58. [Change current mission in auto flight mode](pymavlink/set-current.py)

59. [Set servo](pymavlink/set-servo.py)

60. [Set relay](pymavlink/set-relay.py)

61. [Request and receive auto mode flight plan from vehicle](pymavlink/get-mission.py)

62. [Create and send auto mode flight plan to vehicle](pymavlink/set-mission.py)

63. [Sending partial mission item list to vehicle](pymavlink/set-mission-partial.py)

64. [Clear mission item list on vehicle](pymavlink/clear-mission.py)

65. [Request and receive fence from vehicle](pymavlink/get-fence.py)

66. [Create and send fence to vehicle](pymavlink/set-fence.py)

67. [Enable and disable fence](pymavlink/fence-enable.py)

68. [Request and receive rally points from vehicle](pymavlink/get-rally.py)

69. [Create and send rally points to vehicle](pymavlink/set-rally.py)

70. [RC override](pymavlink/rc-override.py)

71. [Request default message streams](pymavlink/request-defaults.py)

72. [Home distance](pymavlink/distance-home.py)

73. [Set flight speed](pymavlink/set-speed.py)

74. [Set yaw](pymavlink/set-yaw.py)

75. [Pause/resume an autonomous flight](pymavlink/pause-resume.py)

76. [Reading RC inputs and servo outputs](pymavlink/rc-servo.py)

77. [Getting the vibration data from vehicle]()

78. [Getting and setting the home location of the vehicle](pymavlink/home-get-set.py)

79. [Playing tunes from buzzer]()

80. [Reading distance sensor messages]()

81. [Sending and receiving status texts]()

## On-board software development with LUA programing language

This section includes how to control and monitor the vehicle states of the vehicle by on-board using LUA programing language.

82. [Introduction](lua/intro.md)

83. [Sample script](lua/sample_script.lua)

84. [Arming and disarming the vehicle](lua/arm_disarm.lua)

85. [Vector data type]()

86. [Getting attitude and position data of the vehicle]()

87. [Location data type]()

88. [Getting battery data of the vehicle]()

89. [Getting GPS data of the vehicle]()

90. [Send text message to ground control station]()

91. [Controlling serial LEDs]()

92. [Playing tunes from buzzer]()

93. [Getting and setting vehicle flight mode]()

94. [Getting flying information from vehicle]()

95. [Taking off and landing the vehicle]()

96. [Flying the vehicle to a location]()

97. [Getting terrain data from vehicle]()

98. [Relay operations]()

99. [Servo channel operations]()

100. [Getting RC input PWM values]()

101. [Serial communications]()

102. [Getting barometer data]()

103. [Getting and setting vehicle parameters]()

104. [Getting button state]()

## Course documents

Documents and information about this course.

105. [Disclaimer](course-documents/disclaimer.md)
