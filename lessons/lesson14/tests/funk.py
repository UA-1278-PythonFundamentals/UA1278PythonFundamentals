from math import sqrt
from ff import *

def solver(a, b, c):
    D = b * b - 4 * a * c  # обчислення дискримінанта
    if D > 0:
        
        text = f1(b, D, a)
    elif D== 0:
        x = (-b)/(2 * a)
        text = "Дискримінант: %s \n x = %s\n" % (D, x)
    else:
        text = "Дискримінант: %s \n Рівняння розв'язків немає" % D
    return text
