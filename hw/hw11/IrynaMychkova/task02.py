# 2. Write a program that analyzes the entered number and, depending on the number, 
# gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). 
# Take into account cases of entering numbers from 8 and more, 
# as well as cases of entering non-numerical data.

def check_day(day: str) -> str:
    try:
        day = int(day)
        if day < 1:
            raise ValueError("Day cannot be less than 1")
        if day > 7:
            raise ValueError("Day cannot be more than 7")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day - 1]
    except ValueError as e:
        return str(e)
    
print(check_day(input("Enter the day of the week: ")))