# 05.1 Practical tasks / [GitHub]

# Task 1 var 1
print()
print("T1 v1")
intiger = 1, 2, 3, 5, 10
convert_to = []
for i in intiger:
    convert_to.append(float(i))
print(convert_to)


# Task 1 var 2
print()
print("T1 v2")
intiger = [1, 2, 3, 5, 10]
for i in range(len(intiger)):
    intiger[i] = float(intiger[i])
print(intiger)


# Task 2
print()
print("T2")
n = int(input("Input a number: "))
n1 = 0
n2 = 1
while n > 0:
    print(n1)
    n1, n2 = n2, n2 + n1
    n -= 1


# Task 3
print()
print("T3")
num =  int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Number low 0")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
        print("The factorial of ",num," is ", factorial)