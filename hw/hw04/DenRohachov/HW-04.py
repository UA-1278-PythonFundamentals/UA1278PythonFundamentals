### HW 4

temperature = float(input("Вкажить температуру в цельсія: "))
convert = (temperature * 9/5) + 32
if temperature >= -273.15:
    print(float(temperature), "C = ", convert, " F")
else:
    print("Error: Temperature below absolute zero (-273.15 C)\nInput is:",temperature, "C")