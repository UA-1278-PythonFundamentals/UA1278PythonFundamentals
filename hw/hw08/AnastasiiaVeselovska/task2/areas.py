from math import pi
from math import pow

def area_of_rectangle(a_rectangle_number, b_number):
    s = a_rectangle_number * b_number
    return s

def area_of_triangle(a_triangle_number, h_number):
    s = a_triangle_number * h_number * 0.5
    return s

def area_of_circle(r_number):
    s = pi * pow(r_number, 2)
    return s

