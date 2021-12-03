# from project_wild_farm-static-static-lecture-Encapsulation.food.main_dish import MainDish
from Lecture.project import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)


s = Salmon("Salmon", 23.5)
print(s.__class__.__bases__[0].__name__)
