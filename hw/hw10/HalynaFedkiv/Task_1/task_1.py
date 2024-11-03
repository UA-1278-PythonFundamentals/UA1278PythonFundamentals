class Polygon:

    def __init__(self):
        pass


class Rectangle(Polygon):

    def __init__(self, length, width):
        Polygon.__init__(self)
        self.length = length
        self.width = width

    def rectangle_area(self):
        return f'The area of the rectangle is {round(self.length * self.width, 2)}'


pol = Rectangle(2, 5)
print(pol.rectangle_area())
