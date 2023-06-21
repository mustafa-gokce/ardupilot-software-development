-- Description: This script is for doing some examples with Location() object

-- location examples function
function location_example()

    -- example location 1
    local location_1 = Location()
    location_1:relative_alt(true)
    location_1:lat(-353638740)
    location_1:lng(1491648656)
    location_1:alt(3000)

    -- example location 2
    local location_2 = Location()
    location_2:relative_alt(true)
    location_2:lat(-353613588)
    location_2:lng(1491611480)
    location_2:alt(3000)

    -- example location 3
    local location_3 = Location()
    location_3:relative_alt(true)
    location_3:lat(-353601910)
    location_3:lng(1491658294)
    location_3:alt(3000)

    -- calculate distances
    local distance_1_2 = location_1:get_distance(location_2)
    local distance_2_3 = location_2:get_distance(location_3)
    local distance_1_3 = location_1:get_distance(location_3)
    gcs:send_text(7, "Distance 1-2: " .. distance_1_2 .. " meters")
    gcs:send_text(7, "Distance 2-3: " .. distance_2_3 .. " meters")
    gcs:send_text(7, "Distance 1-3: " .. distance_1_3 .. " meters")

    -- calculate bearings
    local bearing_1_2 = math.deg(location_1:get_bearing(location_2))
    local bearing_2_3 = math.deg(location_2:get_bearing(location_3))
    local bearing_1_3 = math.deg(location_1:get_bearing(location_3))
    gcs:send_text(7, "Bearing 1-2: " .. bearing_1_2 .. " degrees")
    gcs:send_text(7, "Bearing 2-3: " .. bearing_2_3 .. " degrees")
    gcs:send_text(7, "Bearing 1-3: " .. bearing_1_3 .. " degrees")

    -- calculate new locations
    local location_2_new = location_1:copy()
    location_2_new:offset_bearing(bearing_1_2, distance_1_2)
    local location_3_new = location_2:copy()
    location_3_new:offset_bearing(bearing_2_3, distance_2_3)
    gcs:send_text(7, "Error of 2: " .. location_2:get_distance(location_2_new) .. " meters")
    gcs:send_text(7, "Error of 3: " .. location_3:get_distance(location_3_new) .. " meters")

    -- calculate vectors
    local vector_1_2 = location_1:get_distance_NE(location_2)
    local vector_2_3 = location_2:get_distance_NE(location_3)
    local vector_1_3 = location_1:get_distance_NE(location_3)
    gcs:send_text(7, "Vector 1-2: North-> " .. vector_1_2:x() .. " East-> " .. vector_1_2:y())
    gcs:send_text(7, "Vector 2-3: North-> " .. vector_2_3:x() .. " East-> " .. vector_2_3:y())
    gcs:send_text(7, "Vector 1-3: North-> " .. vector_1_3:x() .. " East-> " .. vector_1_3:y())

    -- calculate new locations
    location_2_new = location_1:copy()
    location_2_new:offset(vector_1_2:x(), vector_1_2:y())
    location_3_new = location_2:copy()
    location_3_new:offset(vector_2_3:x(), vector_2_3:y())
    gcs:send_text(7, "Error of 2: " .. location_2:get_distance(location_2_new) .. " meters")
    gcs:send_text(7, "Error of 3: " .. location_3:get_distance(location_3_new) .. " meters")

end

-- start the script
return location_example()
