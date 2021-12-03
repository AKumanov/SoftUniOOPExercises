class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")

        self.sleepy = False


import unittest


class CatTest(unittest.TestCase):
    def test_cat_size_increases_after_eating(self):
        # arrange
        cat = Cat("Tom")
        # act
        cat.eat()
        # assert
        self.assertEqual(1, cat.size)
        self.assertEqual(True, cat.fed)

    def test_cat_cannot_eat_after_already_fed_error(self):
        # arrange
        cat = Cat("Tom")
        # act
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
            # assert
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed_error(self):
        cat = Cat('Tom')
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_not_sleepy_after_sleep(self):
        cat = Cat("Tom")
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)


if __name__ == '__main__':
    unittest.main()
