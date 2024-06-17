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

