from abc import ABC, abstractmethod
import math


class GeometricShape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    def __init__(self, color):
        """
        Initializes a geometric shape with a specified color.

        Parameters:
        - color: The color of the geometric shape.
        """
        self.color = color

    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate the area of the geometric shape.

        Parameters:
        - None

        Returns:
        - The area of the geometric shape.
        """
        pass


class Color:
    """
    Class representing the color of a geometric shape.
    """

    def __init__(self, color):
        """
        Initializes the color of a geometric shape.

        Parameters:
        - color: The color of the geometric shape.
        """
        self._color = color

    @property
    def color(self):
        return self._color


class Rectangle(GeometricShape):
    """
    Class representing a rectangle, a type of geometric shape.
    """

    shape_name = "Rectangle"

    def __init__(self, color, width, height):
        """
        Initializes a rectangle with a specified color, width, and height.

        Parameters:
        - color: The color of the rectangle.
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        super().__init__(Color(color))
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Calculates the area of the rectangle.

        Parameters:
        - None

        Returns:
        - The area of the rectangle.
        """
        return self.width * self.height

    def get_info(self):
        """
        Returns information about the rectangle.

        Parameters:
        - None

        Returns:
        - Information about the rectangle including shape name, color, width, height, and area.
        """
        return "{shape}: {color} color, width {width}, height {height}, area {area}".format(
            shape=self.shape_name, color=self.color.color, width=self.width,
            height=self.height, area=self.calculate_area()
        )

    def get_name(self):
        """
        Returns the name of the rectangle.

        Parameters:
        - None

        Returns:
        - The name of the rectangle.
        """
        return self.shape_name


class Circle(GeometricShape):
    """
    Class representing a circle, a type of geometric shape.
    """

    def __init__(self, color, radius):
        """
        Initializes a circle with a specified color and radius.

        Parameters:
        - color: The color of the circle.
        - radius: The radius of the circle.
        """
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        """
        Calculates the area of the circle.

        Parameters:
        - None

        Returns:
        - The area of the circle.
        """
        return math.pi * self.radius ** 2