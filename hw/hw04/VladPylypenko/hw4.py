temp = float(input("Enter the temperature in Celsius: "))

absolute_zero = -273.15

if temp < absolute_zero:
    print(f"Temperature below absolute zero. ({absolute_zero} ℃)")
else:
    temp_in_fahrenheit = (temp * 9 / 5) + 32
    print(f"{temp} ℃ is equivalent to {temp_in_fahrenheit} ℉")