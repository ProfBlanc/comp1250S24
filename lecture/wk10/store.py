"""
This is the documentation of our store.py module.
Put description here
"""

name = "Our Cool Store"
since = 2024
hours_of_operation = {"opening": 8, "closing":20}
product_sold = [
    {"name": "food", "description": "to eat", "price": 10},
    {"name": "drink", "description": "to drink", "price": 3},
    {"name": "clothes", "description": "to wear", "price": 19.99},
    {"name": "shoes", "description": "to walk in", "price": 39.99},
]

def order_in_store(product:str, quantity:int)->float: #parameters
    """
    This is an order function that allows the user to order a product in store
    :param product: a poduct name that should be found in our products sold variable
    :param quantity: a non-negative value
    :return: the price of the purchase
    :type product str
    :type quantity int
    :rtype float

    Unit Testing aka how this function should operate

    >>> order_in_store("honey", -5)
    -1
    >>> order_in_store("food", 5)
    50

    """
    quantity = 1 if quantity <= 0 else quantity

    for each_product in product_sold:
        if product == each_product['name']:
            return each_product['price'] * quantity


    return -1 # product not found


def order_online(address:str, product: str, quantity: int)->float:
    """
    TODO: finish documentation
    :param address:
    :param product:
    :param quantity:
    :return:
    """
    if "toronto" in address.lower(): # "160 Kendal Ave, Toronto, ON" => "160 kendal ave, toronto, on"
        return order_in_store(product=product, quantity=quantity)
    return -1


def feedback(name: str, message: str, stars: int)-> tuple[str, int]:
    if isinstance(name, str) and isinstance(message, str) and isinstance(stars, int):
        name = name.lower()
        if len(name) > 5 and len(message) > 20:
            return name, stars
        return "Error part 1", -1
    else:
        return "Error part 2", 0
