import area_functions


def main():
    print("Select a figure:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    figure = int(input("Enter a number: "))

    if figure == 1:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print(area_functions.rectangle_area(a, b))
    elif figure == 2:
        h = float(input("Enter h: "))
        a = float(input("Enter a: "))
        print(area_functions.triangle_area(h, a))
    elif figure == 3:
        r = float(input("Enter r: "))
        print(area_functions.circle_area(r))


if __name__ == "__main__":
    main()
