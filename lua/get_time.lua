-- Description: This script will get GPS time

-- helper constants
local SECOND_AS_MS = 1000
local MINUTE_AS_MS = 60 * SECOND_AS_MS
local HOUR_AS_MS = 60 * MINUTE_AS_MS
local DAY_AS_MS = 24 * HOUR_AS_MS
local WEEK_AS_MS = 7 * DAY_AS_MS
local YEAR_AS_MS = 365 * DAY_AS_MS
local GPS_TO_UTC_OFFSET = -18 * 1000
local TIMEZONE_OFFSET = 3 * HOUR_AS_MS

-- get GPS time
function get_time()

    -- get boot time in milliseconds
    local boot_time = millis():toint()

    -- send boot time to GCS
    gcs:send_text(7, "System time: " .. boot_time .. " milliseconds since boot")

    -- get GPS time
    local time_week = gps:time_week(0)
    local time_week_ms = gps:time_week_ms(0):toint()

    -- show GPS time on GCS
    gcs:send_text(7, "Time week: " .. time_week)
    gcs:send_text(7, "Time week ms: " .. time_week_ms)

    -- convert GPS time to UTC time
    time_week_ms = time_week_ms + GPS_TO_UTC_OFFSET

    -- add timezone offset to get local time
    time_week_ms = time_week_ms + TIMEZONE_OFFSET

    -- calculate milliseconds of this day
    local time_day_ms = time_week_ms % DAY_AS_MS

    -- calculate hours, minutes, seconds
    local hours = math.floor(time_day_ms / HOUR_AS_MS)
    local minutes = math.floor((time_day_ms - hours * HOUR_AS_MS) / MINUTE_AS_MS)
    local seconds = math.floor((time_day_ms - hours * HOUR_AS_MS - minutes * MINUTE_AS_MS) / SECOND_AS_MS)

    -- send time to GCS
    gcs:send_text(7, string.format("Time: %02d:%02d:%02d", hours, minutes, seconds))

    -- schedule the next call to this function
    return get_time, 1000
end

-- start the script
return get_time()
