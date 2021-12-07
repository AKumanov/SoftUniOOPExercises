class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest


class WorkerTests(unittest.TestCase):
    def test_correct_initialization(self):
        worker = Worker("Test", 20, 10)
        self.assertEqual(worker.name, "Test")
        self.assertEqual(worker.salary, 20)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_energy_incremented(self):
        worker = Worker("Test", 20, 10)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_worker_energy_works(self):
        # arrange
        worker = Worker("Test", 20, 0)
        # act
        with self.assertRaises(Exception) as ex:
            worker.work()
        # assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_work_works_properly(self):
        # arrange
        worker = Worker("Test", 20, 10)
        # act
        worker.work()
        # assert
        self.assertEqual(worker.salary, worker.money)
        self.assertEqual(20, worker.money)

    def test_worker_energy_decreased_after_work(self):
        # arrange
        worker = Worker("Test", 20, 10)
        # act
        worker.work()
        # assert
        self.assertEqual(9, worker.energy)

    def test_get_info_method(self):
        # arrange
        worker = Worker("Test", 20, 10)
        # act and assert
        self.assertEqual("Test has saved 0 money.", worker.get_info())
        worker.work()
        self.assertEqual("Test has saved 20 money.", worker.get_info())




if __name__ == '__main__':
    unittest.main()
