from project.drink.drink import Drink


class Tea(Drink):
<<<<<<< HEAD
    __PRICE = 2.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.__PRICE, brand)
=======
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 2.50, brand)
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
