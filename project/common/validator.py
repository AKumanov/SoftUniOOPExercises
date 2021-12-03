class Validator:
    def __init__(self):
        pass

    @staticmethod
    def validate_string(value, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def validate_integer(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def validate_inside_table_number(value, message):
        if not 1 <= value <= 50:
            raise ValueError(message)

    @staticmethod
    def validate_outside_table_number(value, message):
        if not 51 <= value <= 100:
            raise ValueError(message)
