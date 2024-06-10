"""
most data types have two ways to create an empty value
"""

st1 = ""     # literal value
st2 = str()  # constructor value

l1 = []
l2 = list()

t1 = ()
t2 = tuple()

# sets share {} with dictionaries

s1 = {}  # empty set
s1 = set()  # only way to create empty set
print(type(s1))

d1= {}
d2 = dict()
