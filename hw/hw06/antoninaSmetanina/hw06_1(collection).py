# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

# Approach, where iterate number in one loop
even_num = []
odd_num = []
rest_of_num = []
for i in range(1, 11):
    if i % 2 == 0:
        even_num.append(i)
    elif i % 2 != 0 and i % 3 == 0:
        odd_num.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        rest_of_num.append(i)

print(f'Even is {even_num}') # [2, 4, 6, 8, 10]
print(f'Odd is {odd_num}') # [3, 9]

print(f'Rest of digits is: {rest_of_num}') # [1, 5, 7]
print('-------------------------------------')

# Approach, where iterate number in if loop every time
even_num1 = []
odd_num1 = []
rest_of_num1 = []
for i in range(1, 11):
    if i % 2 == 0:
        even_num1.append(i)
    if i % 3 == 0:
        odd_num1.append(i)
    if i % 2 != 0 and i % 3 != 0:
        rest_of_num1.append(i)
print(f'Even numbers is: {even_num1}') # [2, 4, 6, 8, 10]
print(f'Odd numbers is: {odd_num1}') # [3, 6, 9]
print(f'Numbers that are not divisible by 2 and 3 is: {rest_of_num1}') # [1, 5, 7]

# Elegant way for list
even_num2 = [i for i in range(1, 11) if i % 2 == 0]
print(even_num2)

odd_num2 = [i for i in range(1, 11) if i % 3 == 0]
print(odd_num2)

rest_of_num2 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]
print(rest_of_num2)

even_num3 =[i for i in range(1, 11) if i % 2==0]
print (even_num3)