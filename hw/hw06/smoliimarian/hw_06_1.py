even_num = []
odd_num = []
rest_num = []

for i in range(1, 11):
    if i % 2 == 0:
        even_num.append(i)
    elif i % 2 != 0 and i % 3 == 0:
        odd_num.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        rest_num.append(i)

print(f"Even numbers that are divisible by 2: {even_num}")
print(f"Odd numbers that are divisible by 3: {odd_num}")
print(f"Numbers that are not divisible by 2 and 3: {rest_num}")
