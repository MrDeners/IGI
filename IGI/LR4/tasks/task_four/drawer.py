from PIL import Image, ImageDraw
from .geometric_shape import *


class Drawer:
    """
    Class providing methods for drawing geometric shapes and converting images to ASCII art.
    """

    @staticmethod
    def draw(rectangle):
        """
        Draws a rectangle on an image and saves it as a PNG file.

        Parameters:
        - rectangle: The rectangle object to be drawn.

        Returns:
        - None
        """
        image = Image.new("RGB", (int(rectangle.width), int(rectangle.height)), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle([0, 0, int(rectangle.width), int(rectangle.height)], fill=rectangle.color.color)
        image.save("rectangle.png")
        image.show()

    @staticmethod
    def draw_square_in_circle(circle_radius, color):
        R = circle_radius
        cx, cy = R, R
        square_side = R * 2 ** 0.5

        top_left = (cx - square_side / 2, cy - square_side / 2)
        bottom_right = (cx + square_side / 2, cy + square_side / 2)

        image = Image.new("RGB", (2 * R, 2 * R), "white")
        draw = ImageDraw.Draw(image)

        draw.rectangle([top_left[0], top_left[1], bottom_right[0], bottom_right[1]], outline="black", fill=color)

        draw.ellipse([cx - R, cy - R, cx + R, cy + R], outline="black")

        image.save("square_in_circle.png")
        image.show()

    @staticmethod
    def image_to_ascii(image_path, cols=120):
        """
        Converts an image to ASCII art.

        Parameters:
        - image_path: The path to the image file.
        - cols: The number of columns for the ASCII art (default is 120).

        Returns:
        - ASCII representation of the image.
        """
        img = Image.open(image_path)
        img = img.resize((cols, int(cols * img.size[1] / img.size[0])))
        img = img.convert('L')

        ascii_chars = '@%#*+=-:. '

        ascii_image = ""
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                pixel_value = img.getpixel((j, i))
                ascii_image += ascii_chars[pixel_value // 32]
            ascii_image += "\n"

        return ascii_image
