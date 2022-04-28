function arm_disarm()
    if arming:is_armed() then
        -- gcs:send_text(7, "Vehicle is ARMED!")
        arming:disarm()
    else
        -- gcs:send_text(7, "Vehicle is DISARMED!")
        arming:arm()
    end
    return arm_disarm, 5000
end

return arm_disarm()