from utils import *
from models import *

# Task 1
print("Task 1:", end=" ")
print(list(filter(lambda str: not ("__" in str), dir())))

import re


# Task 2
def validate_password():
    password = input("Enter a password: ")
    if not re.match(r"^[a-zA-Z\d$#@]{6,16}$", password):
        print("Password is not valid 6 < length or > 16")
        return

    elif not re.search(r"[a-z]", password):
        print("Password is not valid. no a - z")
        return

    elif not re.search(r"[A-Z]", password):
        print("Password is not valid. no A - Z")
        return

    elif not re.search(r"\d", password):
        print("Password is not valid no 0 - 9")
        return

    elif not re.search(r"[$#@]", password):
        print("Password is not valid no $#@")
        return
    else:
        print(f"password: {password} is valid")


from areas_module import rectangle_area, triangle_area, circle_area


# Task 3
def calculate_area():
    figure = input("Enter a figure:\n1 - rectangle\n2 - triangle\n3 - circle\n:::")

    if figure == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print(rectangle_area(a, b))
    elif figure == "2":
        h = float(input("Enter h: "))
        a = float(input("Enter a: "))
        print(triangle_area(h, a))
    elif figure == "3":
        r = float(input("Enter r: "))
        print(circle_area(r))
    else:
        print("Invalid input")


if __name__ == "__main__":
    while True:
        task = input("Enter a number of task(2 or 3, q - quit): ")

        if task == "q":
            break

        elif task == "2":
            validate_password()

        elif task == "3":
            calculate_area()
