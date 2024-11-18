# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).
import random


def largest_number(a=random.randint(1, 100), b=random.randint(1, 100)):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int): The first number (default is a random number between 1 and 100)
    b (int): The second number (default is a random number between 1 and 100)

    Returns:
    int: The largest number between a and b. If both numbers are equal, returns either of them.
    """
    print(f"The largest number between a={a} and b={b} is {max(a, b)}")
    return max(a, b)


print(f"The function {largest_number.__name__} returned {largest_number()}")
print(f"The function {largest_number.__name__} returned {largest_number(10, 10)}")
print(f"The function {largest_number.__name__} returned {largest_number(10, 20)}")
print(f"The function {largest_number.__name__} returned {largest_number(30, 20)}")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"The function {largest_number.__name__} returned {largest_number(x, y)}")

# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice)


import math


def rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width


def triangle_area(base, height):
    """
    Calculates the area of a triangle.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height


def circle_area(radius):
    """
    Calculates the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return round(math.pi * radius * radius, 2)


def main():
    print("Welcome to the program that calculates the area of the figure!")
    print("Choose a figure: ")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    while True:
        choice = input("Enter the number of the operation (1/2/3) or 'exit' to exit the program: ")
        if choice == "exit":
            break
        elif choice == "1":
            a = float(input("Enter the length of the rectangle: "))
            b = float(input("Enter the width of the rectangle: "))
            area = rectangle_area(a, b)
            print(f"The area of the rectangle is {area}")
        elif choice == "2":
            b = float(input("Enter the base of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            area = triangle_area(b, h)
            print(f"The area of the triangle is {area}")
        elif choice == "3":
            r = float(input("Enter the radius of the circle: "))
            area = circle_area(r)
            print(f"The area of the circle is {area}")
        else:
            print("Invalid choice, please select a valid operation.")


if __name__ == "__main__":
    main()


# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

# 1
def number_characters(a: str):
    """
    Calculates the frequency of characters in a given string.

    Parameters:
    a (str): The input string.

    Returns:
    dict: A dictionary where the keys are characters and the values are their frequencies.
    """
    dict_characters = {}
    for char in a:
        if char in dict_characters:
            dict_characters[char] += 1
        else:
            dict_characters[char] = 1
    return dict_characters


user_string = input("Enter your string: ")
print(number_characters(user_string))


# 2
def number_characters(a: str):
    """
    Calculates the frequency of characters in a given string using the count method.

    Parameters:
    a (str): The input string.

    Returns:
    dict: A dictionary where the keys are unique characters and the values are their frequencies.
    """
    dict_characters = {}
    for char in set(a):
        dict_characters[char] = a.count(char)
    return dict_characters


user_string = input("Enter your string: ")
print(number_characters(user_string))
