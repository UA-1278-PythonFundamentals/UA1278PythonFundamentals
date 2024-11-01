
def str_to_number_rectangle(a_rectangle, b_rectangle):
    if str.isdigit(a_rectangle) == True:
        a_rectangle = int(a_rectangle)
    else:
        a_rectangle = float(a_rectangle)
        
    if str.isdigit(b_rectangle) == True:
        b_rectangle = int(b_rectangle)
    else:
        b_rectangle = float(b_rectangle)
        
    return (a_rectangle, b_rectangle)

def str_to_number_triangle(a_triangle, b_triangle, c_triangle):
    if str.isdigit(a_triangle) == True:
        a_triangle = int(a_triangle)
    else:
        a_triangle = float(a_triangle)
        
    if str.isdigit(b_triangle) == True:
        b_triangle = int(b_triangle)
    else:
        b_triangle = float(b_triangle)
        
    if str.isdigit(c_triangle) == True:
        c_triangle = int(c_triangle)
    else:
        c_triangle = float(c_triangle)
        
    return (a_triangle, b_triangle, c_triangle)

def str_to_number_circle(r):
    if str.isdigit(r) == True:
        r = int(r)
    else:
        r = float(r)
    return r

def area_of_rectangle(a_rectangle_number, b_rectangle_number):
    s = a_rectangle_number * b_rectangle_number
    return s

def area_of_triangle(a_triangle_number, b_triangle_number, c_triangle_number):
    p = (a_triangle_number + b_triangle_number + c_triangle_number)/2
    s = (p * (p - a_triangle_number) * (p - b_triangle_number) * (p - c_triangle_number)) ** 0.5
    return s

def area_of_circle(r_number):
    pi = 3.14
    s = pi * (r_number ** 2)
    return s


while True:
    print("\n 1. Area of rectangle. \n 2. Area of triangle. \n 3. Area of circle. ")
    number = int(input("Enter the number to calculate the area. To finish, press any number except 1, 2 and 3: "))
    match number:
        case 1:
            a_rectangle = input("Enter the value of side a: ")
            b_rectangle = input("Enter the value of side b: ")
            a_rectangle_number = str_to_number_rectangle(a_rectangle, b_rectangle)[0]
            b_rectangle_number = str_to_number_rectangle(a_rectangle, b_rectangle)[1]
            print(f"The area of rectangle: {area_of_rectangle(a_rectangle_number, b_rectangle_number)}")
        case 2:
            a_triangle = input("Enter the value of side a: ")
            b_triangle = input("Enter the value of side b: ")
            c_triangle = input("Enter the value of side c: ")
            a_triangle_number = str_to_number_triangle(a_triangle, b_triangle, c_triangle)[0]
            b_triangle_number = str_to_number_triangle(a_triangle, b_triangle, c_triangle)[1]
            c_triangle_number = str_to_number_triangle(a_triangle, b_triangle, c_triangle)[2]
            print(f"The area of triangle: {area_of_triangle(a_triangle_number, b_triangle_number, c_triangle_number)}")
        case 3:
            r = input("Enter the circle radius: ")
            r_number = str_to_number_circle(r)
            print(f"The area of circle: {area_of_circle(r_number)}")
        case _:
            break
            


