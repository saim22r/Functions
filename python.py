# Let's create python class

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "Eat fast without chewing"

    def climb(self):
        return "zooming"

    def __shed_skin(self):
        return "RIP skin"

python_fast = Python()

print(python_fast.climb())