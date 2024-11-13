import random


class Human:
    human_species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"welcome {self.name}"

    @classmethod
    def human_species_info(cls):
        return cls.human_species

    @staticmethod
    def arbitrary_message():
        words = ["apple", "car", "house", "hello", "bye", "sun"]
        return " ".join(random.sample(words, 5))


Alex = Human("Alex")
Bob = Human("Bob")

print(Alex.welcome_message())
print(Bob.welcome_message())

print(Human.human_species_info())

print(Human.arbitrary_message())
