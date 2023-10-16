-- Description: This script is for protected function calls
-- pcall is a function that calls a function by protecting it from errors
-- Errors are runtime errors that occur during the execution of the program
-- They are as a result of bad calculations or bad input
-- pcall returns true if the function call was successful, or false if not
-- pcall also returns the error message if the function call was unsuccessful
-- It also takes arguments, which are passed to the function
-- It returns the values returned by the function if any
-- Usage: local success, result = pcall(function, arg1, arg2, ...)

function add()
    return 1 + "a"
    -- return 1 + 2
end

function protected_call()
    local success, result = pcall(add)
    if not success then
        gcs:send_text(7, "Caught, error: " .. result)
    else
        gcs:send_text(7, "Success, result: " .. result)
    end
    gcs:send_text(7, "Called the function")
end

return protected_call()
