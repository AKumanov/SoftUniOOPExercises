from project_vehicle_.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.sound = "Meow meow!"

    def make_sound(self):
        return self.sound
