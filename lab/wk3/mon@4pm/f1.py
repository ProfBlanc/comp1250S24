"""
We will create a pizza ordering system
Ask the user what size of pizza they want
    only accept small, medium, large
Ask the user for the toppings that they want
in the pizza
    confirm that cheese is part of their toppings
Ask the user for the distance between them and the pizza
store: only accept values between 1-30
Calculate a price:
    $5 = base price
    $2 extra for small
    $4 extra for medium
    $6 extra for large
1.75 cents per kilometer for delivery
"""
print("Welcome to our Pizza Restaurant")
size = input("What size of pizza do you want? ").lower()
if size == "small" or size == "medium" or size == "large":
    toppings = input(f"Enter the {size} pizza toppings: ").lower()
    if "cheese" in toppings:
        distance = input("Enter the distance from your home to our restaurant: ")
        if distance.isdigit():  # -10
            distance = int(distance)
            if distance >= 1 and distance <= 30:
                price = 5.0
                if size[0] == "s":
                    price += 2
                elif ord(size[0]) == 109:
                    price += 4
                else:
                    price += 6

                price += distance * 1.75
                print(f"The total for your {size} pizza with the "
                      f"toppings {toppings} is ${price}")
            else:
                print(f"Sorry but we do not deliver to address {distance} kilometers away. It's too far")

        else:
            print("Invalid integer value inputted")
    else:
        print(f"Your {size} pizza needs to contain cheese")
else:
    print("Invalid pizza size")


"""

0       1       2       3       4       5

M       E       D       I       U       M


"""