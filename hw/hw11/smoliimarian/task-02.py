def day_of_week(num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if num not in days:
        raise ValueError("Invalid day of the week.")
    return days[num]


if __name__ == "__main__":
    try:
        day = int(input("Enter a number for the day of the week: "))
        print(day_of_week(day))
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
