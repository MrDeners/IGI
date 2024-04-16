import numpy as np


class MatrixProcessing:
    @staticmethod
    def el_exchange(arr):
        """
                Exchanges elements of the matrix arr with the maximum element in the row.

                Parameters:
                arr (numpy.ndarray): Input matrix.

                Returns:
                numpy.ndarray: Matrix with the exchanged elements.
                """
        for i in range(arr.shape[0]):
            max_elem = np.max(arr[i, :])
            max_idx = np.argmax(arr[i, :])
            arr[i, max_idx] = arr[i, i]
            arr[i, i] = max_elem
        return arr

    @staticmethod
    def median_main_diag(arr):
        """
                Computes the median of the values on the diagonal of the matrix arr.

                Parameters:
                arr (numpy.ndarray): Input matrix.

                Returns:
                float: The median value.
                """
        diag_elements = np.diag(arr)

        sorted_diag_elements = np.sort(diag_elements)

        if len(sorted_diag_elements) % 2 == 0:
            median_manual = (sorted_diag_elements[len(sorted_diag_elements) // 2 - 1] + sorted_diag_elements[
                len(sorted_diag_elements) // 2]) / 2
        else:
            median_manual = sorted_diag_elements[len(sorted_diag_elements) // 2]

        return median_manual
