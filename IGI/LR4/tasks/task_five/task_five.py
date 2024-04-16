import numpy as np
from .matrix_processing import MatrixProcessing
from .num_py import NumPy
from .static_math import StaticMath

def fifth_task():
    """
    Performs the fifth task by generating a random matrix, exchanging elements, calculating the median using NumPy, and a custom function.

    The function prints the element at index (1, 2) of the generated random matrix, a slice of the matrix, and then creates a new random matrix using NumPy.
    It exchanges elements of the matrix using the MatrixProcessing class method el_exchange, calculates the median of the diagonal elements using NumPy and the MatrixProcessing method median_main_diag.
    Finally, it prints out the calculated medians.

    Parameters:
    None

    Returns:
    None
    """
    n = 3
    m = 4

    a = np.random.randint(0, 10, (n, m))
    print(a[1, 2])
    print(a[1:3, 1:4])

    arr = NumPy.matrix_random_create(3, 4)
    arr = MatrixProcessing.el_exchange(arr)
    diag_elements = np.diag(arr)
    median_std = np.median(diag_elements)
    median_manual = MatrixProcessing.median_main_diag(arr)
    print("Median (NumPy):", median_std)
    print("Median (Function):", median_manual)