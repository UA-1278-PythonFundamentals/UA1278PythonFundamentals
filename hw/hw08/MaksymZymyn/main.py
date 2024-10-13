# Task1.
# 1. Create structure of python like:
# ├── main.py
# ├── utils/
# │   ├── __init__.py
# │   └── formatter.py
# │   └── logger.py
# └── models/
#     ├── __init__.py
#     └── admin.py
#     └── user.py
# 2. Create functions create_admin, create_user, format_string, log_in_file in corresponding modules.
# These fuctions may have implementstion like pass.
# 3. Define __all__ in all modules so that contain only the functions from the previous step
# (you can create some additional functions to test it).
# 4. Fill __init.py__ files in packages so that import * of these packages contain only the functions from second step.
# 5. In main.py file write next code:
# from utils import *
# from models import *
# print(list(filter(lambda str: not ("__" in str), dir())))      I must have:  ['create_admin', 'create_user', 'format_string', 'log_in_file']
# You must obtain list like this:
# ['create_admin', 'create_user', 'format_string', 'log_in_file']

from utils import *
from models import *

print(list(filter(lambda str: not ("__" in str), dir())))
# ['create_admin', 'create_user', 'format_string', 'log_in_file']

# Task2.
# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re


def validate_password(password):
    """
    Validate the password according to the specified criteria.

    Parameters:
    password (str): The password to validate.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return False

    # Check for at least one special character
    if not re.search(r"[$#@]", password):
        return False

    return True


while True:
    user_password = input("Enter your password: ")

    if validate_password(user_password):
        print("Valid password.")
        break
    else:
        print("Invalid password. Please ensure it meets the criteria.")

# Task3.
# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
# another module in which we ask the user the area of which figure he wants to
# calculate.
# (To perform the task, you need to import the math module, and from it the
# pow() function and the value of the variable pi, and module, which contains
# three functions for finding areas, into the main program. The basic logic of the
# program is executed in the main module).

from areas import rectangle_area, triangle_area, circle_area


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
