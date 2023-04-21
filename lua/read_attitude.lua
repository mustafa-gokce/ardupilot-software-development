-- Description: This script reads attitude from AHRS and sends it to GCS

-- read attitude from AHRS
function read_attitude()

    -- read roll, pitch and yaw angles in degrees
    local roll = math.deg(ahrs:get_roll())
    local pitch = math.deg(ahrs:get_pitch())
    local yaw = math.deg(ahrs:get_yaw())

    -- send roll, pitch and yaw readings as string to GCS
    gcs:send_text(7, string.format("Attitude -> roll: %0.1f pitch: %0.1f yaw: %0.1f", roll, pitch, yaw))

    -- schedule the next call to this function
    return read_attitude, 1000
end

-- start the script
return read_attitude()
