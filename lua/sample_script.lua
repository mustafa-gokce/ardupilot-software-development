local loop_counter = 0

function simple_loop()
    gcs:send_text(7, "loop_counter: " .. loop_counter)
    -- gcs:send_named_float("COUNTER", loop_counter)
    loop_counter = loop_counter + 1
    return simple_loop, 1000
end

return simple_loop()