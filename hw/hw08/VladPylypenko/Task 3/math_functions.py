import math

def rectangle(a,b):
    a = float(input("Width: "))
    b = float(input("Height: "))

    s = a*b

    print("The area of a rectangle: ", s)
        
def triangle(h,a):
    h = float(input("Height: "))
    a = float(input("Base (a): "))

    s = 0.5*h*a

    print("The area of a triangle:", s)

def circle (pi, r):
    r = float(input("Radius: "))
    pi = math.pi

    s=pi*r**2

    print("The area of a circle:", s)