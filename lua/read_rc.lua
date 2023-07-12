-- Description: This script reads RC inputs.

-- define global variables
local MAV_SEVERITY_DEBUG = 7
local LOOP_DELAY_IN_MS = 1000

-- read channel
function read_channel(channel)
    local channel_value = rc:get_pwm(channel)
    if not channel_value then
        return 0
    end
    return channel_value
end

-- read RC input
function read_rc()

    -- read RC inputs
    local channel_6 = read_channel(6)
    local channel_7 = read_channel(7)

    -- log RC inputs
    gcs:send_text(MAV_SEVERITY_DEBUG, "RC input: channel 6 = " .. channel_6 .. ", channel 7 = " .. channel_7)

    -- schedule the next call to this function
    return read_rc, LOOP_DELAY_IN_MS
end

-- start the script
return read_rc()
