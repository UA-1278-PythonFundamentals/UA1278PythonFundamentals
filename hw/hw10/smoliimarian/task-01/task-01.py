class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rec = Rectangle(5, 10)

print(rec.area())
