int_list = [1, 2, 3, 4, 5]
float_list = [float(i) for i in int_list]
print("Original list:", int_list)
print("Converted to float:", float_list)

n = int(input("Enter the upper limit for Fibonacci numbers: "))
a, b = 0, 1
print("Fibonacci sequence up to", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

num = int(input("Enter a number to calculate its factorial: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")