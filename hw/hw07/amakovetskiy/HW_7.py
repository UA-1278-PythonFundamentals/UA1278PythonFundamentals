
print ("\n\n\n\n\n##############################(Task1)#################################\n\n\n\n")

# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).




def larg(number1, number2):
    '''function that returns the largest number of two numbers'''
    return number1 if number1 > number2 else number2


print(larg(100, 50))



print ("\n\n\n\n\n##############################(Task2)#################################\n\n\n\n")


# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

def area_of_rectangle(length, width):
    return length * width


# print(area_of_rectangle(6, 8))

def area_of_triangle(a, b, c):
    '''a, b, c - sides of the triangle'''
    s_triangle = 0
    
    if a + b > c and a + c > b and b + c > a:
        s_triangle = (1 / 4) * ((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) ** 0.5
    else:
        print('Triangle does not exist')
    return round(s_triangle, 1)


# print(area_of_triangle(6, 9, 9))


def area_of_circle(radius):
    PI = 3.14
    area = PI * radius ** 2
    return round(area, 1)


# print(area_of_circle(5))


string = input("What do you want calculate: rectangle ==> 'r', if triangle ==> 't', or circle ==> 'c': ")

if string == 'r':
    print(area_of_rectangle(length=int(input(f'Write the length: ==>  ')), \
                             width=int(input(f'Write the width:  ==>  '))))
elif string == 't':
    print(area_of_triangle(a=int(input(f'Enter the a-sides of triangle: ==>  ')), \
                           b=int(input(f'Enter the b-sides of triangle: ==>  ')), \
                           c=int(input(f'Enter the c-sides of triangle: ==>  '))))
elif string == 'c':
    print(area_of_circle(radius=int(input(f'Enter the radius of circle: ==>  '))))
else:
    print('Error: letter entered incorrectly')



    print ("\n\n\n\n\n##############################(Task3)#################################\n\n\n\n")


    Task3. Write a function that calculates the number of characters
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}

def count_letters(word='hello'):
    letter_count = {}
    for i in list(word):
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    return letter_count


print(count_letters())

