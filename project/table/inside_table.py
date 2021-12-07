<<<<<<< HEAD
=======
from project.common.validator import Validator
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
from project.table.table import Table


class InsideTable(Table):
<<<<<<< HEAD
    _INVALID_TABLE_NUMBER_MESSAGE = 'Inside table\'s number must be between 1 and 50 inclusive!'

    _MIN_TABLE_NUMBER = 1
    _MAX_TABLE_NUMBER = 50

=======
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
<<<<<<< HEAD
    def table_type(self):
        return 'InsideTable'
=======
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.validate_inside_table_number(value,
                                               message="Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
