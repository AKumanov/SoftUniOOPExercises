<<<<<<< HEAD
=======
from project.common.validator import Validator
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
from project.table.table import Table


class OutsideTable(Table):
<<<<<<< HEAD
    _INVALID_TABLE_NUMBER_MESSAGE = 'Outside table\'s number must be between 51 and 100 inclusive!'

    _MIN_TABLE_NUMBER = 51
    _MAX_TABLE_NUMBER = 100

=======
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
<<<<<<< HEAD
    def table_type(self):
        return 'OutsideTable'
=======
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.validate_outside_table_number(value,
                                                message="Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
