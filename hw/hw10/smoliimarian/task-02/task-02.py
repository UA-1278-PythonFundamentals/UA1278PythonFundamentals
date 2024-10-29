class Human:
    species_msg = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def wellcome_msg(self):
        return f"Hello, {self.name}"

    @classmethod
    def species(cls):
        return cls.species_msg

    @staticmethod
    def static_method():
        return "I am a static method"


person = Human("John")

print(person.wellcome_msg())
print(Human.species())
print(Human.static_method())
