from examples import *

v1 = high_low(-10, 10)
v2 = high_low(400000000, 10000)
print(v1, v2)
print("*" * 20)

v3 = get_product_of_numbers(1, 2, 3)
v4 = get_product_of_numbers(2, 4, 6)
v5 = get_product_of_numbers(num2=20, num1=10, num3=2)
v6 = get_product_of_numbers()
print(v3, v4, v5, v6)
print("*" * 20)

order1 = order_pizza(["cheese", "peperoni", "pineapples"], "medium", 5)
print(order1)