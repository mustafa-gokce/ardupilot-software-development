-- Description: This script sets servo and relay outputs.
-- Make sure that SERVOx_FUNCTION is set to 0, link in below:
-- https://ardupilot.org/copter/docs/parameters.html#servo1-function-servo-output-function
-- Observe the output with: "graph SERVO_OUTPUT_RAW.servox_raw" where x is the selected channel
-- SERVOx_FUNCTION = 94 (Script1) and up to 16 channels can be dedicated for scripting (94 - 109, Script1 - Script16)
-- Before doing relay operations, make sure to set RELAY_PINx (up to 6) to an appropriate value.
-- Make sure that RELAYx_PIN is set to 0 (for 0th bit of SIM_PIN_MASK, 0th SITL output pin).
-- For real world applications, make sure to set RELAYx_PIN to an appropriate output pin, link in below:
-- https://ardupilot.org/copter/docs/parameters.html#relay-pin-first-relay-pin

-- define global variables
local MAV_SEVERITY_DEBUG = 7
local LOOP_DELAY_IN_MS = 1000
local RELAY_INSTANCE = 0
local SERVO_FUNCTION = 94
local flipflop = true
local servo_channel

-- set servo and relay outputs
function set_servo_relay()

    -- check if servo does exist
    if not servo_channel then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Servo does not exist for function " .. SERVO_FUNCTION)
        return set_servo_relay, LOOP_DELAY_IN_MS
    end

    -- check if relay does exist
    if not relay:enabled(RELAY_INSTANCE) then
        gcs:send_text(MAV_SEVERITY_DEBUG, "Relay is not enabled")
        return set_servo_relay, LOOP_DELAY_IN_MS
    end

    -- flipflop is true
    if flipflop then

        -- set servo
        SRV_Channels:set_output_pwm_chan(servo_channel, 2000)

        -- set relay
        relay:on(RELAY_INSTANCE)

    -- flipflop is false
    else

        -- clear servo
        SRV_Channels:set_output_pwm_chan(servo_channel, 1000)

        -- clear relay
        relay:off(RELAY_INSTANCE)

    end

    -- notify the user about the servo state
    local servo_state = SRV_Channels:get_output_pwm(SERVO_FUNCTION)
    gcs:send_text(MAV_SEVERITY_DEBUG, "Servo current state: " .. servo_state)

    -- notify the user about the relay state
    local relay_state = relay:get(RELAY_INSTANCE)
    gcs:send_text(MAV_SEVERITY_DEBUG, "Relay current state: " .. relay_state)

    -- flip the flipflop
    flipflop = not flipflop

    -- schedule the next call to this function
    return set_servo_relay, LOOP_DELAY_IN_MS
end

-- get servo object
servo_channel = SRV_Channels:find_channel(SERVO_FUNCTION)

-- start the script
return set_servo_relay()
