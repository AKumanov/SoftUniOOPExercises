from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
<<<<<<< HEAD
    __PORTION = 245

    def __init__(self, name, price):
        super().__init__(name, self.__PORTION, price)
=======
    def __init__(self, name: str, price: float):
        super().__init__(name, 245, price)
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
