# Let's create an Animal class

# Follow correct naming convention
# We need to initialise with built in method called __init__(self)
# self refers to current class


class Animal:
    def __init__(self): # Declare attributes in the init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "Keep breathing!"

    def eat(self):
        return "Time to eat!"

    def move(self):
        return "Move around!"


# Create an object of the class in order to use methods
cat = Animal() # Create object of Animal class
# print(cat.eat())