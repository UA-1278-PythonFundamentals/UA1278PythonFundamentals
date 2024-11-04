class Human:
    def __init__(self, name):
        self.name = name

    def hi(self):
        return f"Hello {self.name},"    
    
    @classmethod
    def ha(cls):
        return "You are Homosapiens,"
    
    @staticmethod
    def he():
        return "Welcome"
    
a = Human("Vlad") 
print (a.hi(), a.ha(), a.he())