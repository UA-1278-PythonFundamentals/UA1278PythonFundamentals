days = { 1 : "Monday",
     2 : "Tuesday",
     3 : "Wednesday",
     4 : "Thursday",
     5 : "Friday",
     6 : "Saturday",
     7 : "Sunday"}
try:
    day = int(input("Enter number 1-7 to chose day: "))
    if day > 0 and day<8:
        print (f"The day of the week for {day} is {days[day]}.")
    else:
        raise ValueError("Number must be from 1 to 7")
except ValueError as a:
    print("Invalid input:", a)

