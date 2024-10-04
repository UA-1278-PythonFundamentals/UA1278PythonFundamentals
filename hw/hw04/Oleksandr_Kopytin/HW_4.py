def temperature_converter():
    while True:
        temp_cel = input("Enter the temperature in Celsius(q - quit): ")

        if temp_cel == "q":
            break

        temp_cel = float(temp_cel)
        if temp_cel > -237.15:
            print(f"{temp_cel}°C is equivalent to {(temp_cel * (9/5)) + 32}°F")
        else:
            print("Error: Temperature below or equal absolute zero (-237.15°C)")


if __name__ == "__main__":
    temperature_converter()
