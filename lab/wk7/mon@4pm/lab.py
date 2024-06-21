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


# determine which string variable is the longest (accept 2 or 3 values)

def which_is_longest(s1, s2, s3=""):
    # s1 = str(s1)
    # s2 = str(s2)
    # s3 = str(s3)

    if isinstance(s1, str) and isinstance(s2, str) and isinstance(s3, str):
        values = [s1, s2, s3]
        # values.sort(key=len)
        # return values[-1]
        values.sort(key=len, reverse=True)
        return values[0]

result1 = which_is_longest("hello", "good", "i love python")
result2 = which_is_longest("hello", "good")
# result1 = "i love python"
# result2 = "hello"
print(result1)
print(result2)

result3 = which_is_longest(1234, 124.56, 32452)
print(result3)
