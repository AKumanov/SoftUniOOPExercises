from Lecture.project import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories: float):
        self.__calories = calories
        super().__init__(name, price, grams)
