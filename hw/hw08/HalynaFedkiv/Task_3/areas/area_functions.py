__all__ = ['rectangle_area', 'triangle_area', 'circle_area']

from math import pi


def rectangle_area(a, b):
    """
    Calculates the area of a rectangle
    :param a: int or float
    :param b: int or float
    :return: the area of a rectangle
    """
    return a*b


def triangle_area(a, b):
    """Calculates the area of a triangle
    :param a: int or float
    :param b: int or float
    :return: the area of a triangle"""
    return 0.5*a*b


def circle_area(r):
    """Calculates the area of a circle
    :param r: int or float
    :return: the area of a circle"""
    return pi*pow(r, 2)
