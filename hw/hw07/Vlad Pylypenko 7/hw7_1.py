# task 1
def largest_number(num_1, num_2):
    """return the largest number of two numbers"""
    return num_1 if num_1 > num_2 else num_2


# task 2
def rectangle_area(a, b):
    return round((a * b), 2)


def triangle_area(a, h):
    return round((1 / 2 * a * h), 2)


def circle_area(r):
    return round((3.14 * r ** 2), 2)


# task 3
def calculate_chars(word):
    chars_counter = {}
    for char in word:
        if char not in chars_counter:
            chars_counter[char] = word.count(char)
        else:
            continue
    return chars_counter


if __name__ == "__main__":
    while True:
        task = input("Enter a number of task(q - quit): ")

        if task == "1":
            num_1 = int(input("Enter first number: "))
            num_2 = int(input("Enter second number: "))

            print("largest number:", largest_number(num_1, num_2))
            print("=" * 40)

        elif task == "2":
            figure = input("Choose a figure: \n1 - rectangle\n2 - triangle\n3 - circle\n::: ")
            if figure == "1":
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))

                print("Rectangle area =", rectangle_area(a, b))
            elif figure == "2":
                a = int(input("Enter a: "))
                h = int(input("Enter h: "))

                print("Triangle area =", triangle_area(a, h))

            elif figure == "3":
                r = int(input("Enter r: "))

                print("Circle area =", circle_area(r))
            print("=" * 40)

        elif task == "3":
            word = input("Enter word: ")

            print("chars:", calculate_chars(word))
            print("=" * 40)

        elif task == "q":
            break
