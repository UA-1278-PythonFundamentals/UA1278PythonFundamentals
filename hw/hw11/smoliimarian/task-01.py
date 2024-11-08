def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age must be a positive number.")
            return age
        except ValueError as e:
            print(f"Ivalid input: {e}. Please try again.")


def check_age_is_odd_or_even(age):
    return "even" if age % 2 == 0 else "odd"


if __name__ == "__main__":
    age = get_age()
    print(f"Your age is {check_age_is_odd_or_even(age)}.")
