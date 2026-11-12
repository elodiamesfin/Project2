
"""Contains definition for ExpenseTracker class."""

from persistence.file_persister import FilePersister


class ExpenseTracker:
    """Defines ExpenseTracker Class."""

    def __init__(self):
        self._file_persister = FilePersister()

    def create_expense_file(self, filename:str)->None:
        self._file_persister.create_expense_file(filename)

    def save_expense(self, expense:dict)->None:
        self._file_persister.save_expense(expense)

    def open_expense_file(self, filename:str)->None:
        self._file_persister.open_expense_file(filename)

    def print_expenses(self)->None:
        self._file_persister.print_expenses()

    def filter_by_category(self, category:str)->None:
        self._file_persister.filter_by_category(category)

    def filter_by_date_range(self, start_date:str, end_date:str)->None:
        self._file_persister.filter_by_date_range(start_date, end_date)
   
    def export_expenses(self, filename:str)->None:
        self._file_persister.export_expenses(filename)