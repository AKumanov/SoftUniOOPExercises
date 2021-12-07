from project.worker import Worker


class Caretaker(Worker):
    def __init__(self, name, age, salary: int):
        super().__init__(name, age, salary)
