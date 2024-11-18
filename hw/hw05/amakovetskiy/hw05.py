# Task1

l_int = [2, 4, 5, 6]
l_float = []

for i in l_int:
    l_float.append(float(i))

print(l_float)


#Task2
n = int(input())
a = 0
b = 1
for i in range(n):
    if a > n:
        break
    print(a, end=' ')
    temporary = a
    a = b
    b = temporary + b

#Task3

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f'{n}! = {factorial}')



