
#Task 1
#Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.

list_of_integers = [i for i in range(13)]
list_of_floats = []
for j in list_of_integers:
    list_of_floats.append(float(j))
print(list_of_integers)
print(list_of_floats)
print()


# task 2
#Print Fibonacci numbers up to the entered number n, using cycles.

n = int(input('Enter n: '))
num1, num2 = 0, 1
while True:
    next_number = num1
    if next_number > n:
        break
    num1 = num2
    num2 = next_number + num1
    print(next_number, end=' ')
print()
print()


#task 3
# Write a script that will calculate the factorial of the entered
# number without using recursion.

n = int(input('Enter a number: '))
num = 1
factorial = 1
while num <= n:
    factorial *= num
    num += 1
print(f'Factorial of number {n} is {factorial}.')

#or
n = int(input('Enter a number: '))
factorial = 1
for num in range(1, n+1):
    factorial *= num
print(f'Factorial of number {n} is {factorial}.')
