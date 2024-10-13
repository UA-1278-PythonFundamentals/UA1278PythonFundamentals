from Task_3 import *


choice = input('Press "1" to calculate the area of a rectangle.\n'
               'Press "2" to calculate the area of a triangle.\n'
               'Press "3" to calculate the area of a circle.\n'
               'Please make your choice: ')
if choice == '1':
    a = float(input('Enter a width: '))
    b = float(input('Enter a height: '))
    print(f'The area of a rectangle is {rectangle_area(a, b):.2f}')
elif choice == '2':
    a = float(input('Enter a base: '))
    b = float(input('Enter a height: '))
    print(f'The area of a triangle is {triangle_area(a, b):.2f}')
elif choice == '3':
    r = float(input('Enter a radius: '))
    print(f'The area of a circle is {circle_area(r):.2f}')
else:
    print(f'Please try again.')
