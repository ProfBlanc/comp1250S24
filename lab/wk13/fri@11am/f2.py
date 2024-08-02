class Person:
    def __init__(self, name:str, fav_foods:list, energy_level:float):
        self.name = name
        self.fav_foods = fav_foods
        self.__energy_level = energy_level
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = "Person"
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
    @property
    def fav_foods(self):
        return self.__fav_foods
    @fav_foods.setter
    def fav_foods(self, value):
        self.__fav_foods = []

        if isinstance(value, list):
            self.__fav_foods = value if len([ x for x in value if isinstance(x, str)]) == len(value) else []

        # valid_values = True
        # if isinstance(value, list):
        #     for item in value:
        #         if not isinstance(item, str):
        #             valid_values = False
        #             break
        #
        #     if valid_values:
        #         self.__fav_foods = value





ben = Person("Ben",
             ["pizza", "pie","candy",  "broccoli"],
             90
             )

print(ben.fav_foods)
