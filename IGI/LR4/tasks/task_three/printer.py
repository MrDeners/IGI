class Printer:
    @staticmethod
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