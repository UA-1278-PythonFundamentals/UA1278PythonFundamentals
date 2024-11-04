# Regular Ball Super Ball
class Ball(object):

    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# Color Ghost
from random import choice


class Ghost(object):

    colors = ['white', 'yellow', 'purple', 'red']

    def __init__(self):
        self.color = choice(Ghost.colors)


# Basic subclasses - Adam and Eve
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# Classy Classes
class Person:

    def __init__(self, name: str, age: int):
        self.info = f"{name}s age is {age}"


# Building Spheres
from math import pi


class Sphere(object):

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * pi * pow(self.radius, 3), 5)

    def get_surface_area(self):
        return round(4 * pi * pow(self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


# Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
        return cls.__name__
    else:
        raise TypeError('Class name allows only alphanumeric chars (upper & lower letters plus ciphers).')

