import random
import math
import re


# I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# II. Color-ghost
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# III. Basic-subclasses-Adam-and-Eve
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# V. Building Spheres
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * self.radius**3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)

    def get_density(self):
        return round(self.mass / (4 / 3 * math.pi * self.radius**3), 5)


# VI. Dynamic Classes
def class_name_changer(cls, new_name):
    if not re.match(r"^[A-Z][a-zA-Z0-9]*$", new_name):
        raise ValueError(
            "Class name must start with an uppercase letter and contain only alphanumeric characters."
        )

    cls.__name__ = new_name
    return cls
