from shapes import *

def main():
    choice = input("прямокутник,трикутник,коло: ")

    if choice == 'прямокутник':
        a = float(input("a: "))
        b = float(input("b: "))
        area = rectangle_area(a, b)
        print(area)

    elif choice == 'трикутник':
        h = float(input("h: "))
        a = float(input("a: "))
        area = triangle_area(h, a)
        print(area)

    elif choice == 'коло':
        r = float(input("r: "))
        area = circle_area(r)
        print(area)

if __name__ == "__main__":
    main()
