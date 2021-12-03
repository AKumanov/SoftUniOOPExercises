from project.baked_food.food_repository import FoodRepository
from project.common.validator import Validator
from project.drink.drink_repository import DrinkRepository
from project.table.table_repository import TableRepository


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = list()
        self.drinks_menu = list()
        self.tables_repository = list()
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_string(value, message="Name cannot be empty string or white space!")
        self.__name = value

    def find_food_by_name(self, name: str):
        for food in self.food_menu:
            if food.name == name:
                return food
        return None

    def find_drink_by_name(self, name: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink
        return None

    def find_table_by_number(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def find_first_not_reserved_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                return table

    def add_food(self, food_type: str, name: str, price: float):
        if self.find_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = FoodRepository.create_food(food_type, name, price)
        if food:
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if self.find_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = DrinkRepository.create_drink(drink_type, name, portion, brand)
        if drink:
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.find_table_by_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = TableRepository.create_table(table_type, table_number, capacity)
        if table:
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.find_first_not_reserved_table(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_name):
        ordered_food = []
        unordered_food = []
        food_name_data = list(food_name)
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        for food_name in food_name_data:
            food = self.find_food_by_name(food_name)
            if food:
                ordered_food.append(food)
                table.order_food(food)
            else:
                unordered_food.append(food_name)
        output = f"Table {table_number} ordered:\n"
        for food in ordered_food:
            output += f"{str(food)}\n"
        output += f"{self.name} does not have in the menu:\n"
        for food in unordered_food:
            output += f"{food}\n"
        return output.strip()

    def order_drink(self, table_number: int, *drinks_name):
        drinks_name_data = list(drinks_name)
        ordered_drinks = []
        unordered_drinks = []
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        for drink_name in drinks_name_data:
            drink = self.find_drink_by_name(drink_name)
            if drink:
                ordered_drinks.append(drink)
                table.order_drink(drink)
            else:
                unordered_drinks.append(drink_name)
        output = f"Table {table_number} ordered:\n"
        for drink in ordered_drinks:
            output += f"{str(drink)}\n"
        output += f"{self.name} does not have in the menu:\n"
        for unordered_drink_name in unordered_drinks:
            output += f"{unordered_drink_name}\n"

        return output.strip()

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        output = f"Table: {table_number}\n"
        output += f"Bill: {bill:.2f}"
        table.clear()
        return output.strip()



    def get_free_tables_info(self):
        output = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                output += f"{table.free_table_info()}"
        return output.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
