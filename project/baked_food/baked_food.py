from abc import ABC, abstractmethod

<<<<<<< HEAD
from project.utils import check_string_empty_or_white_space


class BakedFood(ABC):
    __INVALID_NAME_MESSAGE = 'Name cannot be empty string or white space!'
    __INVALID_PRICE_MESSAGE = 'Price cannot be less than or equal to zero!'

    @abstractmethod
    def __init__(self, name, portion, price):
=======
from project.common.validator import Validator


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
        self.name = name
        self.portion = portion
        self.price = price

<<<<<<< HEAD
    @classmethod
    def __validate_name(cls, value):
        if not check_string_empty_or_white_space(value):
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_price(cls, value):
        if value <= 0:
            raise ValueError(cls.__INVALID_PRICE_MESSAGE)

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

=======
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
<<<<<<< HEAD
        self.__validate_name(value)
=======
        Validator.validate_string(value, "Name cannot be empty string or white space!")
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
<<<<<<< HEAD
        self.__validate_price(value)
        self.__price = value
=======
        Validator.validate_integer(value, "Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
