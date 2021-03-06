# Software Development for Ardupilot Powered Unmanned Systems

Source codes of Software Development for Ardupilot Powered Unmanned Systems course.

## Setting up the build and simulation environment

This section includes how to install the build environment and simulation software from Ardupilot source code and running the simulation with different vehicles for software development.

1. [Introduction]()
   
2. [Setting up the build environment](environment-setup/build-environment-setup.md)

3. [Setting up the simulation software](environment-setup/simulation-software-setup.md)

4. [Starting the simulation software individually](environment-setup/simulation-software-individually.md)

5. [Creating simulation environment starter shell script](environment-setup/simulation-starter-script.md)

6. [Advanced simulation software use cases]()

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

27. [RC calibration]()

28. [Relay management]()

29. [Motor test]()

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

51. [Sending message stream requests to vehicle]()

52. [Getting and setting vehicle parameters](pymavlink/get-set-parameter.py)

53. [Listening message streams from vehicle]()

54. [Arming and disarming the vehicle](pymavlink/arm-disarm.py)

55. [Changing the flight mode of the vehicle](pymavlink/change-mode.py)

56. [Taking off and landing the vehicle](pymavlink/takeoff-land.py)

57. [Flying the vehicle to a location](pymavlink/goto-location.py)

58. [Dealing with the autonomous missions]()

59. [Calibrating the vehicle]()

60. [Sending system time messages to vehicle]()

61. [Sending heartbeat messages to vehicle]()

62. [Sending and receiving mission items]()

63. [Sending and receiving partial mission item lists]()

64. [Requesting a specific message from vehicle]()

65. [Autonomous mission command item types]()

66. [Diagnosing system health with system status messages]()

67. [Reading attitude of the vehicle]()

68. [Reading position of the vehicle]()

69. [Reading HUD Messages]()

70. [Reading RC channel values]()

71. [Reading servo output channel values]()

72. [Changing and reading current mission item]()

73. [Reading terrain data from vehicle]()

74. [Reading the autopilot version message]()

75. [Reading wind estimating messages from vehicle]()

76. [Dealing with the high latency messages]()

77. [Getting the vibration data from vehicle]()

78. [Getting and setting the home location of the vehicle]()

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
