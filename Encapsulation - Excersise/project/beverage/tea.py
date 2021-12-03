from Lecture.project import HotBeverage


class Tea(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name):
        super().__init__(name, Tea.PRICE, Tea.MILLILITERS)
