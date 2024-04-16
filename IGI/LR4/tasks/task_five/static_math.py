import numpy as np

class StaticMath:
    @staticmethod
    def mean(a):
        """
        Calculates the mean of the elements in the input array.

        Parameters:
        a (numpy.ndarray): Input array.

        Returns:
        float: Mean of the input array.
        """
        return np.mean(a)

    @staticmethod
    def median(a):
        """
        Calculates the median of the elements in the input array.

        Parameters:
        a (numpy.ndarray): Input array.

        Returns:
        float: Median of the input array.
        """
        return np.median(a)

    @staticmethod
    def variance(a):
        """
        Calculates the variance of the elements in the input array.

        Parameters:
        a (numpy.ndarray): Input array.

        Returns:
        float: Variance of the input array.
        """
        return np.var(a)

    @staticmethod
    def standard_deviation(a):
        """
        Calculates the standard deviation of the elements in the input array.

        Parameters:
        a (numpy.ndarray): Input array.

        Returns:
        float: Standard deviation of the input array.
        """
        return np.std(a)