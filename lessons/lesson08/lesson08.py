# def f(a:int,b:int)->float:
#     return a+b

# print(f(1,2))
# print(f("1","2"))



# print(__name__)

# from math import sin, cos
# print(sin(30))
# print(cos(30))
# import math
# print(math.sin(30))
# print(math.cos(30))

# from l2 import f
# print(f)
# # from lesson07.lesson07 import ss 

# import sys
# from pprint import pprint
# pprint(sys.path)

# sys.path.append("c:\\data\\github\\UA1278PythonFundamentals\\lessons")
# from lesson07.lesson07 import ss 
# pprint(sys.path)
# # open("f1.txt", "w")


# print(dir())
# import math
# print(dir())
# from math import *
# print(dir())
# import l1
# print(__name__)
# from p1 import l11

# from l1 import *
# print(dir())
# from l1 import __a, _a, a
# print(dir())
# import l1
# print(l1.a)
# print(l1._a)
# print(l1.__a)

# from p1.l11 import a as aa, _a, __a as _aa
# print(a)
# print(aa)
# print(aa, _a, _aa)

import sys
from pprint import pprint

import p1.l11
import p1.l12
pprint(sys.path)

# from p1.l11 import __a

import p1
print(p1.l11.a)
print(p1.l12.b)
print(p1.a)

