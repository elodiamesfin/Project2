
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
