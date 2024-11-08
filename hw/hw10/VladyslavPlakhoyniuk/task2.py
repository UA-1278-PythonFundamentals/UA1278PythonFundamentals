class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привіт, {self.name}! Ласкаво просимо!")

    @classmethod
    def species(cls):
        return "Це вид: Homosapiens"

    @staticmethod
    def random_message():
        return "Це довільне повідомлення."

human1 = Human("Олександр")
human1.greet()
print(Human.species())
print(Human.random_message())
