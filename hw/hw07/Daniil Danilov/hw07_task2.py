# Task2. Write a program that calculates the area of ​​a rectangle, triangle and circle.
# (write three functions to calculate the area, and call them in the main program depending on the user's choice).


def area_of_rectangle():
    return float(input("Length: ")) * float(input("Width: "))

def area_of_triangle():
    return 0.5 * float(input("Base: ")) * float(input("Height: "))

def area_of_circle():
    pi = 3.141592
    return pi * float(input("Radius: ")) ** 2

choice = input("Choose a shape (rectangle/triangle/circle): ").lower()

if choice == "rectangle":
    print("Area:", area_of_rectangle())
elif choice == "triangle":
    print("Area:", area_of_triangle())
elif choice == "circle":
    print("Area:", area_of_circle())
else:
    print("Invalid choice.")
