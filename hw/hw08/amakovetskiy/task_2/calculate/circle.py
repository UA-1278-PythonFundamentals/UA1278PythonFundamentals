import math
from math import pi, pow


def area_of_circle(radius):
    area = math.pi * math.pow(radius,2)
    return round(area, 1)


# print(area_of_circle(2))