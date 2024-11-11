from math import sqrt

def f1(b, D, a):
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return "Дискримінант: %s \n x1 = %s \n x2 = %s \n" % (D, x1, x2)

def f2(b, D, a):
    x = (-b)/(2 * a)
    return  "Дискримінант: %s \n x = %s\n" % (D, x)

def D(a, b, c):
    return  b * b - 4 * a * c