
"""Main entry point for Expense Tracker application."""

from ui.cli_user_interface import CliUserInterface


def main()->None:
    """Runs the Expense Tracker application."""
    user_interface = CliUserInterface()

    while True:
        user_interface.display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            user_interface.create_expense_file()

        elif choice == "2":
            user_interface.open_expense_file()

        elif choice == "3":
            user_interface.enter_expense()

        elif choice == "4":
            user_interface.print_expenses()

        elif choice == "6":
            print("Exiting Expense Tracker.")
            break

        elif choice == "7":
            user_interface.filter_by_category()

        elif choice == "8":
            user_interface.filter_by_date_range()

if __name__ == "__main__":
    main()
