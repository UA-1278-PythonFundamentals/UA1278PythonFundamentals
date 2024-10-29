class Polygon:
    def __init__(self, *sides):
        self.sides = sides

    def square(self):
        pass


class Rectangle(Polygon):
    def __init__(self, side_1, side_2):
        super().__init__(side_1, side_2)
        self.side1 = side_1
        self.side2 = side_2

    def square(self):
        return self.side1 * self.side2


r = Rectangle(2, 6)

print(r.square())
