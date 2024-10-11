###############################################################################
# Task1. In the range from 1 to 10 determine
#   • even numbers that are divisible by 2,
#   • odd numbers, which are divisible by 3,
#   • numbers that are not divisible by 2 and 3.

even_divizible_by_2 = [x for x in range(1, 11) if x % 2 == 0]
print(f'Even numbers that are divisible by 2: {even_divizible_by_2}')

odd_divizible_by_3 = [x for x in range(1, 11) if x % 3 == 0 and x % 2 != 0]
print(f'Odd numbers that are divisible by 3: {odd_divizible_by_3}')

not_divizible_by_2_and_3 = [x for x in range(1, 11) if x % 3 != 0 and x % 2 != 0]
print(f'Numbers that are not divisible by 2 and 3: {not_divizible_by_2_and_3}')

