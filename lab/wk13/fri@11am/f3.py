class SuperHero:
    def __init__(self, name: str, strength:float):
        self.name = name
        self.strength = strength

    def __str__(self):
        return f"Name: {self.name}, Strength: {self.strength}"

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperHero(name=self.name * other,
                             strength=self.strength * other)

batman = SuperHero("Batman", 10)

print(batman)

double_batman = batman * 5
print(double_batman)

