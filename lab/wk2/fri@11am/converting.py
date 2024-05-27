v1 = "12345"
v2 = int(v1)
v3 = float(str(v2))
v4 = hex(v2)  # int value as arg
v5 = bin(v2)  # int value as arg
v6 = oct(v2)  # int value as arg

# print(v1 + v4)  # results in error
print(v2 + v3)
