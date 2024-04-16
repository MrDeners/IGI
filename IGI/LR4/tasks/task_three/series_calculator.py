import matplotlib.pyplot as plt
import numpy as np
import statistics


class SeriesCalculator:
    """
        A class to calculate and visualize a series and its additional parameters.

        Attributes:
            x (int): The input value.
            eps (float): The epsilon value for convergence.
            math_res (float): The mathematical result for comparison.
        """
    def __init__(self, x, eps, math_res):
        """
                Initializes the SeriesCalculator with the input values.
                """
        self.x = x
        self.eps = eps
        self.math_res = math_res

    def calculate_series(self):
        """
                Calculate the series and return the result, number of iterations, and results.
                """
        divider = 1
        res = 0
        results = []
        for n in range(500):
            divider = (divider * n) if n != 0 else divider
            steep = self.x ** n / divider
            res += steep
            results.append(res)

            if abs(res - self.math_res) <= self.eps:
                return res, n, results
        return res, 500, results

    def plot_results(self, results):
        """
                Plot the results of the series and its convergence.
                """
        n_values = range(len(results))

        plt.plot(n_values, results, label="Series Result")
        plt.axhline(y=self.math_res, color='r', linestyle='--', label="Mathematical Result")
        plt.xlabel('n')
        plt.ylabel('Result')
        plt.title('Series Convergence')
        plt.legend()
        plt.grid(True)
        plt.savefig('series_plot.png')
        plt.show()

    @staticmethod
    def calculate_additional_parameters(results):
        """
                Calculate additional parameters of the series and print the results.
                """
        mean = statistics.mean(results)
        print(f"Mean: {mean}")
        median = statistics.median(results)
        print(f"Median: {median}")
        mode = statistics.mode(results)
        print(f"Mode: {mode}")
        variance = statistics.variance(results)
        print(f"Variance: {variance}")
        stdev = statistics.stdev(results)
        print(f"Stdev: {stdev}")
        return mean, median, mode, variance, stdev