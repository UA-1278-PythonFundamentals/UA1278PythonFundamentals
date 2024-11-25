# Task 01 - Temperature Converter

celsius_temp = int(input("Enter the temperature in Celsius: "))

# didn't check input, because of assumption
# that user will enter a valid input

DEGREE_SIGN = u'\N{DEGREE SIGN}'
CELSIUS_ABSOLUTE_ZERO = -273.15

if float(celsius_temp) < CELSIUS_ABSOLUTE_ZERO:
        fahrenheit_temp = int((celsius_temp * 9/5) + 32)
        print(f"{celsius_temp}{DEGREE_SIGN}C is equivalent to {fahrenheit_temp}{DEGREE_SIGN}F")
else:
    print(f"Error: Temperature below absolute zero ({CELSIUS_ABSOLUTE_ZERO}{DEGREE_SIGN}C)")