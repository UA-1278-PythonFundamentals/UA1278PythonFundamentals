# first task
a = ([1,2,22,534,23,467.0,256,1357])
for i in a:
    if type(i) is int:
        print (float(i))
    else: print("Error")



# second task

n = int(input('Enter n: '))
num1 = 0
num2 = 1
while True:
    next_number = num1
    if next_number > n:
        break
    num1 = num2
    num2 = next_number + num1
    print(next_number, end=' ')



# third task
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f'Factorial of number {i} is {fact}.')