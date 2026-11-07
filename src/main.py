
"""Main entry point for Expense Tracker application."""

from ui.cli_user_interface import CliUserInterface


def main()->None:
    """Runs the Expense Tracker application."""
    user_interface = CliUserInterface()
    user_interface.display_menu()



if __name__ == "__main__":
    main()
