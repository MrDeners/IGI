import csv
from ..rational_number import RationalNumber


class CSVFileServiceMixin:
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for key, num in self.rational_numbers.items():
                writer.writerow([key, num.numerator, num.denominator])

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = int(row[0])
                numerator = int(row[1])
                denominator = int(row[2])
                self.rational_numbers[key] = RationalNumber(numerator, denominator)
