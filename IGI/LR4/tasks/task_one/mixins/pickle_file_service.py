import pickle
from ..rational_number import RationalNumber


class PickleFileServiceMixin:
    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.rational_numbers, file)

    def load_from_pickle(self, filename):
        with open(filename, 'rb') as file:
            self.rational_numbers = pickle.load(file)