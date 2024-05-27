"""
list
    a data type in python
        equivalent to array
    can store multiple values of any data type
"""

v1 = [1, 2.2, True, "hi"]  # a list of 4 values with 4 distinct data types

print(v1[1])

# string => list .
# a string is in implict LIST of characters
v2 = "Ben"
v3 = ["B", "e", "n"]

print(v1)
print(v3)

# convert explictly string => list

v4 = list("Ben Blanc")
print(v4)

# generate a series of numbers

# range(end)
# range(start, end)
# range(start, end, step)

# end value is exclusive (up to but NOT including)
v5 = list(range(10))
print(v5)

v6 = list(  range(1, 11)  )
print(v6)

v7 = list(  range(10, 101, 10) )
print(v7)

v8 = list(  range( 200, 99, -2  ))
print(v8)

print( list("hello".upper())[1:4] )  #  ['E', 'L', 'L]

print(len(v8))  # 51

v9 = list("hello".upper())

print(v9[-3])
print(v9[-3:-2])
