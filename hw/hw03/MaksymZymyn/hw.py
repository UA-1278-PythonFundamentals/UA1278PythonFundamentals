# 1. You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
# - "better", "never" and "is" in the given line
# - you need to display all text in uppercase (all letters in uppercase)
# - replace all occurrences of the symbol “i” with “&”
import random
import this
import math
from functools import reduce

zen = this.s.translate(str.maketrans(this.d))
# Or
zen = "".join([this.d.get(c, c) for c in this.s])

# - "better", "never" and "is" in the given line
print("\nOccurrences of 'better':", zen.count("better"))
print("Occurrences of 'never':", zen.count("never"))
print("Occurrences of 'is':", zen.count("is"))

# - you need to display all text in uppercase (all letters in uppercase)
print("\nText in uppercase:\n", zen.upper())

# - replace all occurrences of the symbol “i” with “&”
print("\nText with 'i' replaced by '&':\n", zen.replace("i", "&"))

# 2. A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

num = random.randint(1000, 9999)
print("My number is ", num)

# - find the product of the digits of this number
str_num = str(num)

# Mine
product_digits = int(str_num[0]) * int(str_num[1]) * int(str_num[2]) * int(str_num[3])
print("\nThe product of the digits of my number is ", product_digits)

# Chatgpt
product_digits = 1
for digit in str_num:
    product_digits *= int(digit)
print("\nThe product of the digits of my number is ", product_digits)

# Chatgpt
product_digits = math.prod(int(digit) for digit in str_num)
print("\nThe product of the digits of my number is", product_digits)

# Chatgpt
product_digits = reduce(lambda x, y: x * y, map(int, str_num))
print("\nThe product of the digits of my number is", product_digits)

# - write the number in reverse order
# Mine
print("\nMy number in reverse order as a number is ", int(str(num)[::-1]))

# Chatgpt
print("\nMy number in reverse order as a string is", str(num)[::-1])

# Chatgpt
print("\nMy number in reverse order as a string is", ''.join(reversed(str_num)))

# Chatgpt
nums = list(str(num))
nums.reverse()
reversed_num = ''.join(nums)
print("\nMy number in reverse order as a string is", reversed_num)

# - in ascending order, you need to sort the numbers included in the given number
# Mine
a, b, c, d = str_num
l = [a, b, c, d]
l.sort()
numbers = ", ".join(l)
print("\nSorting the digits in ascending order: ", numbers)

# Mine
l = []
for digit in str_num:
    digit = int(digit)
    l.append(digit)
l.sort()
# Or
# l = sorted(l)
print("\nSorting the digits in ascending order: ", l)

# Chatgpt
print("\nSorting the digits in ascending order: ", ", ".join(sorted(str_num)))

# Chatgpt
sorted_digits = sorted(int(digit) for digit in str_num)
print("\nSorting the digits in ascending order: ", sorted_digits)

# Chatgpt
l = " ".join(str_num).split()
l.sort()
l = [int(digit) for digit in l]
print("\nSorting the digits in ascending order: ", l)

# Chatgpt
l = list("".join(str_num))
l.sort()
l = [int(digit) for digit in l]
print("\nSorting the digits in ascending order: ", l)

# Chatgpt
digits = [int(d) for d in str(num)]
digits.sort()
print("\nSorting the digits in ascending order: ", digits)

# Chatgpt
digits = list(map(int, str(num)))
digits.sort()
print("\nSorting the digits in ascending order: ", digits)

# 3. Interchange the values of two variables without using the third variable

a = 5
b = 3
print(f"In the beginning: a = {a}, b = {b}")
a, b = b, a
print(f"After interchanging the values of two variables: a = {a}, b = {b}")
