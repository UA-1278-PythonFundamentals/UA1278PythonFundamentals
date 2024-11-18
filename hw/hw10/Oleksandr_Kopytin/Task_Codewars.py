# Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Color-ghost
import random

colors = ["white", "yellow", "purple", "red"]


class Ghost(object):
    def __init__(self):
        self.color = random.choice(colors)


# Basic-subclasses-Adam-and-Eve
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# Classy-classes
class Person:
    def __init__(self, name, age):
        self._info = f"{name}s age is {age}"

    @property
    def info(self):
        return self._info

    @info.setter
    def set_info(self, name, age):
        self._info = f"{name}s age is {age}"


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
        return round(((4 / 3) * pi * self.radius ** 3), 5)

    def get_surface_area(self):
        return round((4 * pi * self.radius ** 2), 5)

    def get_density(self):
        return round((self.mass / self.get_volume()), 5)


# Dynamic Classes
def class_name_changer(cls, new_name):
    if new_name[0].isalpha() and new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid name")
