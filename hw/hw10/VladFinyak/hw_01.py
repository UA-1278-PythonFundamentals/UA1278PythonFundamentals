class Polygon:
    def __init__(self):
        pass

class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def square(a,b):
        return f"Square= {a * b}"    
    
g = Rectangle
print (g.square(5, 50))    
