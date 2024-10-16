# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2.

from calculate.rectangle import *
from calculate.triangle import *
from calculate.circle import *

string = input("What do you want calculate: rectangle write 'r', if triangle write 't', or circle write 'c': ")

if string == 'r':
    print(area_of_rectangle(length=int(input(f'Write the length ')), \
                            width=int(input(f'Write the width '))))
elif string == 't':
    print(area_of_triangle(h=int(input(f'Enter the high of triangle: ')), \
                           a=int(input(f'Enter the a-side of triangle: '))))
elif string == 'c':
    print(area_of_circle(radius=int(input(f'Enter the radius of circle '))))
else:
    print('Error: letter entered incorrectly')
