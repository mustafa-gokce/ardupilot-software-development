-- Description: This script will do multi location mission from file and controlled by switch
-- RCx_OPTION = 300 (AUX1) and up to 8 channels can be used for scripting (300 - 307, AUX1 - AUX8)
-- Content of MISSION.csv is:
-- -35.36573684,149.16312254,30.0
-- -35.36135212,149.16115359,45.0
-- -35.36022811,149.16580334,20.0
-- -35.36565041,149.16683329,35.0

-- create a location object
function createLocation(lat, lng, alt)
    local location = Location()
    location:relative_alt(true)
    location:lat(math.floor(lat * 1e7))
    location:lng(math.floor(lng * 1e7))
    location:alt(math.floor(alt * 1e2))
    return location
end

-- process the line with commas
function split_with_comma(str)
    local fields = {}
    for field in str:gmatch("([^,]+)") do
        fields[#fields + 1] = field
    end
    return fields
end

-- read a file line by line
function lines_from(file_path)
    local lines = {}
    for line in io.lines(file_path) do
        lines[#lines + 1] = line
    end
    return lines
end

-- mode enumerations, helper, constants, configurations
local COPTER_MODES = { [0] = "STABILIZE", [4] = "GUIDED", [6] = "RTL"}
local FILE_PATH = "/scripts/MISSION.csv"
local SCRIPTING_1 = 300
local MEDIUM = 1
local COPTER_MODE_GUIDED = 4
local COPTER_MODE_RTL = 6
local ALT_FRAME_ABOVE_HOME = 1
local TAKEOFF_ALTITUDE = 30
local TARGET_DECISION_DISTANCE = 5
local LOOP_DELAY = 1000
local SEVERITY = 7
local navigation_index = 1

-- target locations
local target_locations = {}

-- multi location mission
function multi_location_mission()

    -- notify user
    gcs:send_text(SEVERITY, "Starting the mission")

    -- call flight mode change step
    return read_mission_file, LOOP_DELAY
end

-- read mission file
function read_mission_file()

    -- read mission file line by line
    local lines = lines_from(FILE_PATH)

    -- check the file is opened successfully
    if not lines then
        gcs:send_text(SEVERITY, "Unable to open file: " .. FILE_PATH)
        return read_mission_file, LOOP_DELAY
    end

    -- create target locations
    for i = 1, #lines do
        local fields = split_with_comma(lines[i])
        target_locations[i] = { tonumber(fields[1]), tonumber(fields[2]), tonumber(fields[3]) }
    end

    -- check at least one waypoint exist
    if #target_locations < 1 then
        gcs:send_text(SEVERITY, "Mission files is empty")
        return read_mission_file, LOOP_DELAY
    end

    -- notify user
    gcs:send_text(SEVERITY, "Mission file read success, total waypoints: " .. #target_locations)

    -- call read auxiliary channel step
    return read_aux, LOOP_DELAY
end

-- read the auxiliary switch
function read_aux()

    -- get switch object
    local switch_1 = rc:find_channel_for_option(SCRIPTING_1)

    -- check if switch does exist
    if not switch_1 then
        gcs:send_text(SEVERITY, "Switch does not exist for option " .. SCRIPTING_1)
        return read_aux, LOOP_DELAY
    end

    -- read switch value
    local switch_1_value = switch_1:get_aux_switch_pos()

    -- check switch value
    if switch_1_value == MEDIUM then
        gcs:send_text(SEVERITY, "Switch is MEDIUM")
        return change_flight_mode, LOOP_DELAY
    end

    -- notify user
    gcs:send_text(SEVERITY, "Waiting for the switch to be MEDIUM")

    -- schedule the next call to this function
    return read_aux, LOOP_DELAY
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
