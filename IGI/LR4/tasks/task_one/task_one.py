from .rational_number_manager import *
from .rational_number import *
from .input_service import *


def first_task():
    """
        This function performs the first task.

        It creates a RationalNumberManager object and adds two rational numbers to it.
        It then saves the rational numbers to a CSV file and a pickle file.
        Finally, it loads the rational numbers from the CSV file and prints them,
        and then loads the rational numbers from the pickle file and prints them.
        """

    rational_manager = RationalNumberManager()

    rational_number = RationalNumber(10, 5)
    rational_manager.add_rational_number(10, rational_number)
    rational_number = Input.input_data()
    rational_manager.add_rational_number(5, rational_number)

    rational_manager.save_to_csv('rational_numbers.csv')
    rational_manager.save_to_pickle('rational_numbers.pkl')

    rational_manager.rational_numbers = {}
    rational_manager.load_from_csv('rational_numbers.csv')
    print("After download from CSV File:", rational_manager.rational_numbers)

    rational_manager.rational_numbers = {}
    rational_manager.load_from_pickle('rational_numbers.pkl')
    print("After download from pickle File:", rational_manager.rational_numbers)
