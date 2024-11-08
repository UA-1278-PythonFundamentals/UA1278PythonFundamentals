class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print(f"Цей багатокутник має {self.sides} сторін.")

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
rect.display_info()
print(f"Площа прямокутника: {rect.area()}")
