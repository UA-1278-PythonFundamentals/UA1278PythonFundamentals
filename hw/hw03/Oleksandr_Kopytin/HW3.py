TEXT = "Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you're Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it's a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let's do more of those! \
Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently."


def task_1():
    print("Task 1.")
    number_of_line = int(input("Enter a number of line: "))
    number_of_line -= 1

    lines_of_text = TEXT.split(".")
    lines_of_text.pop()

    line = lines_of_text[number_of_line]
    print("Your line:", line)
    print("words 'better' found:", line.count("better"))
    print("words 'never' found:", line.count("never"))
    print("words 'is' found:", line.count("is"), "\n")

    print("All text in uppercase:", TEXT.upper(), "\n")

    print("test with & instead of i:", TEXT.replace("i", "&"))


def task_2():
    number = input("Enter a number: ")

    int_number = int(number)
    product = 1
    while int_number > 0:
        product *= int_number % 10
        int_number //= 10

    print("product of numbers:", product)

    print("number in reverse order:", number[::-1])

    print("sorted numbers included in the given number:", "".join(sorted(number)))


def task_3():
    a = input("Enter a:")
    b = input("Enter b:")

    a, b = b, a
    print("a:", a)
    print("b:", b)


if __name__ == "__main__":
    while True:
        task = input("enter a number of task(q - quit): ")

        if task == "1":
            task_1()
        elif task == "2":
            task_2()
        elif task == "3":
            task_3()
        elif task == "q":
            break
