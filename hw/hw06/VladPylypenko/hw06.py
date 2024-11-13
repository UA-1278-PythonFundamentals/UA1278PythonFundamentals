a=([1,2,3,4,5,6,7,8,9])
n=[]
b=[]
c=[]
for i in a:
    if i % 2 == 0:
        n.append(i)

print(f"nbmbers {n} is divisible by 2")
for i in a:
    if i % 3 == 0:
        b.append(i)

print(f"nbmbers {b} is divisible by 3")
for i in a:
    if i % 2 == 0 and i % 3 ==0:
        c.append(i)

print(f"nbmbers {c} is divisible by 2 and 3")


print("")
print("Task 2")
print("")

a = "Vlad"
b=6

while True:
    n = input("entr your login: ")
    if n != "Vlad":
        b = b-1
        if b == 0:
            print("")
            print("You haven't any chances, try next time")
            break
        print(f"Wrong answer, you have {b} attempts left")

    else:
        print(f"Wellcome {a}")
        break