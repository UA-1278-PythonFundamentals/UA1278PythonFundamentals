import lesson05

print(__name__)
print(lesson05.l)


a = 2

def f():
    a = 1
    def g():
        nonlocal a
        a= 3
        print("g", a)
    g()    
    print("f", a)


print(a)
f()
print(a)

