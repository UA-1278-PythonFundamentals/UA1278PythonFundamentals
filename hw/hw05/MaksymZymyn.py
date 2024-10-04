# Task1. Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    l[i] = float(l[i])
print(l)

# Or
i = 0
while i < len(l):
    l[i] = float(l[i])
    i += 1
print(l)

# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

n = int(input("Enter a number: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

# Or
a, b = 0, 1
fibonacci = ""
while a <= n:
    fibonacci = fibonacci + f"{a} "
    a, b = b, a + b
print(fibonacci)

# Or
a, b = 0, 1
fibonacci = []
while a <= n:
    fibonacci.append(a)
    a, b = b, a + b
for fib in fibonacci:
    print(fib, end=" ")
print()

# Or
if n == 0:
    print("0")
else:
    a, b = 0, 1
    fibonacci = f"{a} {b} "
    fib = 0

    while fib < n:
        fib = a + b
        if fib > n:
            break
        fibonacci = fibonacci + f"{fib} "
        a, b = b, fib

    print(fibonacci)

# Or
if n == 0:
    print("0")
else:
    a, b = 0, 1
    fibonacci = [a, b]
    fib = 0

    while fib < n:
        fib = a + b
        if fib > n:
            break
        fibonacci.append(fib)
        a, b = b, fib
    for fib in fibonacci:
        print(fib, end=" ")
print()

# Task3. Write a script that will calculate the factorial of the entered
# number without using recursion.
# Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ….

n = int(input("Enter a number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")

# Or
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f"The factorial is {factorial}.")
