# Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message

class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self) -> str:
        return f'Welcome, {self.name}!'

    @classmethod
    def species(cls) -> str:
        return f'This person is Homosapiens'

    @staticmethod
    def message() -> str:
        return f'Have a great day Homosapiens!'

    def __str__(self):
        return f'Human name is {self.name}'


obj = Human('Tonya')
print(obj)
print(obj.welcome())
print(Human.species())
print(Human.message())
