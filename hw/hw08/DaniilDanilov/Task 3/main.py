# Task3.
#  Write a program that calculates the area of ​​a rectangle S=a*b, the area of ​​a 
# triangle S=0.5*h*a, the area of ​​a circle S=pi*r**2. This module must be used in 
# another module in which we ask the user the area of ​​which figure he wants to 
# calculate.
#  (To perform the task, you need to import the math module, and from it the
#  pow() function and the value of the variable pi, and module, which contains
#  three functions for finding areas, into the main program. The basic logic of the
#  program is executed in the main module).

import math
import math_functions

print("Hello! Here is the list of figures that are available:\n1. Rectangle \n2. Triangle \n3. Circle.")

choice = int(input("Write nubmer. \nYour choice is: "))

if choice == 1:
    print("Rectangle")
    math_functions.rectangle(0,0)

if choice == 2:
    print("Triangle")
    math_functions.triangle(0,0)

if choice == 3:
    print("Circle")
    math_functions.circle(0,0) 

else:
    print("The end.")