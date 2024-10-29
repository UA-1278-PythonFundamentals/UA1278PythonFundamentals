
# class Point:
#     def __init__(self, x=0, y=0):
#         print("Point __init__")
#         self.x = x
#         self.y = y

#     def __str__(self):
#         print("Point __str__")
#         return f"x={self.x}, y={self.y}"

#     def __repr__(self):
#         print("Point __repr__")
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
#         print(type(self))
#         return (self.x**2 + self.y**2) ** 0.5
    

# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         print("Point3D __init__")
#         # self.x = x
#         # self.y = y
#         super().__init__(x, y)

#         self.z = z

#     def __str__(self):
#         print("Point3d __str__")
#         return f"x={self.x}, y={self.y} z={self.z}"
#     def old_print(self):
#         return super().print()
#     def print(self):
#         print(self)



# pd1 = Point3D(1,2,3)
# p1 = Point(9,8)
# pd1.dist_to_zero()
# p1.dist_to_zero()
# # print(type(pd1))
# # print(pd1.__dict__)
# # print(pd1)
# # print(p1)
# pd1.print()
# p1.print()
# pd1.old_print()


# print(f"{type(pd1) is Point=}")
# print(f"{type(p1) is Point=}")
# print(f"{isinstance(pd1, Point)=}")
# print(f"{isinstance(p1, Point)=}")
# print(f"{issubclass(Point3D, Point)=}")
# print(f"{issubclass(Point, Point)=}")

# class A:
#     def print(self):
#         print("A")
#     def foo(self):
#         print("A foo")

# class B:
#     def print(self):
#         print("B")
#     def boo(self):
#         print("B boo")

# class C(A, B):
#     pass


# c = C()
# c.boo()
# c.foo()
# c.print()


# class C(B, A):
#     pass
# c = C()
# c.boo()
# c.foo()
# c.print()

# class A:pass
# class B(A):pass
# class C(A):pass
# class D(B):pass
# class E(B):pass
# class F(C):pass
# class G(E, F):pass
# class K(D, G):pass


# k = K()
# print(K.mro())


# class A:
#     def print(self):
#         print(self)

#     @classmethod
#     def c_print(cls):
#         print(cls)

#     @staticmethod
#     def s_print():
#         print("static")

# a = A()
# print(f"{A=}")
# print(f"{a=}")

# a.print()
# # A.print()#TypeError: A.print() missing 1 required positional argument: 'self'
# A.print(a)


# a.c_print()
# A.c_print()


# A.s_print()
# a.s_print()



# class BaseModel:
#     @classmethod
#     def get_by_id(cls, id):
#         print(f"Select * from {cls.__name__};")


# class User(BaseModel):
#     # def get_by_id(self, id):
#     #     print("Select * from User;")
#     pass

# class Order(BaseModel):
#     # def get_by_id(self, id):
#     #     print("Select * from Order;")
#     pass


# u = User()
# o = Order()
# u.get_by_id(1)
# o.get_by_id(1)


# class A:
#     def __init__(self, x, y, z):
#         self.x = x
#         self._y = y
#         self.__z = z
#     def __str__(self) -> str:
#         return f"{self.x} {self._y} {self.__z}"

# a = A(1,2,3)
# print(a)
# print(a.x)
# print(a._y)
# # print(a.__z)
# print(a._A__z)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f"x={self.__x}, y={self.__y}"
#     def get_x(self):
#         print("get_x")
#         return self.__x
#     def set_x(self, x):
#         print("set_x")
#         if type(x) in (int, float):
#             self.__x = int(x)
#         else:
#             print("error set x")

#     x = property(get_x, set_x)

#     @property
#     def y(self):
#         print("get_y")
#         return self.__y
    
#     @y.setter
#     def y(self, y):
#         print("set_y")
#         self.__y = y

# p = Point(25,17)
# # print(p)
# # p.set_x(99)
# # print(p.get_x())
# # p.set_x(9.55)
# # print(p)
# # p.set_x("kjdfvbdf")
# # print(p)
# # print(p.x)
# # p.x = 99
# # print(p)
# print(p.y)
# p.y = 99
# print(p)


class A:
    def f(self):
        print("A")
    def f(self, text):
        print("A", text)

class B(A):
    def f(self):
        print("B")

a = A()
a.f("fndbkf")
from pprint import pprint
pprint(A.__dict__)