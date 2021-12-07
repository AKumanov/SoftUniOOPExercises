class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: int, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = __class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        needed_fuel = self.calculate_needed_fuel(kilometers)
        if not needed_fuel > self.fuel:
            self.fuel -= needed_fuel

    def calculate_needed_fuel(self, kilometers):
        needed_fuel = self.fuel_consumption * kilometers
        return needed_fuel
