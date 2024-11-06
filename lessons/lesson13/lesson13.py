# doubled_odds = [n * 2 for n in range(10)]
# print(doubled_odds)
# doubled_odds = [n for n in range(10) if n % 2 == 1]
# print(doubled_odds)
# doubled_odds = [n * 2 for n in range(10) if n % 2 == 1]
# print(doubled_odds)

# doubled_odds = []
# for n in range(10):
#     if n % 2 == 1:
#         doubled_odds.append(n * 2)
                            
# print(doubled_odds)


# vec1 = [3, 10, 2, 1]
# vec2 = [-20, 5, 1]
# print(list(zip(vec1, vec2)))
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# print(dot_mul)
        

# l = [1, "123", 2,"3",4,"6",7,8]
# print(l)
# ll = map(int, l)
# print(list(ll))

# def my_map(fun, l):
#     result = []
#     for i in l:
#         result.append(fun(i))
#     return result


# def my_print(obj):
#     print(">"*10)
#     print(obj)
#     print("<"*10)

# my_print(20)
# my_print([1,2,3])
# l = [1, "123", 2,"3",4,"6",7,8]
# list(map(my_print, l))

# from functools import reduce
# def a_add_b(a, b):
#     print(f"{a=} {b=} {a+b=}")
#     return a+b
# print(reduce(a_add_b, [47,11,42,13]))

# r = range(5)
# print(r)
# itr = iter(r)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))



# class my_range:
#     def __init__(self, start, end=None, step=1) -> None:
#         self.current = None
#         if end is None:
#             self.start = 0
#             self.end = start
#         else:
#             self.start = start
#             self.end = end
#         self.step = step

#     def __repr__(self) -> str:
#         return f"RANGE({self.start}, {self.end}, {self.step})"
    
#     def __iter__(self):
#         r = my_range(self.start, self.end, self.step)
#         if self.current is None:
#             r.current = self.start
#         return r
#     def __next__(self):
#         if self.current < self.end:
#             result = self.current
#             self.current += self.step
#             return result  
#         raise StopIteration("my renge is empty")
# r1 = my_range(4)
# r2 = my_range(-4, 4)
# r3 = my_range(-4, 4, 3)
# print(r1)
# print(r2)
# print(r3)
# c = 1
# for i in r1:
#     c += 1
#     print(i)
#     if c >10:
#         break
# for i in r2:
#     print(i)
# for i in r3:
#     print(i)


# print(r1)

# i1_r1 = iter(r1)
# i2_r1 = iter(r1)
# print(i1_r1)
# print(i2_r1)
# print(next(i1_r1))
# print(next(i1_r1))
# print(next(i2_r1))


# def my_it(l):
#     return l
# print(my_it)

# def my_it(l):
#     yield l

# print(my_it([1,2,3,4]))

# def range2(end):
#     curent = 0
#     while curent < end:
#         return curent
#         curent += 1

# r = range2(10)
# print(r)

# def range2(end):
#     curent = 0
#     while curent < end:
#         yield curent
#         curent += 1

# r = range2(3)
# print(r)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

# def range_i(end):
#     return [i for i in range(end)]
# ri = range_i(10)
# print(ri.__sizeof__(), ri)
# def range_g(end):
#     curent = 0
#     while curent < end:
#         yield curent
#         curent += 1
# rg = range_g(10)
# print(rg.__sizeof__(), rg, list(rg))

# ri = range_i(1000)
# print(ri.__sizeof__(), ri)
# rg = range_g(1000)
# print(rg.__sizeof__(), rg, list(rg))

# print([i**2 for i in range(5)])
# print({i for i in range(5)})
# print({i:i**2 for i in range(5)})
# print((i**2 for i in range(5)))



# def dec(obj):
#     print(type(obj))
#     return obj


# dec(1)
# dec("1")


# @dec
# def sum(a, b):
#     print(a+b)

# sum(10, 20)


# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner


# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         result = func(*args, **kwargs)
#         print("%" * 30)
#         return result
#     return inner



# @star
# @percent
# @star
# def sum(a, b):
#     print(f"{a+b=}")

# @percent
# def div(a, b):
#     print(f"{a/b=}")



# sum(10, 25)
# sum(99, 33)


# def layer(symbol, count):
#     def dec(func):
#         def inner(*args, **kwargs):
#             print(symbol * count)
#             result = func(*args, **kwargs)
#             print(symbol * count)
#             return result
#         return inner
#     return dec


# @layer("=", 20)
# @layer("#", 10)
# def sum(a, b):
#     print(f"{a+b=}")

# sum(10., 20)
# ===
# ###
# 20
# ##
# ==



# class A():
#     @layer("Class", 5)
#     def __init__(self) -> None:
#         pass
 

# a = A()

def dec(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        return result
    return inner


class User:
    def __init__(self, user_id, name, age, email, role):
        self.__user_id = user_id
        self.__name = name
        self.__age = age
        self.__email = email
        self.__role = role
    
    def __repr__(self):
        return f"User({self.__user_id}, {self.__name}, {self.__age}, {self.__email}, {self.__role})"
    @dec
    def get_age(self):
        return self.__age
    @dec
    def set_age(self, age):
        if age > 0:
            self.__age = age
    age = property(get_age, set_age)
    

    @property
    @dec
    def name(self):
        return self.__name
    
    @name.setter
    @dec
    def name(self, name):
        self.__name = name
user = User(12, "Liubomyr", 38, "galamagal86@gmail.com", "mentor")
print(user)
print(user.get_age())
user.set_age(-25)
print(user)
user.set_age(25)
print(user)

print(user.age)
user.age = 44
print(user)
print(user.age)

print(user.name)
user.name = "Igor"
print(user.name)
print(user)