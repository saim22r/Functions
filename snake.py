# Let's create a class called Snake

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True

# Lets add some specific methods/behaviours
    def use_tongue_to_smell(self):
        return "I can smell"

snake1 = Snake()

# print(snake1.use_tongue_to_smell())