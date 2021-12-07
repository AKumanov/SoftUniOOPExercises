from abc import ABC, abstractmethod

<<<<<<< HEAD
from project.utils import is_positive, check_string_empty_or_white_space


class Drink(ABC):
    __INVALID_NAME_MESSAGE = 'Name cannot be empty string or white space!'
    __INVALID_PORTION_MESSAGE = 'Portion cannot be less than or equal to zero!'
    __INVALID_BRAND_MESSAGE = 'Brand cannot be empty string or white space!'

    @abstractmethod
    def __init__(self, name, portion, price, brand):
=======
from project.common.validator import Validator


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

<<<<<<< HEAD
    @classmethod
    def __validate_name(cls, value):
        if not check_string_empty_or_white_space(value):
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_portion(cls, value):
        if not is_positive(value):
            raise ValueError(cls.__INVALID_PORTION_MESSAGE)

    @classmethod
    def __validate_brand(cls, value):
        if not check_string_empty_or_white_space(value):
            raise ValueError(cls.__INVALID_BRAND_MESSAGE)

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"

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
        Validator.validate_string(value, message="Name cannot be empty string or white space!")
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
<<<<<<< HEAD
        self.__validate_portion(value)
=======
        Validator.validate_integer(value, message="Portion cannot be less than or equal to zero!")
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
<<<<<<< HEAD
        self.__validate_brand(value)
        self.__brand = value
=======
        Validator.validate_string(value, message="Brand cannot be empty string or white space!")
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
>>>>>>> 568d84c65e9791ecadbc978a331d0b40f1497680
