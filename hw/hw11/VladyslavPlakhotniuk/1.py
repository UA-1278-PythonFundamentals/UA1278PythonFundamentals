def process_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від’ємним.")
    elif age % 2 == 0:
        return "Ваш вік парний."
    else:
        return "Ваш вік непарний."

try:
    user_age = int(input("Введіть свій вік: "))
    result = process_age(user_age)
    print(result)
except ValueError as e:
    print("Помилка:", e)
except Exception:
    print("Некоректне введення. Будь ласка, введіть числовий вік.")
