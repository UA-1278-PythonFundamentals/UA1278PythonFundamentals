class Human:
    name = "Gerge de Bill"
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def print(self):
        print(f"Hello {self.name}! You`re {self.age}")
    @classmethod
    def homo(cls):
        print(f"{cls.name} is homosapiens")

    @staticmethod
    def tones(sic):
        return str(sic)


h = Human("Harris", 27)
h.print()

Human.homo()

print(Human.tones("SHOVE IT! SHOVE IT! SHOVE IT!"))
