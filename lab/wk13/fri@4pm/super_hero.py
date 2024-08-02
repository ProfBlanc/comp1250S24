class SuperHero:
    def __init__(self, human_name, hero_name,
                 hero_power, hero_planet):

        self.human_name = human_name
        self.hero_name = hero_name
        self.hero_power = hero_power
        self.hero_planet = hero_planet


    def __str__(self):
        return (f'Name={self.human_name}, '
                f'Hero={self.hero_name}, '
                f'Power={self.hero_power}, '
                f'Planet={self.hero_planet}')


    def __mul__(self, other):
        # Operand1 OPERATOR Operand2
        # 1 + 2
        # batman * 2
        if isinstance(other, int):
            return SuperHero(
                human_name=self.human_name * other,
                hero_name=self.hero_name * other,
                hero_power = self.hero_power * other,
                hero_planet = self.hero_planet * other
                             )
        else:
            return "I don't know what to do here"
