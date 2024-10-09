# Task2. Print Fibonacci numbers up to the entered number n, using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
n = int(input('Enter the number: '))

if n < 0:
    print("Incorrect input")

fibonachi = [0, 1]
next_number = 0
step = 2
while True:
    next_number = fibonachi[step - 1] + fibonachi[step - 2]
    if next_number > n:
        break
    fibonachi.append(next_number)
    step += 1

print(fibonachi)