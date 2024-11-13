try:
    a = int(input("Write a number from 1 to 7: "))
    if a <=0 or a >= 8:
        raise ValueError("You input wrong data")
    elif a == 1:
        print("Monday")
    elif a == 2:
        print("Tuesday")
    elif a == 3:
        print("Wednesday")
    elif a == 4:
        print("Thursday")
    elif a == 5:
        print("Friday")
    elif a == 6:
        print("Saturday")
    elif a == 7:
        print("Sunday")
except ValueError as e:
    print("We obtain error:", e.data)