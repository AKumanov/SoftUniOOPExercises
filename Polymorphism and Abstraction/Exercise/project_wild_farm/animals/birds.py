from project_wild_farm.animals.animal import Bird
from project_wild_farm.food import Meat, Seed, Vegetable, Fruit


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.good_food = [Meat]
        self.weight_per_quantity = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.good_food = [Meat, Fruit, Vegetable, Seed]
        self.weight_per_quantity = 0.35

    def make_sound(self):
        return "Cluck"
