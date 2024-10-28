# 07.1 Practical tasks / [GitHub Topic 7]
print()
print("07.1 Practical tasks / [GitHub Topic 7]")

# Task 1
print("Task 1")
def numbers(a,b):
    if a > b:
        return(a)
    else:
        return(b)
print(numbers(10,40))


# Task 2
# Write a program that calculates the area of a rectangle,
# triangle and circle (write three functions to calculates
# the number of characters included in given string

print()
print("Task 2")
def rectangle(a,b):
    area_rectangle = a*b
    return(area_rectangle)
print(rectangle(5,5))

def triangle(a,b):
    area_triangle = a*b/2
    return(area_triangle)
print(triangle(10,5))

def circle(r):
    area_circle = 3.14 * r**2
    return(area_circle)
print(circle(15))


# Task 3
print()
print("Task 3")
def word(w):
    c = {}
    for i in w:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    print(c)
word("hello")