def process_age(user_age):
    if user_age < 0:
        raise ValueError("Age can not be negative")

    return "age is even" if user_age % 2 == 0 else "age is odd"


if __name__ == "__main__":
    age = int(input("Enter age: "))
    try:
        print(process_age(age))
    except ValueError as e:
        print(e)
