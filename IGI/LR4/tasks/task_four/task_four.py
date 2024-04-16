from .drawer import *
from .shape_creater import *


def fourth_task():
    """
        This function creates a rectangle using ShapeCreater, draws it using Drawer, and converts the image to ASCII art.

        Parameters:
        - None

        Returns:
        - None
        """

    # rectangle = ShapeCreater.rectangle()
    circle = ShapeCreater.circle()

    Drawer.draw_square_in_circle(circle.radius, circle.color)


if __name__ == "__main__":
    fourth_task()
