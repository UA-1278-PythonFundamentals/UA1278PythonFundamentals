print("first task:")
l = [1, 2, 3, 45, 75369, 732]
print(f"\t List that contains elements of integer type: {l}; {type(l[0])}")
for i in range(len(l)):
    l[i] = float(l[i])
print(f"\t List that contains elements of floating type: {l}; {type(l[0])}", "\n ------------------------------------------------------------")

print("\n second task:")
n = int(input("\t Enter the number n for the Fibonacci sequence: "))
print("\t Sequence of Fibonacci numbers: ")
for i in range(n):
    if i == 0:
        previous_number_1 = i
        print("\t", i, end = "")
    elif i == 1:
        next_number = previous_number_1 + i
        previous_number_2 = next_number
        print(",", next_number, end = "")
    else:
        next_number = previous_number_2 + previous_number_1
        previous_number_1 = previous_number_2
        previous_number_2 = next_number
        print(",", next_number, end = "")
print("\n ------------------------------------------------------------")

print("\n third task:")
number = int(input("\t Enter the number that factorial you want to calculate: "))
result = 1
for i in range(1,number+1):
    if number == 0:
        break
    else:
        result *= i
print(f"\t {number}! = {result}", "\n ------------------------------------------------------------")

        

