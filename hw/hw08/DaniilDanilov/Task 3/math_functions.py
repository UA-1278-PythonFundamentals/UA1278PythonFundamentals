# Task3.
#  Write a program that calculates the area of ​​a rectangle S=a*b, the area of ​​a 
# triangle S=0.5*h*a, the area of ​​a circle S=pi*r**2. This module must be used in 
# another module in which we ask the user the area of ​​which figure he wants to 
# calculate.
#  (To perform the task, you need to import the math module, and from it the
#  pow() function and the value of the variable pi, and module, which contains
#  three functions for finding areas, into the main program. The basic logic of the
#  program is executed in the main module).

#  1.Rectangle      2.Triangle      3.Circle.

import math

def rectangle(a,b):
    a = float(input("Width: "))
    b = float(input("Height: "))

    s = a*b

    print("The area of a rectangle: ", s)
        
def triangle(h,a):
    h = float(input("Height: "))
    a = float(input("Base (a): "))

    s = 0.5*h*a

    print("The area of a triangle:", s)

def circle (pi, r):
    r = float(input("Radius: "))
    pi = math.pi

    s=pi*r**2

    print("The area of a circle:", s)