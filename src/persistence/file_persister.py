
"""Contains definition for FilePersister class."""

import json
import csv


class FilePersister:
    """Defines FilePersister Class."""

    def __init__(self):
        self._active_expense_file = ""

    def create_expense_file(self, filename:str)->None:
        self._active_expense_file = filename
        print(f"Creating expense file: {filename}")
        header_dict = {}
        header_dict["app_name"] = "Expense Tracker"
        header_dict["version"] = "1.0"
        with open(filename, "w") as f:
            f.write(json.dumps(header_dict) + "\n")

    def save_expense(self, expense:dict)->None:
        with open(self._active_expense_file, "a") as f:
            f.write(json.dumps(expense) + "\n")

    def open_expense_file(self, filename:str)->None:
        with open(filename, "r") as f:
            print(f.read())
        self._active_expense_file = filename

    def print_expenses(self)->None:
        with open(self._active_expense_file, "r") as f:
            for line in f:
                expense = json.loads(line)
                if "date" in expense:
                    print(expense)

    def filter_by_category(self, category:str)->None:
        with open(self._active_expense_file, "r") as f:
            for line in f:
                expense = json.loads(line)
                if "category" in expense:
                    if expense["category"] == category:
                        print(expense)

    def filter_by_date_range(self, start_date:str, end_date:str)->None:
        with open(self._active_expense_file, "r") as f:
            for line in f:
                expense = json.loads(line)
                if "date" in expense:
                    if start_date <= expense["date"] <= end_date:
                        print(expense)

    def export_expenses(self, filename:str)->None:
        expenses = []
        with open(self._active_expense_file, "r") as f:
            for line in f:
                expense = json.loads(line)
                if "date" in expense:
                    expenses.append(expense)

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount"])

            for expense in expenses:
                writer.writerow([
                    expense["date"],
                    expense["category"],
                    expense["amount"]
                ])

        print(f"Expenses exported to {filename}")
