


import math


def calculating(x, eps, math_res):
    # Function to calculate the result of a series based on input values x, eps, and math_res
    """
    This function calculates the result of a series based on input values x, eps, and math_res.

    Parameters:
    - x (int): The input value x.
    - eps (float): The epsilon value for calculation.
    - math_res (float): The mathematical result for comparison.

    Returns:
    - Tuple (float, int): The calculated result and the number of iterations.
    """
    divider = 1
    res = 0
    for n in range(500):
        divider = (divider * n) if n != 0 else divider
        steep = x ** n / divider
        res += steep

        if abs(res - math_res) <= eps:
            return res, n
    return res, 500


def result_print(x, eps, res, math_res):
    # Function to print the result in a table format with headers and data
    """
    This function prints the result in a table format with headers and data.

    Parameters:
    - x (int): The input value x.
    - eps (float): The epsilon value used for calculation.
    - res (Tuple[float, int]): The result of the calculation and the number of iterations.
    - math_res (float): The mathematical result for comparison.

    Returns:
    - None
    """
    print("{:<10} {:<10} {:<5} {:<10} {:<5}".format("x", "n", "F(x)", "Math F(x)", "eps"))
    print("{:<10} {:<10} {:.5f} {:.5f} {:<5}".format(x, res[1], res[0], math_res, eps))


def float_validator(func):
    """
    This function is a decorator that validates floating point input.

    Parameters:
    - func (function): The function to be decorated that processes the input.

    Returns:
    - function: The wrapper function that handles input validation.
    """

    def wrapper(el):
        while True:
            try:
                el = input("Input eps:")
                result = func(el)
                break
            except ValueError:
                print("ERROR: Not a number entered")
        return result

    return wrapper


@float_validator
def floating_string(el):
    """
    This function converts the input string to a floating-point number.

    Parameters:
    - el (str): The input string to be converted to a float.

    Returns:
    - float: The converted floating-point number.
    """
    return float(el)


def first_task():
    # Function to process the expression by taking input values, calculating the mathematical result, and printing
    # the final result
    """
    This function processes the expression by taking input values, calculating the mathematical result,
    and printing the final result.

    Returns:
    - None
    """
    while True:
        try:
            x = int(input("Input x:"))
            break
        except ValueError:
            print("ERROR: Not a number entered")

    eps = floating_string('')
    math_res = math.exp(x)
    res = calculating(x, eps, math_res)
    result_print(x, eps, res, math_res)
