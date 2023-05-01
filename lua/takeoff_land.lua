-- ahrs:get_location() is used to get the current current location
-- location:change_alt_frame(frame_type) is used to change the altitude frame of the location
-- arming:pre_arm_checks() is used to check if vehicle is armable
-- arming:is_armed() is used to check the arm status
-- arming:arm() is used to arm the vehicle
-- arming:disarm() is used to disarm the vehicle
-- vehicle:get_mode() returns the mode of the vehicle as a number
-- vehicle:set_mode(mode) sets the mode of the vehicle where mode is a number
-- vehicle:start_takeoff(altitude) used to take off the vehicle to some altitude

-- mode enumerations
local COPTER_MODES = { [0] = "STABILIZE", [4] = "GUIDED", [9] = "LAND" }
local COPTER_MODE_GUIDED = 4
local COPTER_MODE_LAND = 9
local ALT_FRAME_ABOVE_HOME = 1
local TAKEOFF_ALTITUDE = 30
local TAKEOFF_DECISION_ALTITUDE = 5
local ALTITUDE_DECISION_PRECISION = 1

-- helper variables
local takeoff_before = false

-- take off and land the vehicle
function takeoff_land()

    -- get the location of the vehicle
    local current_location = ahrs:get_location()

    -- do not proceed if there is not valid location estimation
    if not current_location then
        return takeoff_land, 1000
    end

    -- get altitude above home
    if not current_location:change_alt_frame(ALT_FRAME_ABOVE_HOME) then
        return takeoff_land, 1000
    end
    local current_altitude = current_location:alt() * 1e-2

    -- get armable, armed, mode and altitude
    local is_armable = arming:pre_arm_checks()
    local is_armed = arming:is_armed()
    local mode_number = vehicle:get_mode()
    local mode_name = COPTER_MODES[mode_number]

    -- dummy message
    gcs:send_text(7, string.format("Armable: %s Armed: %s Mode: %s Altitude: %0.2f", is_armable, is_armed, mode_name, current_altitude))

    -- check takeoff before
    if not takeoff_before then

        -- set the mode to GUIDED
        if mode_number ~= COPTER_MODE_GUIDED then
            vehicle:set_mode(COPTER_MODE_GUIDED)
        end

        -- arm the vehicle
        if not is_armed and is_armable then
            arming:arm()
        end

        -- takeoff the vehicle
        if current_altitude < TAKEOFF_DECISION_ALTITUDE then
            vehicle:start_takeoff(TAKEOFF_ALTITUDE)
        end

        -- check takeoff successful
        if TAKEOFF_ALTITUDE - current_altitude < ALTITUDE_DECISION_PRECISION then
            takeoff_before = true
        end

    -- takeoff before
    else

        -- set the mode to LAND
        if mode_number ~= COPTER_MODE_LAND then
            vehicle:set_mode(COPTER_MODE_LAND)
        end
    end

    -- schedule the next call to this function
    return takeoff_land, 1000
end

-- start the script
return takeoff_land()
