def task_1():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7]

    for index in range(len(list_of_numbers)):
        list_of_numbers[index] = float(list_of_numbers[index])

    print("converted list:", list_of_numbers)


def task_2():
    num1, num2 = 0, 1
    index_of_last_number = int(input("index of last number: "))

    while index_of_last_number > 0:
        print(num1, end=" ")
        num1, num2 = num2, num2 + num1
        index_of_last_number -= 1

    print()  # for beautiful console output


def task_3():
    num = int(input("enter a number: "))
    factorial = 1

    for multiplier in range(1, num + 1):
        factorial *= multiplier

    print(f"factorial of {num} =", factorial)


if __name__ == "__main__":
    while True:
        task = input("enter a number of task(q - quit): ")

        if task == "1":
            task_1()
            print("=" * 40)
        elif task == "2":
            task_2()
            print("=" * 40)
        elif task == "3":
            task_3()
            print("=" * 40)
        elif task == "q":
            break
