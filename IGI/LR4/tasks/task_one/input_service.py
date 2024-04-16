from ..input_service import *
from .rational_number import *


class Input(InputService):
    """
        A class representing input service for rational numbers.

        This class provides methods for inputting rational numbers from the user.
        """
    @staticmethod
    def input_data():
        """
                Input a rational number from the user in the format 'numerator.denominator'.

                Returns:
                RationalNumber: A RationalNumber object representing the inputted rational number.

                Raises:
                ZeroDivisionError: If the user tries to divide by zero.
                """
        while True:
            try:
                data = input("Input number on next format (numerator.denominator): ")
                if all(char.isdigit() or char == '.' for char in data):
                    number = data.split(".")
                    zero_checker = int(number[0]) / int(number[1])
                    return RationalNumber(number[0], number[1])
                else:
                    print("Please input a valid number.")
            except ZeroDivisionError:
                print("Cannot divide by zero")
