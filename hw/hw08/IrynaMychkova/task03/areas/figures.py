from math import pi, pow

def area_of_circle(radius: float) -> float:
    """
    Calculate the area of a circle with a given radius.

    :param radius: the radius of the circle
    :return: the area of the circle
    """

    return round(pi * pow(radius, 2), 2)

def area_of_rectangle(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle with a given width and height.

    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :return: the area of the rectangle
    """

    return width * height

def area_of_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle with a given base and height.

    :param base: the base of the triangle
    :param height: the height of the triangle
    :return: the area of the triangle
    """

    return 0.5 * base * height