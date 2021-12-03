from Lecture.project import Product


class Food(Product):
    def __init__(self, name, price, grams):
        self.grams = grams
        super().__init__(name, price)
