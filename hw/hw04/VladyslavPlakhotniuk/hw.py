while True:
    c = float(input(":"))
    match c:
        case temp if temp < -273.15:
            print("Помилка")
        case _:
            f = (c * 9 / 5) + 32
            print(f"Температура по Фаренгейту: {f}")