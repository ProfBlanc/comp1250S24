"""
Repetition Structure
    loops
        for while

Control Stuctures
    if statements
        if, elif, else

Attributes / Values
    variables
        single, multiple (list, tuple, sets, dictionaries)

Functions/Behaviors
    a named value
        stores mutliple statements



in function, have the ability to modify the behavior

an order from Amazon
    order a t-shirt
        customize
           color, size, type, material
                paramters

        final product requested is delivered to you
        to deliver something to a caller, you RETURN statement

"""


def order_tshirt(size, color, type):
    price = 5.0
    value = "hello"
    if size == 'medium':
        price += 1
    elif size == 'large':
        price += 2
    else:
        price += 3

    if "long" in type:
        price += 5

    if color not in "black white".split(" "):
        price += 4

    # return price
    return price, color, size



# print(value)
cost = order_tshirt("large", "red", "long")
print(cost)



def add(n1, n2):
    if isinstance(n1, int) or isinstance(n1, float) \
            and isinstance(n2, int) or isinstance(n2, float):
        return n1 + n2

v1 = add(1, 2)
v2 = add("a", "b")
v3 = add(1.1, 2.2)
v4 = add([1,2], [3,4])
# v5 = add("hi", 123)
v5 = add(1, 1.1)
print("hello")
