"""
Tuples
    like a list
        stores series of values
    BUT
        immutable
            values cannot change after creation

    ???
        Why does this data exists
            if programmer wants to create a series of values and disallow user to change these values => use tuple
"""

t1 = ("dob", "place of birth", "sin", 12345)

# insert into a tuple?
# delete a value from a tuple?
# get you get an index of a value of a tuple
# can you copy a tuple?
# can you merge values that update the original value?
# can you merge values that create a new tuple?
print(t1[2])  # 'sin'
print(t1.index("dob"))  # 0

student_meta_data = (123456789, "Date Accepted to GBC")
# student_meta_data[0] = 229374372394  # cannot change, hence immutable

t2 = ("test", "case", 123)

t3 = t1 + t2
print(t3)

t4 = t1 * 3 + t2 * 4

t5 = tuple("Benny")

print(t5)

t6 = tuple(range(1, 11, 3))

print(t6)

# isinstance(value, dataTypeWithoutQuotes)

print(isinstance("ben", str))
print(isinstance(123, int))
print(isinstance(True, int))
print(isinstance(123.4, int))
print(isinstance(123.4, float))



