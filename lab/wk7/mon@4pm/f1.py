"""
A function: a name that has multiple steps/processes
    variable = one or many values

a function: a name that points to multiple steps or processes => bahaviour
    parameters: modify how the function behaves


    Sleep
        1) closes eyes
        2) slow down breathing
        3) start dreaming

    Sleeping can vary
        location
        duration

    sleep(location, duration)
        execute steps to sleep
        introducing local variables
"""

def sleep(location):
    eyes = "open"
    heart_rate = 100
    is_dreaming = False

    if "bed" in location:
        eyes = "closed"
        is_dreaming = True
        duration = 480
    elif location in "train bus".split(" "):
        eyes = "half-open"
        duration = 10


    heart_rate /= 2

    # return "snoring!"  # feedback that the method has executed
    return eyes, heart_rate, duration, is_dreaming  # returns tuple

result = sleep("bed")
print(result)
result = sleep("train")
print(result)