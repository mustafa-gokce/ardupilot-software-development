-- Description: This script will fly the drone to a location
-- To initialize the target location, local target_location = Location()
-- To make the location as altitude above home, target_location:relative_alt(true)
-- To set latitude, target_location:lat(latitude)
-- To set longitude, target_location:lng(longitude)
-- To set altitude, target_location:alt(altitude)
-- Use vehicle:set_target_location(target_location) to set the target location

-- create target location
local target_location = Location()
target_location:relative_alt(true)
target_location:lat(-353613139)
target_location:lng(1491611342)
target_location:alt(4500)

-- fly to a location
function goto_location()

    -- notify user
    gcs:send_text(7, "Target distance: " .. vehicle:get_wp_distance_m() .. " meters")

    -- go to location
    vehicle:set_target_location(target_location)

    -- schedule the next call to this function
    return goto_location, 1000
end

-- start the script
return goto_location()
