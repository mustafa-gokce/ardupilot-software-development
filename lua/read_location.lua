-- Description: This script reads location from AHRS and sends it to the GCS

-- altitude frame types
local ALT_FRAME_ABSOLUTE = 0
local ALT_FRAME_ABOVE_HOME = 1

-- read location from AHRS
function read_location()

    -- read current location of the vehicle
    local current_location = ahrs:get_location()

    -- check for valid location
    if current_location then

        -- change altitude frame
        -- current_location:change_alt_frame(ALT_FRAME_ABSOLUTE)
        current_location:change_alt_frame(ALT_FRAME_ABOVE_HOME)

        -- get latitude, longitude and altitude of the vehicle
        local latitude = current_location:lat() * 1e-7
        local longitude = current_location:lng() * 1e-7
        local altitude = current_location:alt() * 1e-2

        -- notify GCS with the current location
        -- gcs:send_text(7, string.format("Location -> Latitude: %0.6f Longitude: %0.6f Altitude %0.2f (AMSL)", latitude, longitude, altitude))
        gcs:send_text(7, string.format("Location -> Latitude: %0.6f Longitude: %0.6f Altitude %0.2f (HOME)", latitude, longitude, altitude))

    end

    -- schedule the next call to this function
    return read_location, 1000
end

-- start the script
return read_location()
