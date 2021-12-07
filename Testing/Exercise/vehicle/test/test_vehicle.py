from unittest import TestCase, main

from project_vehicle_.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(12.5, 10.5)

    def test_initializer_working_correctly(self):
        self.assertEqual(12.5, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.horse_power)
        self.assertEqual(12.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def calculates_correctly_needed_fuel_for_trip(self):
        expected = 10
        result = 12.5 / self.vehicle.fuel_consumption
        self.assertEqual(expected, result)

    def test_drive_method_subtract_properly_fuel(self):
        kilometers = 1
        expected = 11.25
        self.vehicle.drive(kilometers)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_drive_calculates_proper_fuel_needed_for_trip(self):
        expected = 1.25
        prior = self.vehicle.fuel
        self.vehicle.drive(1)
        self.assertEqual(expected, prior - self.vehicle.fuel)

    def test_drive_with_10_1__kilometers_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10.1)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_method_raises_when_fuel_above_capacity(self):
        self.vehicle.drive(1)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1.26)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_makes_fuel_from_11_25_to_12_5(self):
        prior = self.vehicle.fuel
        self.vehicle.drive(1)
        self.vehicle.refuel(1.25)
        new = self.vehicle.fuel
        self.assertEqual(prior, new)

    def test_string_method_returns_the_proper_message(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == '__main__':
    main()
