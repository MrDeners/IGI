# Author - Malush Denis BSUIR IaPT 253501      Created - 01.04.2024
# Laboratory Work - #3
# Python Studying   Version - 1.0.0 (Release)
# The Best program for Python Studying


import math


def calculating(x, eps, math_res):
    # Function to calculate the result of a series based on input values x, eps, and math_res
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
    print("{:<10} {:<10} {:<5} {:<10} {:<5}".format("x", "n", "F(x)", "Math F(x)", "eps"))
    print("{:<10} {:<10} {:.5f} {:.5f} {:<5}".format(x, res[1], res[0], math_res, eps))


def float_validator(func):
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
    return float(el)


def first_task():
    # Function to process the expression by taking input values, calculating the mathematical result, and printing
    # the final result

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
