from areas import *

shape = input("Enter the shape of the figure \
(rectangle a b, triangle b h, circle r) with dimentions: \n \
Example: rectangle 5 10 \n \
Example: triangle 5 10 \n \
Example: circle 5 \n").split()

match shape:
  case "rectangle", a, b:
    print(f"The area of the rectangle is {area_of_rectangle(int(a), int(b))}")
  case "triangle", b, h:
    print(f"The area of the triangle is {area_of_triangle(int(b), int(h))}")
  case "circle", r:
    print(F"The area of the circle is {area_of_circle(int(r))}")
  case _:
    print(f"Invalid input: {shape}")