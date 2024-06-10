"""
SETS
    a series of values
        how different then list, tuples?

    a series of values that are
        unordered
            no indexes stored
                cannot select a specific value

        does not contain duplicate values

        cannot contain mutable data types
            no list allowed
            tuple, string allowed

"""

s1 = set()  # NOT SAME as [], NOT SAME as ()
s2 = {1, "a", False, 2.3}

s1.add("hello")
s1.add("world")
s1.add(123)
s1.add("123")

s1.add(123)

# print(s1[0])
for value in s1:
    print(value)

#s1.discard("abc")
if "abc" in s1:
    s1.remove("abc")
