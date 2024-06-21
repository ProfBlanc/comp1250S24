"""
function
    outlining a behaviour
        multiple steps
            step = statement

sleeping
    shutting eyes
    lowering heart rate

a process
order item online

ordering a t-shirt
    customize the shirt
        size, color, sleeve_type


"""

def order_tshirt(size, color, sleeve_type):  # params
    if size in ['small', 'medium', 'large'] and \
        color in ['red', 'black', 'blue'] and \
        sleeve_type in "long short none".split(" "):
        return f"Your {size} t-shirt order in color " \
                f"{color} with sleeve type " \
                f"{sleeve_type} is ready"
    else:
        return (f"Order not possible")


result1 = order_tshirt("large", "black", "long")
print(result1)




def add(n1, n2):
    if isinstance(n1, int) or isinstance(n1, float) \
            and isinstance(n2, int) or isinstance(n2, float):
        return n1 + n2


v1 = add(1, 2)
v2 = add(1.1, 2.2)
v3 = add("1", "2")
v4 = add(2, True)
v5 = add([1,2], [3,4])
v6 = add({1,2}, {4,6})
print("hi")


def mul(a, b):
    return a, b

print(mul(2,3))
