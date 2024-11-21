even_numbers_divisible_by_2 = []
odd_numbers_divisible_by_3 = []
numbers_not_divisible_by_2_or_3 = []

for num in range(1, 11):
    if num % 2 == 0:  
        even_numbers_divisible_by_2.append(num)
    elif num % 3 == 0 and num % 2 != 0:  
        odd_numbers_divisible_by_3.append(num)
    elif num % 2 != 0 and num % 3 != 0:  
        numbers_not_divisible_by_2_or_3.append(num)

        while True:
    login = input("Enter your login: ") 
    if login == "First":
        print("Hello, First!")
        break 
    else:
        print("Error: Incorrect login, please try again.")
