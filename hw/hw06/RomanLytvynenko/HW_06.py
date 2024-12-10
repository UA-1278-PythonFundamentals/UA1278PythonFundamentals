# Task 1
# In range from 1 to 10 determine
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

ten_range = range(1, 11)

even_numbers = []
odd_numbers = []
not_divisiable = []

even_numbers = [number for number in ten_range if number % 2 == 0]
odd_numbers = [number for number in ten_range if number % 3 == 0]
not_divisiable = [number for number in ten_range if number % 2 == 1 and number % 3 == 1]

print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')
print(f'Not divisiable numbers: {not_divisiable}')


# Task 2
# Write the script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.

login = input('Print user\'s login: \n')

while(login != "First"):
    print(f'Error. Login {login} is incorrect. Please write correct login.')
    login = input('Print user\'s login: \n')
else:
    print(f'Welcome, {login}')