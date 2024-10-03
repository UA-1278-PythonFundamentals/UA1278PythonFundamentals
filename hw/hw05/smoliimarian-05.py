# # TASK 1

int_num_list = [1, 3, 14, 42, 56, 133, 5]
float_num_list = []

for num in int_num_list:
    float_num_list.append(float(num))

print(float_num_list)

# # TASK 2

num = int(input("Enter a number: "))

a, b = 0, 1

for i in range(num):
    if a > num:
        break
    print(a)
    temp = a
    a = b
    b = temp + b


# TASK 3

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
