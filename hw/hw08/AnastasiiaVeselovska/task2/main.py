from areas import area_of_rectangle, area_of_triangle, area_of_circle
# from areas import *

def str_to_number_rectangle(a_rectangle, b):
    if str.isdigit(a_rectangle) == True:
        a_rectangle = int(a_rectangle)
    else:
        a_rectangle = float(a_rectangle)
        
    if str.isdigit(b) == True:
        b = int(b)
    else:
        b = float(b)
        
    return (a_rectangle, b)

def str_to_number_triangle(a_triangle, h):
    if str.isdigit(a_triangle) == True:
        a_triangle = int(a_triangle)
    else:
        a_triangle = float(a_triangle)
        
    if str.isdigit(h) == True:
        h = int(h)
    else:
        h = float(h)
        
    return (a_triangle, h)

def str_to_number_circle(r):
    if str.isdigit(r) == True:
        r = int(r)
    else:
        r = float(r)
    return r


while True:
    print("\n 1. Area of rectangle. \n 2. Area of triangle. \n 3. Area of circle. ")
    number = int(input("Enter the number to calculate the area. To finish, press any number except 1, 2 and 3: "))
    match number:
        case 1:
            a_rectangle = input("Enter the value of side a: ")
            b = input("Enter the value of side b: ")
            a_rectangle_number = str_to_number_rectangle(a_rectangle, b)[0]
            b_number = str_to_number_rectangle(a_rectangle, b)[1]
            print(f"The area of rectangle: {area_of_rectangle(a_rectangle_number, b_number)}")
        case 2:
            a_triangle = input("Enter the value of side a: ")
            h = input("Enter height value h: ")
            a_triangle_number = str_to_number_triangle(a_triangle, h)[0]
            h_number = str_to_number_triangle(a_triangle, h)[1]
            print(f"The area of triangle: {area_of_triangle(a_triangle_number, h_number)}")
        case 3:
            r = input("Enter the circle radius: ")
            r_number = str_to_number_circle(r)
            print(f"The area of circle: {area_of_circle(r_number)}")
        case _:
            break