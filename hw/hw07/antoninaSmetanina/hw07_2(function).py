# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

def area_of_rectangle(length, width):
    return length * width


# print(area_of_rectangle(, 2))

def area_of_triangle(a, b, c):
    s_triangle = 0
    '''a, b, c - sides of the triangle'''
    if a + b > c and a + c > b and b + c > a:
        s_triangle = (1 / 4) * ((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) ** 0.5
    else:
        print('Triangle does not exist')
    return round(s_triangle, 1)


# print(area_of_triangle(2, 3, 3))


def area_of_circle(radius):
    PI = 3.14
    area = PI * radius ** 2
    return round(area, 1)


# print(area_of_circle(2))


string = input("What do you want calculate: rectangle write 'r', if triangle write 't', or circle write 'c': ")

if string == 'r':
    print(area_of_rectangle(length=int(input(f'Write the length ')), \
                            width=int(input(f'Write the width '))))
elif string == 't':
    print(area_of_triangle(a=int(input(f'Enter the a-sides of triangle: ')), \
                           b=int(input(f'Enter the b-sides of triangle: ')), \
                           c=int(input(f'Enter the c-sides of triangle: '))))
elif string == 'c':
    print(area_of_circle(radius=int(input(f'Enter the radius of circle '))))
else:
    print('Error: letter entered incorrectly')

