import os
from geometric_lib import circle

radius = float(os.getenv('RADIUS', 7))

print("Площадь круга: ", circle.area(radius))

print("Периметр круга: ", circle.perimeter(radius))
