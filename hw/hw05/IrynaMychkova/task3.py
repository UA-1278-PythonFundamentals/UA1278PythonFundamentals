# Task. Write a script that will calculate the factorial of the entered number
# without using recursion.
n = int(input('Enter the number: '))
factorial = 1
if n < 0:
    print("Incorrect input")

for i in range(1, n + 1):
    factorial *= i
    
print(f'{n}! = {factorial}')
