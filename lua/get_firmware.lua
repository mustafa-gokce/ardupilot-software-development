-- Description: This script reads firmware version

-- helper constants
local VEHICLE_TYPE_COPTER = 2
local MINIMUM_REQUIRED_VERSION = 4.5
local REQUIRED_VERSION_HASH = "73480438"

-- read firmware version
function get_firmware()

    -- get major, minor and patch version
    local VERSION_MAJOR = FWVersion:major()
    local VERSION_MINOR = FWVersion:minor()
    local VERSION_PATCH = FWVersion:patch()
    local VERSION_HASH = FWVersion:hash()
    local VERSION_STRING = FWVersion:string()
    local VEHICLE_TYPE = FWVersion:type()

    -- send version to GCS
    gcs:send_text(7, string.format("Major: %d, Minor: %d, Patch: %d", VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH))
    gcs:send_text(7, string.format("Hash: %s", VERSION_HASH))
    gcs:send_text(7, string.format("Version String: %s", VERSION_STRING))
    gcs:send_text(7, string.format("Vehicle type: %d", VEHICLE_TYPE))

    -- this script should only be run on copter
    if VEHICLE_TYPE ~= VEHICLE_TYPE_COPTER then
        gcs:send_text(7, "This script is for Copter only")
        return
    end

    -- this script should only be run on versions above 4.5
    if VERSION_MAJOR + VERSION_MINOR * 0.1 < MINIMUM_REQUIRED_VERSION then
        gcs:send_text(7, "This script should be run on version above 4.5")
        return
    end

    -- check the version hash
    if REQUIRED_VERSION_HASH ~= VERSION_HASH then
        gcs:send_text(7, "Incompatible version hash: " .. VERSION_HASH)
        return
    end

    -- check for stable release
    if string.find(VERSION_STRING, "dev") then
        gcs:send_text(7, "Development binary, be careful")
    end

    -- notify user
    gcs:send_text(7, "Starting to script...")

    -- schedule the next call to this function
    -- return get_firmware, 1000
end

-- start the script
return get_firmware()
