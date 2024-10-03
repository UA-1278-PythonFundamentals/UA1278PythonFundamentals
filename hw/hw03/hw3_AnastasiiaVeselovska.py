print("first task:")
zen_of_python = "\n The Zen of Python, by Tim Peters\n \n Beautiful is better than ugly.\n Explicit is better than implicit.\n Simple is better than complex.\n Complex is better than complicated.\n \
Flat is better than nested.\n Sparse is better than dense.\n \
Readability counts.\n Special cases aren't special enough to break the rules.\n \
Although practicality beats purity.\n Errors should never pass silently.\n \
Unless explicitly silenced.\n In the face of ambiguity, refuse the temptation to guess.\n \
There should be one-- and preferably only one --obvious way to do it.\n \
Although that way may not be obvious at first unless you're Dutch.\n \
Now is better than never.\n Although never is often better than *right* now.\n \
If the implementation is hard to explain, it's a bad idea.\n \
If the implementation is easy to explain, it may be a good idea.\n \
Namespaces are one honking great idea -- let's do more of those!"
find_better = str(zen_of_python.find("better"))
print('\t 1. Find "better": ' + find_better + "\n ---------------------------")
find_never = str(zen_of_python.find("never"))
print('\t 2. Find "never": ' + find_never + "\n ---------------------------")
find_is = str(zen_of_python.find("is"))
print('\t 3. Find "is": ' + find_is + "\n ---------------------------")
uppercase = zen_of_python.upper()
print("\t 4. Uppercase: " + uppercase + "\n ---------------------------")
replace = zen_of_python.replace("i", "&")
print(
    '\t 5. Replace "i" to "&": '
    + replace
    + "\n ------------------------------------------------------------"
)

print("\n second task:")
number = input("Enter a four-digit natural number: ")
digit_1 = int(number[0])
digit_2 = int(number[1])
digit_3 = int(number[2])
digit_4 = int(number[3])
product = digit_1 * digit_2 * digit_3 * digit_4
print("\t 1. Product of the digits: " + str(product) + "\n ---------------------------")
reverse_order = number[::-1]
print("\t 2. The number in reverse order: " + reverse_order + "\n ---------------------------")
sorted_number = sorted(number)
print("\t 3. Sorted numbers: " + "".join(sorted_number) + "\n ------------------------------------------------------------")

print("\n third task:")
variable_1 = input("Enter the first variable: ")
variable_2 = input("Enter the second variable: ")
variable_1, variable_2 = variable_2, variable_1
print("\t The swap of two variables:\n \t the first variable =", variable_1 + ", the second variable =", variable_2 + "\n ------------------------------------------------------------")
