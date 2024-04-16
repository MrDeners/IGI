import numpy as np

class NumPy:
    @staticmethod
    def matrix_random_create(n, m):
        """
        Creates a random matrix of size n x m with integer elements between 0 and 10.

        Parameters:
        n (int): Number of rows in the matrix.
        m (int): Number of columns in the matrix.

        Returns:
        numpy.ndarray: Random matrix of size n x m.
        """
        return np.random.randint(0, 10, (n, m))

    @staticmethod
    def matrix_create():
        """
        Creates a matrix with predefined values.

        Returns:
        numpy.ndarray: Matrix with predefined values.
        """
        return np.array([[1, 2, 3], [4, 5, 6]])

    @staticmethod
    def matrix_print_element(a):
        """
        Prints the sine of the given element.

        Parameters:
        a (float): Element to calculate the sine of.

        Returns:
        float: Sine of the element.
        """
        return np.sin(a)

    @staticmethod
    def array_zeros():
        """
        Creates a matrix of zeros with size 3 x 3.

        Returns:
        numpy.ndarray: Matrix of zeros with size 3 x 3.
        """
        return np.zeros((3, 3))

    @staticmethod
    def element_array_sum(a, b):
        """
        Calculates the sum of the given arrays element-wise.

        Parameters:
        a (numpy.ndarray): First array.
        b (numpy.ndarray): Second array.

        Returns:
        numpy.ndarray: Array with the element-wise sum of a and b.
        """
        return a + b

    @staticmethod
    def element_mul(a, multiplier):
        """
        Multiplies each element of the given array by the given multiplier.

        Parameters:
        a (numpy.ndarray): Array to be multiplied.
        multiplier (float): Multiplier value.

        Returns:
        numpy.ndarray: Array with each element multiplied by the multiplier.
        """
        return a * multiplier