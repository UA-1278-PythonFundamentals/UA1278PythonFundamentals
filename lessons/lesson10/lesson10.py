# a = list()

# class A():
#     def foo(self):
#         print("A:foo")
#     def boo(self):
#         print("A:boo")


# class B(A):
#     def boo(self):
#         print("B:boo")


# a = A()
# a.foo()
# a.boo(1)
# b = B()
# b.foo()
# b.boo()

# class Human:
#     """doc for class Human"""
#     name = "A"
#     def print(self):
#         print("Human", self.name)


# # print(Human.__doc__)
# # help(Human)

# h1 = Human()
# h2 = Human()
# print(type(h1), h1)
# print(type(h2), h2)
# h1.print()
# h2.print()
# print(h1.name)

# class A:
#     cm = [1, 2]
#     ci = 1
#     def __init__(self):
#         self.im = [11,22]
#         self.ii = 99

# def print_A(obj):
#     print(f"cm:{obj.cm} ci:{obj.ci} im:{obj.im} ii:{obj.ii} {obj.__dict__}")

# a1 = A()
# a2 = A()
# # print(dir(A))
# print(A.__dict__)
# # print(dir(a1))
# print(a1.__dict__)
# print_A(a1)
# print_A(a2)
# a1.im.append(22)
# a2.ii = 55
# a1.cm.append(99)
# print_A(a1)
# # print_A(a2)


# class A:
#     cm = [1, 2]
#     ci = 1
#     def __init__(self):
#         self.im = [11,22]
#         self.ii = 99

#     def method_print(self):
#         print(f"method_print cm:{self.cm} ci:{self.ci} im:{self.im} ii:{self.ii} {self.__dict__}")


# def print_A(obj):
#     print(f"cm:{obj.cm} ci:{obj.ci} im:{obj.im} ii:{obj.ii} {obj.__dict__}")


# a1 = A()
# a2 = A()
# # print(dir(A))
# print(A.__dict__)
# # print(dir(a1))
# print(a1.__dict__)


# a1.method_print()
# A.method_print(a1)

# A.m = print_A
# a1.m()
# a2.m()


# class A:

#     def __new__(self, * args, ** kwargs): # class Singleton.
#         return  object.__new__ (self, *args, **kwargs)
#     pass
#     def foo():
#         raise NotImplemented() 
    
# a = A()
# print(type(a), a)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         # print("__str__")
#         return f"x={self.x}, y={self.y}"

#     def __repr__(self):
#         # print("__repr__")
#         return f"({self.x}, {self.y})"

#     def to_string(self):
#         return f"x={self.x}, y={self.y}"

#     def print(self):
#         print(self.to_string())

#     def __add__(self, other):

#         p = Point()
#         p.x = self.x + other.x
#         p.y = self.y + other.y
#         return p

#     def __lt__(self, other):

#         return self.dist_to_zero() < other.dist_to_zero()

#     def add(self, other):

#         p = Point()
#         p.x = self.x + other.x
#         p.y = self.y + other.y
#         return p

#     def dist_to_zero(self):

#         return (self.x**2 + self.y**2) ** 0.5


# p1 = Point(12, 17)
# p2 = Point(1, 25)
# print(p1)
# print(p2)
# # print([p1, p2])
# # print(p1.to_string())
# # p1.print()

# # print(str(p1))
# p3 = p1 + p2
# p4 = p1.add(p2)
# print(p3, p4)
# from random import randint

# points = [Point(randint(-10, 10), randint(-10, 10)) for _ in range(10)]
# print(points)
# print(points[0] < points[1])
# points.sort()
# print(points)



l = [a1,a2, a3]
l<type>