-- Description: This script will get battery data

-- get battery data
function get_battery()

    -- get battery related data
    local voltage = battery:voltage(0)
    local voltage_resting_estimated = battery:voltage_resting_estimate(0)
    local current_amps = battery:current_amps(0)
    local consumed_mah = battery:consumed_mah(0)

    -- send data to GCS
    gcs:send_text(7, "Voltage: " .. voltage .. "V")
    gcs:send_text(7, "Resting voltage (estimated): " .. voltage_resting_estimated .. "V")
    gcs:send_text(7, "Instantaneous current: " .. current_amps .. "A")
    gcs:send_text(7, "Consumed capacity: " .. consumed_mah .. "mAh")

    -- schedule the next call to this function
    return get_battery, 1000
end

-- start the script
return get_battery()
