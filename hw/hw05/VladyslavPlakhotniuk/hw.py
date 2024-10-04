#task1
a = [1, 3, 5, 87, 34, 232, 233, 9]
for reverse in a:
    print(float(reverse))


#task2
n = int(input(":"))
a, m = 0,1
for sum in range(n):
    if a > n:
        break
    print(a, " ")
    a, m = m, a + m


#task3
n = int(input(":"))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факторіал {n} = {factorial}")