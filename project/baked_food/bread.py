from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
<<<<<<< HEAD
    __PORTION = 200

    def __init__(self, name, price):
        super().__init__(name, self.__PORTION, price)
=======
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
