# Task2. Create a class Human, everyone has a name, 
# create a method in the class that displays a welcome message to each person. 
# Create a class method in the class that returns information 
# that it is a species of "Homosapiens". 
# And in the class create a static method that returns an arbitrary message.

class Human:
    """Class Human"""
    
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


olga = Human("Jhon Doe")
print(olga.welcome() + ' ' + olga.species())

vasyl = Human("Jane Doe")
print(vasyl.welcome() + ' ' + vasyl.species())

print(Human.species()) # Homosapiens