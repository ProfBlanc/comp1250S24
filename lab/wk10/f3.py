"""
Random functions to work on creating functions.
Week 10 content
"""


def high_low(num1: int = 10, num2: int = 20) -> tuple[int, int]:
    """
    This function sorts the two numbers and
    returns the values as a sorted tuple
    :param num1: first int value
    :param num2: second int value
    :return: tuple with sorted values
    >>> high_low()
    (10, 20)
    >>> high_low(1, 2)
    (1, 2)
    >>> high_low(22, 11)
    (11, 22)
    >>> high_low(1, 1)
    (1, 1)
    >>> high_low(num2=100, num1=-100)
    (-100, 100)
    """
    return min(num1, num2), max(num1, num2)


def product_of_three_numbers(num1: int, num2: int, num3: int) -> int:
    return num1 * num2 * num3


def get_sum_and_avg_of_numbers(*args):
    # for value in args:
    #     print(value)
    return sum(args), sum(args) / len(args)



def order_pizza(size: str,toppings: list, sauces: list, address: str) -> float:
    """
    We will order a pizza and outline the size, toppings,
    sauces and a price will be generated for our pizza order
    :param size: 1 char of s,m,or l
    :param toppings: list of toppings must have 1 topping and cheese must be included
    :param sauces: no validation
    :param address: at least 10 character in address
    :return: the price of the pizza
    """
    pass



##############################

print()
print("Hello World!")
print("hi", 123)
print("hello", False, 1.234)

from examples import get_sum_and_avg_of_numbers

v = get_sum_and_avg_of_numbers(1, 2,3 ,44, 55)
print(v)
