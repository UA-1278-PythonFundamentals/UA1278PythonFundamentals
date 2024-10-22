#task01
sequence = range(1, 11)
paired_twos = [x for x in sequence if x % 2 == 0]
odd_threes = [x for x in sequence if x % 2 != 0 and x % 3 == 0]
exclusive_nums = [x for x in sequence if x % 2 != 0 and x % 3 != 0]
print(paired_twos)
print(odd_threes)
print(exclusive_nums)

#task02
while True:
    login = input("Введіть логін: ")
    
    if login == "First":
        print("Вітаємо")
        break
    else:
        print("Помилка:")

