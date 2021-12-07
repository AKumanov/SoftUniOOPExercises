from project.drink.drink import Drink


class Water(Drink):
<<<<<<< HEAD
    __PRICE = 1.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.__PRICE, brand)
=======
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 1.50, brand)
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
