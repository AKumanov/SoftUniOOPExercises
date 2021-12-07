class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class ListTest(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 4, 6, 7, 3, 2)

    def test_add_operation_adding_properly(self):
        length = len(self.integer_list.get_data()) + 1
        self.integer_list.add(5)
        result = False
        if 5 in self.integer_list.get_data():
            result = True
        self.assertEqual(True, result)
        new_len = len(self.integer_list.get_data())
        self.assertEqual(length, new_len)

    def test_add_operation_returns_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(3.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_out_of_range_error(self):
        with self.assertRaises(IndexError) as ex:
            index = len(self.integer_list.get_data())
            self.integer_list.remove_index(index)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_element_working_properly(self):
        index = 3
        original_length = len(self.integer_list.get_data()) - 1
        item = self.integer_list.get_data()[index]
        self.assertEqual(7, item)
        item = self.integer_list.remove_index(index)
        new_length = len(self.integer_list.get_data())
        self.assertEqual(original_length, new_length)
        self.assertEqual(7, item)

    def test_initialization_takes_only_integers(self):
        self.integer_list.__init__(1, 2, 3, 3.2, str(8))
        self.assertEqual(3, len(self.integer_list.get_data()))

    def test_get_method_returns_specific_element(self):
        index = 3
        expected = 7
        found = self.integer_list.get(index)
        self.assertEqual(expected, found)
        index = 9
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(index)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_biggest_method_after_sort_works(self):
        found = self.integer_list.get_biggest()
        self.assertEqual(7, found)

    def test_get_index_returns_the_correct_index(self):
        correct_index = 3
        found_index = self.integer_list.get_index(7)
        self.assertEqual(correct_index, found_index)


if __name__ == '__main__':
    unittest.main()
