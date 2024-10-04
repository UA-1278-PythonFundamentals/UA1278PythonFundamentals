temperature_celsius = float(input("Enter temperature in Celsius: "))
if temperature_celsius <= -273.15:
    print ("Error: Temperature below absolute zero (-273.15°C)")
else: print (f"{temperature_celsius}°C is equivalent to {(temperature_celsius * 9/5) + 32}°F")
   