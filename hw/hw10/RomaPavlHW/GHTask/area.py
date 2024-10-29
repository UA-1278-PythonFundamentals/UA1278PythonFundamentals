import math

class Pol:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def calc_area(self):
        print( (self.a * self.b**2)/(4 * math.tan(math.pi / self.a)))

class Rect(Pol):
    def calc_area(self):
        print(self.a * self.b)


pol = Pol(4, 6)
pol.calc_area()

rec = Rect(4,6)
rec.calc_area()