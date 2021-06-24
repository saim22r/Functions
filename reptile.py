# Let's create reptile class to inherit Animal class

## Importing Animal class. Must be in the same directory
from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__() # Super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "It's chilly looking, go in the sun!"

    def hunt(self):
        return "Keep working hard to find food"

    def use_venom(self):
        return "I'll use it if i have to"

# Let's create an object of Reptile class
smart_reptile = Reptile()
# print(smart_reptile.hunt())
# print(smart_reptile.breath()) # Inherited from Animal class