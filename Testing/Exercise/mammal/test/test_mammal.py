from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Lion", "ROAR!")

    def test_init_method_attaches_name_type_sound(self):
        mam = Mammal("Test", "Lion", "ROAR!")
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("ROAR!", self.mammal.sound)
        self.assertEqual("animals", mam._Mammal__kingdom)

    def test_private_attribute_of_object(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_method_uses_sound_attribute(self):
        sound = self.mammal.sound
        expected = "ROAR!"
        self.assertEqual(f"Test makes {expected}", self.mammal.make_sound())
        self.assertIn(sound, self.mammal.make_sound())

    def test_get_kingdom_method_returns_the_correct_private_attribute(self):
        expected = "animals"
        result = self.mammal.get_kingdom()
        self.assertEqual(expected, result)
        self.assertIn(expected, result)

    def test_get_info_method_returns_the_correct_information(self):
        expected = "Test is of type Lion"
        type = self.mammal.type
        name = self.mammal.name
        self.assertEqual(expected, self.mammal.info())
        self.assertIn(type, self.mammal.info())
        self.assertIn(name, self.mammal.info())


if __name__ == '__main__':
    main()
