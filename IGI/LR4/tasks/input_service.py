class InputService:
    """
        A generic input service class.

        This class provides a method to input data from the user.
        """
    @staticmethod
    def input_data():
        """
                Input data from the user.

                Returns:
                str: The data inputted by the user.
                """
        return input("Input your data: ")
