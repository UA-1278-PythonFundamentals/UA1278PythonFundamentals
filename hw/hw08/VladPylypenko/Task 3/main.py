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