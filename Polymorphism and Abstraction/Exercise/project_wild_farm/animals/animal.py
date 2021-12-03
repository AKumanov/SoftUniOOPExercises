from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten
        self.good_food = None
        self.weight_per_quantity = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if type(food) not in self.good_food:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += (food.quantity * self.weight_per_quantity)
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        self.wing_size = wing_size
        super().__init__(name, weight)

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region: str):
        self.living_region = living_region
        super().__init__(name, weight)

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
