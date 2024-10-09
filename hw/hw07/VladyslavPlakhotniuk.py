#task01
import math


def searchMax(num1, num2):
    """Повертає більше з двох чисел."""
    return max(num1, num2)
print(searchMax(5, 10))
print(searchMax.__doc__)

#task02
S = 0
while True:
    print("1. Трикутник")
    print("2. Прямокутник")
    print("3. Коло")
    print("4. Вихід")
    choice = input("Ваш вибір: ")
    if choice == '1':
        a = float(input("Введіть довжину сторони a: "))
        b = float(input("Введіть довжину сторони b: "))
        c = float(input("Введіть довжину сторони c: "))
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Площа трикутника: {S}")
    elif choice == '2':
        l = float(input("Введіть довжину прямокутника: "))
        w = float(input("Введіть ширину прямокутника: "))
        S = l * w
        print(f"Площа прямокутника: {S}")
    elif choice == '3':
        r = float(input("Введіть радіус кола: "))
        S = math.pi * (r ** 2)
        print(f"Площа кола: {S}")
    elif choice == '4':
        print("Вихід")
        break
    else:
        print("Error.")

#task03
def char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = str(input())
output = char(input_string)
print(output)