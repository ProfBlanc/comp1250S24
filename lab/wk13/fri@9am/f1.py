from food_delivery import FoodDelivery

uber_eats = FoodDelivery(name="UberEats",
available_restaurants= ["Pizza Pizza", "McDonalds", "Tim Hortons"],
hours_available={"open": 6, "close": 23}, distance_limitation=20,
                        min_order_amount=5
)

print(uber_eats.name)

print(uber_eats)  # class name @ hash code
print(uber_eats.order(from_restaurant="Tim Hortons",
                      time_of_order=2, order_total=10,
                      distance_from_restaurant=1 ))
