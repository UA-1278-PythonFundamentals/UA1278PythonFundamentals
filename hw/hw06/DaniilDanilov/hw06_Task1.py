# In the range from 1 to 10 determine 
#  • even numbers that are divisible by 2,
#  • odd numbers, which are divisible by 3,
#  • numbers that are not divisible by 2 and 3.

all_number = []
even_numbers = []
odd_numbers = []
other_numbers = []

for a in range(0, 11):
    all_number.append(a)
    if a % 2 == 0:
        even_numbers.append(a)
    elif a % 3 == 0:
        odd_numbers.append(a)
    elif a % 2 != 0 and a % 3 != 0:
        other_numbers.append(a)

print("All numbers:", all_number)
print("Even numbers that are divisible by 2:", even_numbers)
print("Odd numbers, which are divisible by 3:", odd_numbers)
print("Numbers that are not divisible by 2 and 3:", other_numbers)
