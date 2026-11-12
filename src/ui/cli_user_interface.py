
"""Contains definition for CliUserInterface class."""

from application.expense_tracker import ExpenseTracker


class CliUserInterface:
    """Defines CliUserInterface Class."""

    def __init__(self):
        self._expense_tracker = ExpenseTracker()

    def display_menu(self)->None:
        print("\nExpense Tracker")
        print("1. Create Expense File")
        print("2. Open Expense File")
        print("3. Enter Expense")
        print("4. Print Expenses")
        print("5. Export Expenses")
        print("6. Exit")
        print("7. Filter Expenses by Category")
    
    def create_expense_file(self)->None:
        filename = input("Enter expense filename: ")
        self._expense_tracker.create_expense_file(filename)

    def enter_expense(self)->None:
        expense = {}
        expense["date"] = input("Enter expense date: ")
        expense["category"] = input("Enter expense category: ")
        expense["amount"] = float(input("Enter expense amount: "))
        self._expense_tracker.save_expense(expense)

    def open_expense_file(self)->None:
        filename = input("Enter expense filename: ")
        self._expense_tracker.open_expense_file(filename)


    def print_expenses(self)->None:
        self._expense_tracker.print_expenses()

    def filter_by_category(self)->None:
        category = input("Enter expense category to filter: ")
        self._expense_tracker.filter_by_category(category)
