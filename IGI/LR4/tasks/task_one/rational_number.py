class RationalNumber:
    """
        A class representing a rational number.

        Attributes:
        - isRational (bool): Indicates if the number is rational.
        - numerator (int): The numerator of the rational number.
        - denominator (int): The denominator of the rational number.
        """
    isRational = True

    def __init__(self, numerator, denominator):
        """
                Initialize a RationalNumber object with a numerator and a denominator.

                Parameters:
                - numerator (int): The numerator of the rational number.
                - denominator (int): The denominator of the rational number.
                """
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        """
                Return a string representation of the RationalNumber object.

                Returns:
                str: A string representation of the object in the format 'RationalNumber(numerator=..., denominator=...)'
                """
        return f'RationalNumber(numerator={self.numerator}, denominator={self.denominator})'

