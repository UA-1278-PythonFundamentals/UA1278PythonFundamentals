
##########Task1##############
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in l:
    if i % 2 == 0:
        print(i)

for i in l:
    if i % 2 != 0 and i % 3 == 0:
        print(i)

for i in l:
    if i % 2 != 0 and i % 3 != 0:
        print(i)


##########Task2##############

while True:
    i = input()
    if i == "First":
        print("Hello")
    else:
        print("Error")
        break
