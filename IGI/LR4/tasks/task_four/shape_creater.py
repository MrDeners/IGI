from .geometric_shape import *


class ShapeCreater:
    """
        This class provides methods for creating geometric shapes.
        """
    @staticmethod
    def rectangle():
        """
                Creates a rectangle with the specified width, height, and color.

                Parameters:
                - None

                Returns:
                - A Rectangle object with the specified width, height, and color.
                """
        color = input("Input rectangle color: ")
        color = color.lower()
        while True:
            try:
                width = int(input("Input rectangle width: "))
                height = int(input("Input rectangle height: "))
                if width > 0 and height > 0:
                    break
                print("Input positive numbers")
            except ValueError:
                print("Input only number")
        return Rectangle(color, width, height)

    @staticmethod
    def circle():
        """
                Creates a rectangle with the specified width, height, and color.

                Parameters:
                - None

                Returns:
                - A Rectangle object with the specified width, height, and color.
                """
        color = input("Input rectangle color: ")
        color = color.lower()
        while True:
            try:
                r = int(input("Input radius: "))
                if r > 0:
                    break
                print("Input positive numbers")
            except ValueError:
                print("Input only number")

                while True:
                    try:
                        r = int(input("Input radius: "))
                        break
                    except ValueError:
                        print("Input int number:")
        return Circle(color, r)