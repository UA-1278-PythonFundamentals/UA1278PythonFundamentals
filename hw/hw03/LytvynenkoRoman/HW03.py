# 1. Write Python's philosophy in the string format:
# - find separately the naumber of occurences of the words "better", "never" and "is" in the given line

import importlib
import codecs

print('Original \'Zen of python\':')
this = importlib.import_module('this')

zen_of_python_original = codecs.encode(this.s, 'rot_13')
zen_of_python_lower = zen_of_python_original.lower()

number_of_better_in_zen = zen_of_python_lower.count('better')
number_of_never_in_zen = zen_of_python_lower.count('never')
number_of_is_in_zen = zen_of_python_lower.count('is')

print('Task 1.1: Find separatly the number of occurrences of the words: better, never, is.')
print(f'\n\'The Zen of python\' number of occurrences for:\n\
      better : {number_of_better_in_zen} times\n\
      never : {number_of_never_in_zen} times\n\
      is : {number_of_is_in_zen} times', end = '\n\n')

print('Task 1.2: Display all text in uppercase.')
print(zen_of_python_original.upper())

print('Task 1.3: Replace all occurrencesof te symbol \'i\' with \'&\'.')
print(zen_of_python_original.replace('i', '&'))

# 2. A four-digit natural number is specified:

from random import randrange

number = str(randrange(1000, 9999))
print(f"Recieved number: {number}")

# - find the product of the digits of this number
product_of_digits = 1

for digit in number:
      product_of_digits *= int(digit)

print(f"Digits product of \"{number}\" is \"{product_of_digits}\"")

# - write the number in reverse order
reversed_number = number[::-1]
print(f"Origin number: {number} --> Reversed number: {reversed_number}")

# in ascending order, you need to sort the numbers included in the given number
ordered_digits_from_number = sorted(number)
print(ordered_digits_from_number)

# 3. Interchange the values of two variables without using the third variable.

a = 1
b = 2
print(f"Before interchange: a={a}; b={b}")

(a, b) = (b, a)
print(f"After interchange: a={a}; b={b}")