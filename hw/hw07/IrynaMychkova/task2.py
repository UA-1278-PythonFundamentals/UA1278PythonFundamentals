# Task2. Write a program that calculates the area of a rectangle, 
# triangle and circle (write three functions to calculate the area. 
# And call them in the main program depending on the user's choice).
from math import pi

def rectangle(a: int, b: int) -> int:
  """
  This function calculates the area of a rectangle
  :param a: int
  :param b: int
  :return: int
  """
  return a * b

def triangle(b: int, h: int) -> int:
  """
  This function calculates the area of a triangle
  :param b: int
  :param h: int
  :return: int
  """
  return b * h / 2

def circle(r: int) -> int:
  """
  This function calculates the area of a circle
  "param r: int
  :return: float
  """
  return pi * r ** 2

shape = input("Enter the shape of the figure \
(rectangle a b, triangle b h, circle r) with dimentions: \n \
Example: rectangle 5 10 \n \
Example: triangle 5 10 \n \
Example: circle 5 \n").split()

match shape:
  case "rectangle", a, b:
    print(f"The area of the rectangle is {rectangle(int(a), int(b))}")
  case "triangle", b, h:
    print(f"The area of the triangle is {triangle(int(b), int(h))}")
  case "circle", r:
    print(F"The area of circle is {round(circle(int(r)))}")
  case _:
    print(f"Invalid input: {shape}")