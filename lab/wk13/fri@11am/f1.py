class Car:
    def __init__(self, make, model, year, color):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0
        self.__max_speed = 200

    @property
    def speed(self):
        return str(self.__speed) + " km/h"

    @speed.setter
    def speed(self, value):
        self.__speed = value if value >= 0 and value <= self.__max_speed else 0

    def accelerate(self, increase_speed_by):
        if self.__speed + increase_speed_by <= self.__max_speed:
            self.__speed += increase_speed_by




# buying an object = instantiate
# special method = constructor
# init in python

honda = Car(color="black", make="honda",
            year=2000, model='crv')

print(honda.color)
print(honda.make)
print(honda.model)

honda.model = "accent"
print(honda.model)

print(honda.speed)
honda.accelerate(80)
print(honda.speed)
honda.accelerate(100)
print(honda.speed)
honda.accelerate(50)
print(honda.speed)

honda.speed = -50
print(honda.speed)
