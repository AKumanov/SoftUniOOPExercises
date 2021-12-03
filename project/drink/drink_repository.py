from project.drink.tea import Tea
from project.drink.water import Water


class DrinkRepository:
    def __init__(self):
        pass

    @staticmethod
    def create_drink(drink_type: str, name: str, portion: float, brand: str):
        """ possible drink types are: Tea, Water """
        if drink_type == Tea.__name__:
            return Tea(name, portion, brand)
        if drink_type == Water.__name__:
            return Water(name, portion, brand)

