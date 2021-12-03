from project_vehicle_.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.sound = "Woof!"

    def make_sound(self):
        return self.sound
