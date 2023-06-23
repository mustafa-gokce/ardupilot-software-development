-- Description: This script will do multi location mission

-- create a location object
---@param lat number
---@param lng number
---@param alt number
---@return Location_ud
function createLocation(lat, lng, alt)
    local location = Location()
    location:relative_alt(true)
    location:lat(math.floor(lat * 1e7))
    location:lng(math.floor(lng * 1e7))
    location:alt(math.floor(alt * 1e2))
    return location
end

-- mode enumerations, helper, constants, configurations
local COPTER_MODES = { [0] = "STABILIZE", [4] = "GUIDED", [6] = "RTL"}
local COPTER_MODE_STABILIZE = 0
local COPTER_MODE_GUIDED = 4
local COPTER_MODE_RTL = 6
local ALT_FRAME_ABOVE_HOME = 1
local TAKEOFF_ALTITUDE = 30
local TARGET_DECISION_DISTANCE = 5
local LOOP_DELAY = 1000
local SEVERITY = 7
local navigation_index = 1

-- target locations
local target_locations = { { -35.36573684, 149.16312254, 30.0 },
                           { -35.36135212, 149.16115359, 45.0 },
                           { -35.36022811, 149.16580334, 20.0 },
                           { -35.36565041, 149.16683329, 35.0 } }

-- multi location mission
function multi_location_mission()

    -- notify user
    gcs:send_text(SEVERITY, "Starting the mission")

    -- call flight mode change step
    return change_flight_mode, LOOP_DELAY
end

-- change flight mode function
function change_flight_mode()

    -- get flight mode
    local mode_number = vehicle:get_mode()
    local mode_name = COPTER_MODES[mode_number]

    -- notify user
    gcs:send_text(SEVERITY, "Flight mode: " .. mode_name)

    -- check the flight mode
    if mode_number ~= COPTER_MODE_GUIDED then
        vehicle:set_mode(COPTER_MODE_GUIDED)
        return change_flight_mode, LOOP_DELAY
    end

    -- get vehicle is flying or not
    local is_flying = vehicle:get_likely_flying()

    -- jump start to do navigation if already flying
    if is_flying then
        gcs:send_text(SEVERITY, "Jump starting to do navigation")
        navigation_index = 1
        return do_navigation(), LOOP_DELAY
    end

    -- call arm vehicle step
    return arm_vehicle, LOOP_DELAY
end

-- arm vehicle function
function arm_vehicle()

    -- get armable and arming status
    local is_armable = arming:pre_arm_checks()
    local is_armed = arming:is_armed()

    -- arm the vehicle
    if not is_armed and is_armable then
        gcs:send_text(SEVERITY, "Arming the vehicle...")
        arming:arm()
    end

    -- call this function again if it is not is_armed
    if not is_armed then
        return arm_vehicle, LOOP_DELAY
    end

    -- notify user
    gcs:send_text(SEVERITY, "Armed the vehicle")

    -- call takeoff vehicle step
    return takeoff_vehicle, LOOP_DELAY
end

-- takeoff the vehicle
function takeoff_vehicle()

    -- get taking off
    local is_taking_off = vehicle:is_taking_off()

    -- takeoff the vehicle
    if not is_taking_off then
        gcs:send_text(SEVERITY, "Trying to take off to " .. TAKEOFF_ALTITUDE .. " meters...")
        vehicle:start_takeoff(TAKEOFF_ALTITUDE)
        return takeoff_vehicle, LOOP_DELAY
    end

    -- notify user
    gcs:send_text(SEVERITY, "Takeoff is successful")

    -- call wait for takeoff step
    return wait_takeoff, LOOP_DELAY
end

-- wait for takeoff
function wait_takeoff()

    -- get taking off
    local is_taking_off = vehicle:is_taking_off()

    -- get the altitude of the vehicle
    local current_location = ahrs:get_location()
    current_location:change_alt_frame(ALT_FRAME_ABOVE_HOME)
    local current_altitude = current_location:alt() * 1e-2

    -- check takeoff is completed
    if is_taking_off then
        gcs:send_text(SEVERITY, "Waiting for altitude: " .. math.floor(current_altitude) .. "/" .. TAKEOFF_ALTITUDE .. " meters...")
        return wait_takeoff, LOOP_DELAY
    end

    -- notify user
    gcs:send_text(SEVERITY, "Takeoff is complete")

    -- call do navigation step
    return do_navigation, LOOP_DELAY
end

-- go to waypoints
function do_navigation()

    -- create target location
    local target_location = createLocation(target_locations[navigation_index][1], target_locations[navigation_index][2], target_locations[navigation_index][3])

    -- go to location
    vehicle:set_target_location(target_location)

    -- get current location of the vehicle
    local current_location = ahrs:get_location()

    -- calculate target distance
    local target_distance = current_location:get_distance(target_location)

    -- notify user
    gcs:send_text(SEVERITY, "Waypoint " .. navigation_index .. " distance: " .. math.floor(target_distance))

    -- check the target distance and increment the navigation index
    if target_distance < TARGET_DECISION_DISTANCE then
        gcs:send_text(SEVERITY, "Reached to waypoint: " .. navigation_index)
        navigation_index = navigation_index + 1
    end

    -- check the end of the navigation
    if navigation_index > #target_locations then
        gcs:send_text(SEVERITY, "Mission is complete")
        return return_to_launch, LOOP_DELAY
    end

    -- call do navigation step
    return do_navigation, LOOP_DELAY
end

-- return to home
function return_to_launch()

    -- get flight mode
    local mode_number = vehicle:get_mode()
    local mode_name = COPTER_MODES[mode_number]

    -- get distance to home
    local home_location = ahrs:get_home()
    local current_location = ahrs:get_location()
    local home_distance = current_location:get_distance(home_location)

    -- notify user
    gcs:send_text(SEVERITY, "Returning to home, flight mode: " .. mode_name .. ", distance: " .. math.floor(home_distance) .. " meters")

    -- check the flight mode
    if mode_number ~= COPTER_MODE_RTL then
        vehicle:set_mode(COPTER_MODE_RTL)
    end

    -- check the home distance
    if home_distance < TARGET_DECISION_DISTANCE then
        gcs:send_text(SEVERITY, "Reached to home")
        return wait_disarm, LOOP_DELAY
    end

    -- call return to home step
    return return_to_launch, LOOP_DELAY
end

-- wait until vehicle is disarmed
function wait_disarm()

    -- get armable arming status
    local is_armed = arming:is_armed()
    local is_landing = vehicle:is_landing()

    -- get the altitude of the vehicle
    local current_location = ahrs:get_location()
    current_location:change_alt_frame(ALT_FRAME_ABOVE_HOME)
    local current_altitude = current_location:alt() * 1e-2

    -- notify user
    gcs:send_text(SEVERITY, "Final stage, armed:" .. tostring(is_armed) .. " landing:" .. tostring(is_landing) .. " altitude:" .. math.floor(current_altitude) .. "m")

    -- call wait disarm function
    return wait_disarm, LOOP_DELAY
end

-- start the script
return multi_location_mission()
