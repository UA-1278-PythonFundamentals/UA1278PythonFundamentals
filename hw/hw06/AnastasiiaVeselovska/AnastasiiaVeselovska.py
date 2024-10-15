print("first task:")
even, odd, l = [], [], []
for i in range(1,11):
    if i % 2 == 0:
        even.append(i)
    else:
        if i % 3 == 0:
            odd.append(i)
        else:
            l.append(i)
print(f"\t even numbers that are divisible by 2: {even}")
print(f"\t odd numbers, which are divisible by 3: {odd}")
print(f"\t numbers that are not divisible by 2 and 3: {l}")
print("\n ------------------------------------------------------------")

print("\n second task:")
while True:
    login = input("\t Еnter your login: ")
    if login == "First":
        print("\t Hello, user!")
        break
    else:
        print("\t You entered the wrong login. Try entering your login again.")
