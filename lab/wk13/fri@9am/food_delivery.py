class FoodDelivery:
    """
    name
    date_created
    hours_available
    available_restaurants
    distance_limitation
    min_order_amount
    food_price
    delivery_charge
    total_price
    """
    def __init__(self, name, hours_available
                 , distance_limitation, min_order_amount,
                 available_restaurants):
        self.name = name
        self.hours_available = hours_available
        self.food_price = 0
        self.delivery_charge = 0
        self.total_price = 0
        self.distance_limitation = distance_limitation
        self.min_order_amount = min_order_amount
        self.available_restaurants = available_restaurants

    @property  # a method that behaves like a property  only to GET the value
    def name(self):
        return self.__name

    @name.setter
    def name(self, potential_value):
        self.__name = "Default Food Delivery Service"
        if isinstance(potential_value, str) and len(potential_value) >=5 and potential_value.isalpha():
            self.__name = potential_value

    @property
    def available_restaurants(self):
        return self.__available_restaurants

    @available_restaurants.setter
    def available_restaurants(self, potential_value):
        self.__available_restaurants = []
        if isinstance(potential_value, list) and len(potential_value) >= 3:
            self.__available_restaurants = potential_value

    def __str__(self):
        return (f'Name={self.name}, Hours_Available={self.hours_available}, '
                f'Distance_Limitation={self.distance_limitation}, '
                f'Available_Restaurants={self.available_restaurants}, '
                f'Minimum_Order_Amount={self.min_order_amount}')

    def order(self, from_restaurant, time_of_order, order_total, distance_from_restaurant):
        if from_restaurant in self.available_restaurants and \
            time_of_order >= self.hours_available["open"] and time_of_order <= self.hours_available["close"] \
            and order_total >= self.min_order_amount and distance_from_restaurant <= self.distance_limitation:
                self.food_price = order_total
                self.delivery_charge = 0.15 * self.food_price
                self.total_price = (self.food_price + self.delivery_charge) * 1.13
                return "Order Completed", self.total_price
        return "Order failed!"
