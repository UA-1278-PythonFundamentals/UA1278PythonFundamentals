# first task
a = ([1, 2, 3, 4, 5, 6])
n = []

for i in a:
    n.append(i)

print(n)



# second task

fi = int(input("Press number"))

a,b=0,1

for i in range(fi):
    if a > fi:
        break
    print(a)
    t=a
    a=b
    b=t+b



# third task
fi = int(input("Press number"))
a = 1

for i in range(1, fi+1):
    a *= i

print(f"{fi}! = {a}")