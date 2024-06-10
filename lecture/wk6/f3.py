n1 = list(range(1, 11))
n2 = list(range(2, 15, 2))

# common values of the two lists?

s1 = set(n1)
s2 = set(n2)

s3 = s1.intersection(s2)

print("common values are", s3)