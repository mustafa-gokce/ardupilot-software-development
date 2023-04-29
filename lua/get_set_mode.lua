-- Description: This script gets and sets the flight mode of the vehicle
-- Copter modes: https://mavlink.io/en/messages/ardupilotmega.html#COPTER_MODE
-- Plane modes: https://mavlink.io/en/messages/ardupilotmega.html#PLANE_MODE
-- Rover modes: https://mavlink.io/en/messages/ardupilotmega.html#ROVER_MODE
-- Sub modes: https://mavlink.io/en/messages/ardupilotmega.html#SUB_MODE
-- vehicle:get_mode() returns the mode of the vehicle as a number
-- vehicle:set_mode(mode) sets the mode of the vehicle where mode is a number

-- mode enumerations
local COPTER_MODES = { [0] = "STABILIZE", [1] = "ACRO", [2] = "ALT_HOLD",
                       [3] = "AUTO", [4] = "GUIDED", [5] = "LOITER",
                       [6] = "RTL", [7] = "CIRCLE", [9] = "LAND",
                       [11] = "DRIFT", [13] = "SPORT", [14] = "FLIP",
                       [15] = "AUTOTUNE", [16] = "POSHOLD", [17] = "BRAKE",
                       [18] = "THROW", [19] = "AVOID_ADSB", [20] = "GUIDED_NOGPS",
                       [21] = "SMART_RTL", [22] = "FLOWHOLD", [23] = "FOLLOW",
                       [24] = "ZIGZAG", [25] = "SYSTEMID", [26] = "AUTOROTATE",
                       [27] = "AUTO_RTL" }
local COPTER_MODE_GUIDED = 4
local COPTER_MODE_LAND = 9

-- get and set mode of the vehicle
function get_set_mode()

    -- get current flight mode number
    local flight_mode = vehicle:get_mode()

    -- periodically change the flight mode
    if flight_mode == COPTER_MODE_GUIDED then
        vehicle:set_mode(COPTER_MODE_LAND)
    elseif flight_mode == COPTER_MODE_LAND then
        vehicle:set_mode(COPTER_MODE_GUIDED)
    end

    -- send current flight mode to GCS
    gcs:send_text(7, "Flight mode: " .. COPTER_MODES[flight_mode])

    -- schedule the next call to this function
    return get_set_mode, 1000
end

-- start the script
return get_set_mode()
