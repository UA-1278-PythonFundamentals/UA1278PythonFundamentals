### HW 06
### 06.1 Practical tasks / [GitHub]
### Task 1

# In the range from 1 to 10 determine
# - even numbers that are divisible by 2
# - odd numbers, which are divisible by 3
# - numbers that are not divisible by 2 and 3


print("Task 1")
l1 = [] # - even numbers that are divisible by 2
l2 = [] # - odd numbers, which are divisible by 3
l3 = [] # - numbers that are not divisible by 2 and 3
for i in range(10):
    i += 1
    if i % 2 == 0:
        l1.append(i)
    if i % 2 != 0:
        if i % 3 ==0:
            l2.append(i)
    if i % 2 != 0 and i % 3 != 0:
        l3.append(i)

print("even numbers that are divisible by 2: ", l1) # - even numbers that are divisible by 2
print("odd numbers, which are divisible by 3: ", l2) # - odd numbers, which are divisible by 3
print("# - numbers that are not divisible by 2 and 3: ", l3) # - numbers that are not divisible by 2 and 3

### End Task 1

print()
print("Task 2")
### Task 2

# Write a script that checks the login that the user enterers.
# If the login is «First», then greet the users.
# If the login is different, send an error message.
# (Need to use loop while)



def login(login):
    while login == "First":
        print("Logis is right. Welcome!")
        break
    else:
        print("Login is wrong!")

login(input("Please, inter the login: "))
