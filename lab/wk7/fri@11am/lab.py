"""
A Function?
    a name that represents many steps
    many python statements


    A process
    ordering something online
    customize the bahavior/settings of the process

"""

def order_tshirt(size, color):
    if size not in "s,m,l,xl".split(","):
        print("Invalid Size")
    elif color not in "black blue white red green".split(" "):
        print("Invalid Color")
    else:
        return 5 * (len(size) + len(color))

# print(color)
v1 = order_tshirt("s", "black")
print(v1)

v2 = order_tshirt("xxs", "beige")
print(v2)


def mult(n1, n2):
    if isinstance(n1, int) or isinstance(n1, str) \
            or isinstance(n1, float) and \
            isinstance(n2, int) or isinstance(n2, str) \
            or isinstance(n2, float):
                return n1 * n2

v1 = mult(5, 6)
v2 = mult("hello", 3)
v3 = mult(5, "a")
v4 = mult([1,2,3], [4,5,6])
# v5 = mult("hello", 1.5)
print("end")


def two_vals(a, b):
    return a, b

print(two_vals("hi", 123))
