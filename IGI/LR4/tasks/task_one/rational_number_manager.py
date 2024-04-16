import csv
import pickle
from .rational_number import RationalNumber
from .mixins.mixin_importer import *


class RationalNumberManager(CSVFileServiceMixin, PickleFileServiceMixin):
    def __init__(self):
        """
                Initialize RationalNumberManager with an empty dictionary to store rational numbers.
                """
        self.rational_numbers = {}

    # Setter
    def add_rational_number(self, key, rational_number):
        """
                Add a rational number to the manager with a specified key.

                Parameters:
                key (int): The key to associate with the rational number.
                rational_number (RationalNumber): The rational number to add.
                """
        self.rational_numbers[key] = rational_number

    # Getter
    @property
    def get_rational_numbers(self):
        """
                Get all rational numbers stored in the manager.

                Returns:
                dict: A dictionary of rational numbers with keys.
                """
        return self.rational_numbers

    # Property
    @property
    def get_rational_numbers_x2(self):
        """
               Get all rational numbers multiplied by 2.

               Returns:
               map: A map object containing RationalNumber instances multiplied by 2.
               """
        return map(lambda x: RationalNumber(x.numerator * 2, x.denominator * 2), self.rational_numbers.values())

    def find_equal_numbers(self):
        """
                Check if there are equal rational numbers in the manager.

                Returns:
                bool: True if equal numbers are found, False otherwise.
                """
        seen = set()
        for key, num in self.rational_numbers.items():
            fraction = (num.numerator, num.denominator)
            if fraction in seen:
                return True
            seen.add(fraction)
        return False

    def find_largest_number(self):
        """
                Find the rational number with the largest value in the manager.

                Returns:
                RationalNumber: The rational number with the largest value.
                """
        max_value = max(self.rational_numbers.values(), key=lambda x: x.numerator / x.denominator)
        return max_value
