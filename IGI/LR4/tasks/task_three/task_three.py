import math

from .printer import *
from .series_calculator import *


def third_task():
    """
        Perform the third task which involves inputting x and eps, calculating the series, printing the results,
        calculating additional parameters, and plotting the results.
        """
    while True:
        try:
            x = int(input("Input x:"))
            eps = float(input("Input eps:"))
            break
        except ValueError:
            print("ERROR: Not a number entered")

    math_res = math.exp(x)

    series_calc = SeriesCalculator(x, eps, math_res)

    res, n, results = series_calc.calculate_series()

    Printer.result_print(x, eps, (res, n), math_res)

    SeriesCalculator.calculate_additional_parameters(results)

    series_calc.plot_results(results)
