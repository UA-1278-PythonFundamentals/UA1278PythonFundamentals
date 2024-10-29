# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

print(print ("\n\n\n\n\n##############################(Task1)#################################\n\n\n\n"))


even_numbers  = []
odd_numbers   = []
not_divisible = []
for i in range(1, 11):
    if i % 2 == 0:
       even_numbers.append(i)
    if i % 3  == 0: 
        odd_numbers.append(i)
    if i % 2 != 0 and i % 3 != 0:
        not_divisible.append(i)

print(f'Even numbers is: {even_numbers}')
print(f'Odd numbers is: {odd_numbers}')
print(f'Not divisible is: {not_divisible}')


# COMPREHENSIONS

even_num2 = [i for i in range(1, 11) if i % 2 == 0]
print(even_num2)

odd_num2 = [i for i in range(1, 11) if i % 3 == 0]
print(odd_num2)

not_divisible2 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]
print(not_divisible2)