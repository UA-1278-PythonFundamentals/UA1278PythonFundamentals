
#Temperature Converter - converts the temperature from Celsius to Fahrenheit

temper_celcium = float(input("Enter the temperatur in Celcium: ==>  "))
absolute_zero = -273.15
if temper_celcium >= absolute_zero:
    temper_in_farengete = ((temper_celcium*9/5) +32)
    print(f'{temper_celcium}°C is equivalent to {temper_in_farengete}°F')
else:
    print('Error: Temperature below absolute zero (-273.15°C)')