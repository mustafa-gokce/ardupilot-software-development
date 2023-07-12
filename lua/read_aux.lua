-- Description: This script reads auxiliary switch.
-- RCx_OPTION = 300 (AUX1) and up to 8 channels can be used for scripting (300 - 307, AUX1 - AUX8)

-- define global variables
local MAV_SEVERITY_DEBUG = 7
local LOOP_DELAY_IN_MS = 1000
local SCRIPTING_1 = 300
local LOW = 0
local MEDIUM = 1
local HIGH = 2
local switch_1

-- read auxiliary switch
function read_aux()

    -- check if switch does exist
    if not switch_1 then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Switch does not exist for option " .. SCRIPTING_1)
        return read_aux, LOOP_DELAY_IN_MS
    end

    -- read switch value
    local switch_1_value = switch_1:get_aux_switch_pos()

    -- check switch value
    if switch_1_value == LOW then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Switch is LOW")
    elseif switch_1_value == MEDIUM then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Switch is MEDIUM")
    elseif switch_1_value == HIGH then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Switch is HIGH")
    else
        gcs:send_text(MAV_SEVERITY_DEBUG, "Switch is in unknown position")
    end

    -- schedule the next call to this function
    return read_aux, LOOP_DELAY_IN_MS
end

-- get switch object
switch_1 = rc:find_channel_for_option(SCRIPTING_1)

-- start the script
return read_aux()
