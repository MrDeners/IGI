class BaseReader:
    """
    Base class for reading text from a file.

    This class provides a basic implementation for reading text from a file. It defines a `read` method that takes a file name
    and returns the contents of the file as a string.

    Attributes:
        text (str): The text read from the file.
    """
    def __init__(self, text):
        self.text = text

    @staticmethod
    def read(file_name):
        """
        Read text from a file.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            str: The contents of the file as a string.
        """
        with open(f'{file_name}.txt', 'r') as file:
            return file.read()


class AdvancedReader(BaseReader):
    """
    Advanced class for reading text from a file.

    This class extends the `BaseReader` class and provides an enhanced implementation for reading text from a file.
    It defines a `read` method that takes a file name and returns the contents of the file as a string.

    Attributes:
        text (str): The text read from the file.
        is_read (bool): Flag indicating if the text has been read.
    """
    is_read = False

    def __init__(self, text):
        super().__init__(text)

    @staticmethod
    def read(file_name):
        """
        Read text from a file.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            str: The contents of the file as a string.
        """
        with open(f'{file_name}.txt', 'r') as file:
            is_read = True
            return file.read()