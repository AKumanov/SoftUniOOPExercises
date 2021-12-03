class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity >= len(self.animals) + 1:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__animal_capacity >= len(self.animals) + 1 and not self.__budget >= price:
            return "Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity >= len(self.workers) + 1:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum([w.salary for w in self.workers])
        if not needed_money > self.__budget:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = sum([a.money_for_care for a in self.animals])
        if not needed_money > self.__budget:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        final = list()
        final.append(f"You have {len(self.animals)} animals")

        final.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            final.append(lion.__repr__())

        final.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            final.append(tiger.__repr__())

        final.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            final.append(cheetah.__repr__())

        return '\n'.join(final)

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        final = list()
        final.append(f"You have {len(self.workers)} workers")

        final.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            final.append(keeper.__repr__())

        final.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            final.append(caretaker.__repr__())

        final.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            final.append(vet.__repr__())

        return '\n'.join(final)
