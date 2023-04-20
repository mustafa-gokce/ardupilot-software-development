-- Description: This script reads attitude from AHRS and sends it to GCS

-- read attitude from AHRS
function read_attitude()

    local roll = math.deg(ahrs:get_roll())
    local pitch = math.deg(ahrs:get_pitch())
    local yaw = math.deg(ahrs:get_yaw())

    gcs:send_text(7, string.format("Attitude -> roll: %0.1f pitch: %0.1f yaw: %0.1f", roll, pitch, yaw))

    -- schedule the next call to this function
    return read_attitude, 1000
end

-- start the script
return read_attitude()
