#######Task1##########
# class Ball():
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type
#
#     def ball_type(self):
#         return self.ball_type

#######Task2##########
# import random
# class Ghost(object):
#     def __init__ (self):
#          self.color = random.choice(["white", "yellow", "purple", "red"])



#######Task3##########
# class Human:
#     pass
#
# class Man(Human):
#     pass
#
# class Woman(Human):
#     pass
#
#
# def God():
#     m = Man()
#     w = Woman()
#     return [m, w]

#######Task4##########
# class Person:
#     def __init__(self, name, age):
#         self.info=f"{name}s age is {age}"
#
#######Task5##########
#
#
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = float(radius)
#         self.mass = float(mass)
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         return round(4 / 3 * 3.141592653589 * self.radius ** 3, 5)
#
#     def get_surface_area(self):
#         return round(4 * 3.141592653589 * self.radius ** 2, 5)
#
#     def get_density(self):
#         return round(self.mass / (4 / 3 * 3.141592653589 * self.radius ** 3), 5)
#
#######Task6##########
# def class_name_changer(cls, new_name):
#     if not new_name.isalnum() or not new_name[0].isupper():
#         raise "Value Error"
#     cls.__name__ = new_name
#     return cls