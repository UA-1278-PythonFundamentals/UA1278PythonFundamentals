# Regular Ball Super Ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)  #=> "regular"
print(ball2.ball_type)  #=> "super"


# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

# from random import choice
class Ghost(object):
    count = 0

    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        Ghost.count += 1
        self.color = colors[Ghost.count % len(colors)]


ghost = Ghost()
print(ghost.color)  #=> "white" or "yellow" or "purple" or "red"
ghost2 = Ghost()
print(ghost2.color)


# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects
# (representing Adam and Eve). The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.

def God():
    return adam, eve


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


adam = Man()
print(adam)
eve = Woman()
print(eve)
result = [adam, eve]
print(result)


# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number, c
# omplete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        self.info = f"{name}s age is {age}"

    def getInfo(self):
        return self.info


obj = Person('john', 34)
print(obj.getInfo())

# Now that we have a Block let's move on to something slightly more complex: a Sphere.
PI = 3.14159265359


class Sphere(object):

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4 / 3) * PI * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * PI * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


ball = Sphere(2, 50)
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())


# some function, which could change name of given class.

def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper() and new_name != False and not new_name[0].isdigit():
        cls.__name__ = new_name
    else:
        raise ValueError(
            'Invalid class name. It must start with an uppercase letter and contain only alphanumeric characters ')


class MyClass:
    pass

