temp_in_celsius = float(input("Enter the temperature in Celsius: "))

ABSOLUTE_ZERO = -273.15

if temp_in_celsius < ABSOLUTE_ZERO:
    print(f"Temperature below absolute zero. ({ABSOLUTE_ZERO} ℃)")
else:
    temp_in_fahrenheit = (temp_in_celsius * 9 / 5) + 32
    print(f"{temp_in_celsius} ℃ is equivalent to {temp_in_fahrenheit} ℉")
