-- Description: This script will read and write from/to a file
local ALT_FRAME_ABOVE_HOME = 1
local FILE_PATH = "/scripts/LOCATION_DATA.csv"
local file
local location_data = {}

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

-- save data to file
function save_to_file()

    -- check the file is opened successfully
    if not file then
        gcs:send_text(7, "Unable to open file: " .. FILE_PATH)
        return
    end

    -- save the data to file (for more precision, use string formatting)
    file:write(tostring(millis()) .. ", " .. table.concat(location_data, ", ") .. "\n")

    -- flush the file
    file:flush()

end

-- read and write from/to a file
function read_write()

    -- read current location of the vehicle
    local current_location = ahrs:get_location()

    -- check for valid location
    if current_location then

        -- change altitude frame
        if current_location:change_alt_frame(ALT_FRAME_ABOVE_HOME) then

            -- get latitude, longitude and altitude of the vehicle
            location_data[1] = current_location:lat() * 1e-7
            location_data[2] = current_location:lng() * 1e-7
            location_data[3] = current_location:alt() * 1e-2

            -- save the location to file
            save_to_file()

        end
    end

    -- schedule the next call to this function
    return read_write, 1000
end

file = io.open(FILE_PATH, "a")
if not file then
    gcs:send_text(7, "Unable to open file: " .. FILE_PATH)
end

-- process the file
-- local first_line = lines_from(FILE_PATH)[1]
-- local values = split_with_comma(first_line)
-- local time_stamp = tonumber(values[1])
-- local latitude = tonumber(values[2])
-- local longitude = tonumber(values[3])
-- local altitude = tonumber(values[4])
-- gcs:send_text(7, "Time stamp: " .. time_stamp .. " Latitude: " .. latitude .. " Longitude: " .. longitude .. " Altitude: " .. altitude)

-- start the script
return read_write()
