# Task2. Create a class Human, everyone has a name, 
# create a method in the class that displays a welcome message to each person. 
# Create a class method in the class that returns information 
# that it is a species of "Homosapiens". 
# And in the class create a static method that returns an arbitrary message.

class Human:
    """Class Human"""

    __name:str = ""
    
    def __init__(self, name:str):
        """
        Constructor
        :param name: str
        """

        self.__name = name

    def welcome(self) -> str:
        """
        Method welcome
        :return: str
        """

        return f"Hello, {self.__name}!"
    
    @staticmethod
    def species() -> str:
        """
        Method species
        :return: str
        """

        return "Homosapiens"


olga = Human("Olga")
print(olga.welcome()) # Hello, Olga!
print(olga.species()) # Homosapiens

vasyl = Human("Vasyl")
print(vasyl.welcome()) # Hello, Vasyl!
print(vasyl.species()) # Homosapiens

print(Human.species()) # Homosapiens