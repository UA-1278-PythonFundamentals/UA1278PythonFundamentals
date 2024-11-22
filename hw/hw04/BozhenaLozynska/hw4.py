Celsius = float(input("Вітаю! Подай температуру  "))
if Celsius <= -273.15:
      print ("Помилка: Температура нижче абсолютного нуля (-273.15°C)")
else:
        Fahrenheit = (Celsius * 9/5) + 32
        print(Celsius, "°C еквівалентно ", Fahrenheit, "°F")