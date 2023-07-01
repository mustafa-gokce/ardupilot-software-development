-- Description: This script will write log to on-board logging system
-- https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Logger/README.md
-- https://github.com/ArduPilot/pymavlink/blob/master/tools/mavlogdump.py

-- global variables
local my_data = {}

-- save to log file
function save_to_log()
    logger:write("ASD1", "latitude,longitude,altitude", "fff", my_data[1], my_data[2], my_data[3])
end

-- write log to on-board logging system
function update()

    -- read current location of the vehicle
    local current_location = ahrs:get_location()

    -- check for valid location
    if current_location then

        -- get latitude, longitude and altitude of the vehicle
        my_data[1] = current_location:lat() * 1e-7
        my_data[2] = current_location:lng() * 1e-7
        my_data[3] = current_location:alt() * 1e-2

        -- save data to log file
        save_to_log()

    end

    -- schedule the next call to this function
    return update, 1000
end

-- start the script
return update()
