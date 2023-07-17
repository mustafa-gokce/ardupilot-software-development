-- Description: This script gets and sets the home position.

-- define global variables
local MAV_SEVERITY_DEBUG = 7
local LOOP_DELAY_IN_MS = 1000

-- get and set home position
function get_set_home()

    -- check if home position is set
    if not ahrs:home_is_set() then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Home position is not set yet.")
        return get_set_home, LOOP_DELAY_IN_MS
    end

    -- get home position
    local home_position = ahrs:get_home()

    -- get home position coordinates
    local home_latitude = home_position:lat() * 1e-7
    local home_longitude = home_position:lng() * 1e-7
    local home_altitude = home_position:alt() * 1e-2

    -- log home position
    gcs:send_text(MAV_SEVERITY_DEBUG, "Home position: latitude = " .. home_latitude .. ", longitude = " .. home_longitude .. ", altitude = " .. home_altitude)

    -- create new home position
    local new_home_position = Location()
    new_home_position:lat(-353612754)
    new_home_position:lng(1491611647)
    new_home_position:alt(58621)

    -- set home position
    if ahrs:set_home(new_home_position) then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Home position is set.")
    else
        gcs:send_text(MAV_SEVERITY_DEBUG, "Home position is not set.")
    end

    -- schedule the next call to this function
    return get_set_home, LOOP_DELAY_IN_MS
end

-- start the script
return get_set_home()
