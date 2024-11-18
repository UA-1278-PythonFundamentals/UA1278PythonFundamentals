DAYS = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"}

if __name__ == "__main__":
    day_of_week = input("Enter a number of day: ")
    try:
        print(DAYS[day_of_week])
    except KeyError:
        print("Number of day can not be lees or equal 0 or greater than 7 or data was non-numerical")
