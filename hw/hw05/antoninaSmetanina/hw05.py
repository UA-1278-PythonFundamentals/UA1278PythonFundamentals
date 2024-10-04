# Task1. Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

l_int = [2, 4, 5, 6]
l_float = []

for i in l_int:
    l_float.append(float(i))

print(l_float)

# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

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


# Task3. Write a script that will calculate the factorial of the entered
# number without using recursion.
# Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, 4! = 1*2*3*4 =24

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f'{n}! = {factorial}')

