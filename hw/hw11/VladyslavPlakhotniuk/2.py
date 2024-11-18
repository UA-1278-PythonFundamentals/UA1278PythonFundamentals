def get_day_of_week(number):
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }
    if number in days:
        return days[number]
    else:
        raise ValueError("Число має бути від 1 до 7.")

try:
    user_number = int(input("Введіть число (1-7): "))
    day = get_day_of_week(user_number)
    print("День тижня:", day)
except ValueError as e:
    print("Помилка:", e)
except Exception:
    print("Некоректне введення. Будь ласка, введіть числове значення від 1 до 7.")
