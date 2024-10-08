# def print_text(a):
#     text = "111111111111text"
#     print("my_text >>" , a, "<< end my_text")
#     print(text)

# print_text("Anna")
# print_text(15)
# # print(text) #NameError: name 'text' is not defined. Did you mean: 'next'?
# print(print_text)
# print("print: ", print_text(55))

# print(print.__doc__)
# help(print)

# def greet(name):
#     """This function greets to the person
#     name - arg text"""
#     print("Hello, " + name + ". Good morning!")
# greet("Anna")
# print(greet.__doc__)
# # return 1 #SyntaxError: 'return' outside function

# def max_number(a, b):
#     if a > b:
#         return a
#         print("after return")
#     elif a < b:
#         return b
    

# print(max_number(1,2))
# c = max_number(3, 5)
# print(c)

# c = max_number(3, 3)
# print(c)


# def print_info(name, age):
#     print(f"my name is {name}, my age: {age}")

# # print_info() #TypeError: print_info() missing 2 required positional arguments: 'name' and 'age'
# # print_info("oleg", 18, 5) #TypeError: print_info() takes 2 positional arguments but 3 were given
# print_info("oleg", 28)
# print_info("Ira", 18)


# def print_info(name, age=18):
#     print(f"my name is {name}, my age: {age}")

# # print_info() #TypeError: print_info() missing 1 required positional argument: 'name'
# print_info("Anna")
# print_info("Andry", 88)


# print_info(15, "Liuda")
# print_info(age=15, name="Liuda")



# def print_info(name, age=15, city="Lviv"):
#     print(f"my name is {name}, my age: {age}, from {city}")

# print_info("Oleg")
# print_info("olga", age=25, city="IF")


# def print_info():
#     name = input("name:")
#     age = input("age:")
#     city = input("city:")
#     print(f"my name is {name}, my age: {age}, from {city}")

# print_info()
# print_info()


# def f(*args, **qwargs):
#     print(f"{args} {qwargs}")

# f(1,2,3,4,5,6,7, l=1,b="test", name=55)

# def g(a,b,c, *args, d=10, e=20, **kwargs):
#     print(f"{a =}\t{b =}\t{c =}\t{args =}\t{d =}\t{e =}\t{kwargs =}")


# g(1,2,3)
# g(1,2,3,4,5,6,7, e=99, t=55, m=88)


# def f(*args):
#     return sum(args) / len(args)

# print(f(10, 20, 30, 25))


# def avg(*args):
#     return sum(args) / len(args)


# def mean_num(*args):
#     print(sum(args)/ len(args))
    
# vedenya = input ("Введи числа через кому: ")
# def chuselca (*chusla):
#     return (f"Ти ввів - {chusla}")
# print (chuselca (vedenya))


# def g(a,b,c, *args, d=10, e=20, **kwargs):
#     print(f"{a =}\t{b =}\t{c =}\t{args =}\t{d =}\t{e =}\t{kwargs =}")

# l = (10,20,30,40,50)
# g(l[0],l[1],l[2],l[3],l[4])
# g(*l)
# d = {
#     "a":99,
#     "b": "test",
#     "c": 888,
#     "d": "SOftServe"
# }

# g(*d)
# g(**d)
# g(a=d["a"], b=d["b"], c=d["c"], d=d["d"])
# print(g)
# gg = g
# gg(**d)
# # print(gg)
# from random import randint
# l = [randint(0, 5) for _ in range(10)]
# s = sum(l)
# print(l, s)
# d = sum
# def sum(arr):
#     return arr.count(0)
# s = sum(l)
# print(l, s)
# sum = d
# s = sum(l)
# print(l, s)

# a = 1
# b = 2
# c = [1,2,3]
# print(a,b,c)
# print(dir())
# def f(c, d, e):
#     print("\t",dir())
#     a = 10
#     b= 20
#     c +=1
#     d +=1
#     e.append(20)
#     print(a,b,c,d, e)
#     print("\t",dir())
# f(a,b,c)
# print(dir())
# print(a,b,c)


# g = "global"

# def fun():
#     print(g)
# fun()

# def fun():
#     # print(g)
#     g = "local"
#     print(g)
# fun()
# print(g)

# g = "global"

# def fun():
#     global g
#     print(g)
#     g = "local"
#     print(g)
# fun()
# print(g)

# g = "global"
# l = "global"
# def out():
#     nonlocal l
#     l = "local" 
#     def inner():
#         ll = "local_inner"
#         nonlocal l
#         l=22
#         print("inner:", g, l, ll)
#     inner()
#     print("out:", g, l)
# out()
# print(g, l)

# def my_decor(fun):
#     def inner(*arg, **kwa):
#         print(">"*10)
#         print(f"ren: {fun.__name__} {arg=} {kwa=}")
#         result = fun(*arg, **kwa)
        
#         print("<"*10)
#         return result
#     return inner

# @my_decor
# def sum(a, b):
#     return a+b

# @my_decor
# def div(a,b):
#     return a/b
    
# print(f"sum: {sum(10, 20)}")
# print(f"sum: {sum(110, 210)}")
# print(f"sum: {sum(1110, 2110)}")

    
# print(f"div: {div(10, 20)}")
# print(f"div: {div(110, 210)}")
# print(f"div: {div(1110, 2110)}")

def fuc(n):
    f = 1
    for i in range(1,n+1):
        f *=i
    return f
print(fuc(5))
print(fuc(6))

# def r_fuc(n):
#     print(n)
#     return n*r_fuc(n-1)

# import sys
# sys.setrecursionlimit(5000)
# print(sys.getrecursionlimit())

# print(r_fuc(6))

# def r_fuc(n):
#     if n <= 0:
#         return 1
#     return n*r_fuc(n-1)

# print(r_fuc(6))


s= lambda a,b: a**b;   x=1
print(x)
print(s(5, 25) )

def s(a, b):
    return a**b


l = [1,2,"3,2",4,"5", "-99", "0", [1,2,34,45]]
l.sort(key=lambda e: str(e))
print(l)
def ss(e):
    return str(e).__len__()
l.sort(key=ss)
print(l)