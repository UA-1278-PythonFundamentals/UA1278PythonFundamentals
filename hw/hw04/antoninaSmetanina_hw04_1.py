# Task1. "Temperature Converter"

temperature = int(input('Enter the temperature: '))

convert_in_fahrenheit = round((temperature * 9 / 5 + 32), 2)
if temperature <= -273.15:
    print(f'Error: Temperature below absolute zero (-273.15°C), {convert_in_fahrenheit}°F')
elif temperature > 56.7:
    print(f'Error: Temperature is very high (max 56.7°C), or {convert_in_fahrenheit}°F')
else:
    print(f'{temperature}C° is equivalent to {convert_in_fahrenheit}°F')

# Ternary operator
print(f'Error: Temperature below absolute zero (-273.15°C), {convert_in_fahrenheit}°F') if temperature <= -273.15\
    else print(f'{temperature}C° is equivalent to {convert_in_fahrenheit}°F')

