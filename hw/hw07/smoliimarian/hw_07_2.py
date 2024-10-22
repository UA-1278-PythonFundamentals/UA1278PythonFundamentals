def area_of_triangle(base, height):
    return 0.5 * base * height


def area_of_rectangle(length, width):
    return length * width


def area_of_circle(radius):
    return 3.14 * radius**2


def main():
    print("Enter 1 for triangle, 2 for rectangle, 3 for circle")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print("The area of the triangle is", area_of_triangle(base, height))
    elif choice == 2:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("The area of the rectangle is", area_of_rectangle(length, width))
    elif choice == 3:
        radius = float(input("Enter the radius: "))
        print("The area of the circle is", area_of_circle(radius))
    else:
        print("Invalid choice")


main()
