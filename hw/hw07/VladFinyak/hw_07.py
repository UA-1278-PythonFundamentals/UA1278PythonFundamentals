# Task 1
def g(*args):
    sa= sum(args) / len(args)
    print (sa)

g(2,2,2,2,2,2,2,2,100000000)


def q(a,b):
    '''Function returns the largest number of two
numbers'''
    if a > b:
        print(a)
    elif b > a:
        print (b)
    else: print(f"{a} = {b}")        

q (50, 15)
q (1, 100)
q (10, 10)


# Task 2

def s_rectangle(a,b):
    s = a * b
    print (f"area of a rectangle: {s}")

def s_triangle(a,b,c):
    '''Formula Gerona'''
    P = a + b +c
    p = P / 2
    ss = p * (p - a)*(p - b)*(p - c)
    s = ss**0.5
    print (f"area of a triangle: {s}")

def s_circle(r):
    s = r ** 2 * 3.14
    print (f"area of a circle: {s}")

figure = (input('''
1 --> rectangle
2 --> triangle
3 --> circle
Enter the number of figure:                
'''))
if figure == "1":
    a = int(input("Enter height: "))
    b = int(input("Enter width: "))
    s_rectangle(a,b)
elif figure == "2":
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    s_triangle(a,b,c)
elif figure == "3":
    a = int(input("Enter radius: "))
    s_circle(a)
else: print ("Error")        

# Task 3

def a (text):
    return{i: text.count(i) for i in text}
print(a(input("")))