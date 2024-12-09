# Task 01
# Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.

float_list = []

for int_num in range(10):
   float_list.append(float(int_num))

print(float_list)


# Task 02
# Print Fibonacci numbers up to the entered number n, using cycles.

entered_limit = int(input('Please print number for limit to Fibonacci numbers: '))

fibonacci_number = 1
fibonacci_list = [0]
index = 1

while fibonacci_number < entered_limit:
    fibonacci_list.append(fibonacci_number)
    fibonacci_number = fibonacci_list[index - 1] + fibonacci_list[index]
    index += 1

print(fibonacci_list)

# Task 03
# Write a script that will calculate the factorial of the entered number without using recursion.

entered_number = int(input('Please enter number to calculate factorial of entered number:'))

factorial_of_entered_number = 1

for x in range(1, entered_number + 1):
    factorial_of_entered_number *= x

print(f'Factorial of entered number ({entered_number}) is {factorial_of_entered_number}.')