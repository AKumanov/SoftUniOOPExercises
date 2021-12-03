from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TableRepository:
    def __init__(self):
        pass

    @staticmethod
    def create_table(table_type: str, table_number: int, capacity: int):
        """ possible table types: InsideTable, OutsideTable """
        if table_type == InsideTable.__name__:
            return InsideTable(table_number, capacity)
        if table_type == OutsideTable.__name__:
            return OutsideTable(table_number, capacity)
