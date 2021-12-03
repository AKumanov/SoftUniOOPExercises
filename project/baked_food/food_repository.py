from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class FoodRepository:
    def __init__(self):
        pass

    @staticmethod
    def create_food(food_type: str, name: str, price: float):
        """ possible food types: Bread, Cake"""
        if food_type == Bread.__name__:
            return Bread(name, price)
        if food_type == Cake.__name__:
            return Cake(name, price)
