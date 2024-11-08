class Human:

    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f'Welcome {self.name}!'

    @staticmethod
    def species():
        return 'Homosapiens'


o = Human('Olga')
print(o.greetings())
print(o.greetings(), Human.species())

