from project_wild_farm.animals.animal import Mammal
from project_wild_farm.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.good_food = [Vegetable, Fruit]
        self.weight_per_quantity = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.good_food = [Meat]
        self.weight_per_quantity = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.good_food = [Vegetable, Meat]
        self.weight_per_quantity = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.good_food = [Meat]
        self.weight_per_quantity = 1

    def make_sound(self):
        return "ROAR!!!"
