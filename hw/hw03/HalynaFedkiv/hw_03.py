#task_1
print('Task 1'.center(70, '='), end='\n\n')

philosophy = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(f'"Better" appears in the philosophy {philosophy.lower().count('better')} times.')
print(f'"Never" appears in the philosophy {philosophy.lower().count('never')} times.')
print(f'"Is" appears in the philosophy {philosophy.lower().count('is')} times.\n')
print(philosophy.upper(), end = '\n\n')
print(philosophy.replace('i', '&'), end='\n\n')


#task_2

import random

print('Task 2'.center(70, '='), end='\n\n')
number = input('Please enter a four-digit natural number:')
if len(number) != 4:
    number = str(random.randint(1000, 10000))
print('The original number is:', number)

product = 1
for digit in number:
    product *= int(digit)
print('The product of the digits of the number:', product)

print('The reversed number is:', number[::-1])
print('Numbers, included in the given number, in ascending order:', ''.join(sorted(number)), end='\n\n')


#task_3
print('Task 3'.center(70, '='), end='\n\n')
a, b = 2, 3
print(f'a = {a}, b = {b}')
b, a = a, b
print(f'a = {a}, b = {b}')