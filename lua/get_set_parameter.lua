-- Description: This script shows how to get and set a parameter

-- get and set a parameter
function get_set_parameter()

    -- create SCR_USER1 parameter object
    local SCR_USER1 = Parameter()
    if not SCR_USER1:init("SCR_USER1") then
        gcs:send_text(7, "Failed to initialize the parameter")
        return
    end

    -- notify the user about the parameter value
    gcs:send_text(7, "Value of SCR_USER1: " .. SCR_USER1:get())

    -- set the parameter
    local result = SCR_USER1:set(1)

    -- notify the user about the result
    gcs:send_text(7, "Parameter set operation result: " .. tostring(result))

    -- notify the user about the parameter value
    gcs:send_text(7, "Value of SCR_USER1: " .. SCR_USER1:get())

    -- schedule the next call to this function
    -- return get_set_parameter, 1000
end

-- start the script
return get_set_parameter()
