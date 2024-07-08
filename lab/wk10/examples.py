"""
Many function examples
"""
def high_low(num1:int, num2:int)->tuple[int, int]:
    """
    Return a tuple of the lowest number & highest num
    :param num1: any int value
    :param num2: any int value
    :return: tuple of low then high number
    """
    return min(num1, num2), max(num1, num2)

def get_product_of_numbers(num1:int = 1, num2:int = 2, num3:int = 3)->int:
    return num1 * num2  * num3

def order_pizza(topping:list[str], size:str, distance:float)->float:
    """
    Calculate the price of a pizza order
    :param topping: list of string toppings
    :param size: small, medium or large
    :param distance: a km distance to deliver
    :return: the price of the pizza
    """
    base_price = 5
    if "cheese" in topping and len(topping) <= 5:
        if size not in "small medium large".split(" "):
            return -2 # invalid size
        if distance <0 and distance > 15:
            return -3 # invalid distance

        toppings_charge = 2 * len(topping)
        if size[0] == "m":
            base_price += 2
        if size[0] == "l":
            base_price += 3
        distance_charge = 1.7 * distance
        return base_price + toppings_charge + distance_charge
    else:
        return -1 # invalid toppings