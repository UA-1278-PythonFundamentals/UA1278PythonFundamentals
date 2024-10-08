# FIRST TASK
Odd = []
Even = []
Other = []
for i in range(1,11):
    if i % 6 == 0:
        Even.append(i),
        Odd.append(i)
    elif i % 2 == 0:
        Odd.append(i)
    elif i % 3 == 0:
        Even.append(i)
    else: Other.append(i)
print (f"Odd numbers: {Odd}")
print (f"Even numbers: {Even}")
print (f"Other numbers: {Other}")



# SECOND TASK
login = input("Enter login:")
while login == "First":
    print ("Congratulations")
    break