def task_1():
    nums = list(range(1, 11))

    divisible_by_2 = [x for x in nums if x % 2 == 0]
    divisible_by_3 = [x for x in nums if x % 3 == 0]
    not_divisible_by_2_3 = [x for x in nums if x not in divisible_by_2 and x not in divisible_by_3]

    print("divisible by 2:", divisible_by_2, "\n", "divisible by 3:", divisible_by_3, "\n",
          "not divisible by 2 and 3:", not_divisible_by_2_3, sep="")


def task_2():
    while True:
        login = input("Enter a login: ")

        if login == "First":
            print("Hello, First!")
            break
        else:
            print(f"'{login}' login is not valid")


if __name__ == "__main__":
    while True:
        task = input("enter a number of task(q - quit): ")

        if task == "1":
            task_1()
            print("=" * 40)
        elif task == "2":
            task_2()
            print("=" * 40)
        elif task == "q":
            break
