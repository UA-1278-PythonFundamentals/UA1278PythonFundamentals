temp = float(input("Enter temperature in Celsius: "))
formula = (temp * 9/5) + 32
fahrenheit = round(formula, 2)

if temp < -273.15:
    print("Error: temperature bellow absolute zero(-273.15)")
else:
    print(f"{temp}°C is equivalent to {fahrenheit}°F")