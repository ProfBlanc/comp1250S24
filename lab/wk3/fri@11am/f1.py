"""
Pizza delivery calculator

Ask the user for a pizza size
    small   medium   large

Ask the user for the toppings
    Ensure that cheese is on the pizza
Ask the user their distance from restaurant
    Allow a max distance of 20

Ask the user for how many pizza they want

Calculate the price
    $5 base price
    $2 extra for small
    $3 extra for medium
    $4 for large

Charge 1.6 per km

"""

print("Welcome to our pizza restaurant")
size = input("Enter your pizza size (S,M,L): ")

# ' hello ' => 'hello'

# ' hello world ' => 'hello world'


if size.strip().upper()[0] in 'SML':
    toppings = input("Enter the toppings").lower()
    if "cheese" in toppings:
        distance = int(input("Enter the distance from your address to the restaurant in kilometers: "))
        if distance > 0 and distance <= 20:
            quantity = int(input("Enter a quantity"))
            if quantity > 0:
                price = 5
                if size.strip().upper()[0] == "S":
                    price += 2
                elif size.strip().upper()[0] == "M":
                    price += 3
                else:
                    price += 4

                price *= quantity

                price += distance * 1.60
                print(f"Your {size} pizza with toppings {toppings} costs $ {price}")

            else:
                print("Quantity must be greater than 1")
        else:
            print("Your address is too far from the restaurant.")
    else:
        print("Cheese must be on the pizza")
else:
    print("Sorry but you chose a wrong size")