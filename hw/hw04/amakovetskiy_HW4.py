
#Temperature Converter - converts the temperature from Celsius to Fahrenheit

temp_in_celsius = float(input('Enter the temperature in Celsius: '))

#first
if temp_in_celsius >= -273.15:
    temp_in_fahrenheit = (temp_in_celsius * 9 / 5) + 32
    print(f'{temp_in_celsius}°C is equivalent to {temp_in_fahrenheit}°F')
else:
    print('Error: Temperature below absolute zero (-273.15°C)')

#second
print(f'{temp_in_celsius}°C is equivalent to {(temp_in_celsius * 9/5) + 32}°F'
      if temp_in_celsius >= -273.15 else 'Error: Temperature below absolute zero (-273.15°C)')
#########
#########