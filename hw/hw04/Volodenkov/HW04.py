
# Task1 
c = float(input("Enter the temperature in Celsius: "))
if c < -273.15:
	print("Error: Temperature below absolute zero (-273.15°C)")
else:
	f = c * 9/5 + 32
	print(f"{c}°C is equivalent to {f}")

