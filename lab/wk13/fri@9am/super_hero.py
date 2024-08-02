class SuperHero:
    def __init__(self, name="SuperHero", strength=10.0):
        self.name = name
        self.strength = strength

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value if isinstance(value, str) \
            and len(value) > 4 else "SuperHero"

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        self.__strength = value if (isinstance(value, int) \
                                    or isinstance(value, float)) \
            and value >= 10 else 10

    def __str__(self):
        return f"Name: {self.name}, Strength: {self.strength}"

    def __add__(self, other):
        if isinstance(other, SuperHero):
            return SuperHero(name=self.name + "-" + other.name,
                             strength=(self.strength + other.strength)/2
                             )
        else:
            return "I don't know what to do here. Please " \
                    "add two SuperHeros together"

