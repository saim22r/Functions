# Python OOP
- Four Pillars of OOP
- Functions and good practice of functions

## First Iteration
```
def greeting():
    print("Welcome")

greeting() # You have to call the function to execute the code
```
- Pass is the keyword that allows the ineterpretor to skip without any errors
- DRY (Don't Repeat Yourself) declare functions and reuse code
### Second Iteration (Use return statement)
```
def greeting():
    print("Good morning!")
    return "Welcome"
print(greeting())
```
### Third Iteration (With user name as a string as an argument)
```
def greeting(name):
    # print(name)
    return "Welcome on Board " + name

print(greeting("Saim"))
```
- Create a function to prompt the user to enter their name and display the name back to the user with greeting message
```
def greeting(name):
    return "Welcome " + name + "!"

print(greeting(input("What is your name? ")))
```
- Let's create a function with multiple args as an int
```
def add(num1, num2):
    return num1 + num2

print(add(1, 3))

def multiply(num1, num2):
    return num1 * num2

print(multiply(4, 3))
```
- Return statement is the last line of code in a function

# Python's extensive documentation on python.org
- We have used functions that we have created as well as builtin
- Import is the keyword that is used to import any module available in python.org

## math
- import math
```
num1 = 22.44 # Float

# In real life situations you will have to round the value
# If the value is less than .50 round down. If it is .51 or above then round up

print(math.ceil(num1))
print(math.floor(num1))
print(math.pi)
```
## Random class/methods
```
import random 
print(random.random())
# Generates a random number between 0 and .99 every time the program is run
```
## How can we interact with our machine with python
```
import os # Gives info about your OS
import math, datetime, sys

work_dir = os.getcwd() # Provides current location/Path
print(work_dir)

print(datetime.date.today()) # today's date
print(sys.path)
```
## Packages (requests)

- Requests is a package to interact with a live API
- We can make an API call to any web address using python requests packages
- pip is a package manager in python to install any packages
- Type into terminal `pip install requests`
- pip -v
```
import requests

requests_api = requests.get("https://www.bbc.co.uk/")

if requests_api.status_code == 200:
    print("Success")

print(requests_api.status_code) # Status code = 200 for successful, 404 and above = failure
print(requests_api.headers)
print(requests_api.content)
```
# Object Oriented Programming (OOP)
## Four Pillars of OOP
- Abstraction: Shows only essential attributes and "hides" unnecessary information
- Inheritance: One class acquires the property of another class
- Encapsulation:  Bundling of data, along with the methods that operate on that data, into a single unit
- Polymorphism: Different classes can be used with the same interface

## Step 1: Create an animal.py file to create a parent class
### Let's create an Animal class

- Follow correct naming convention
- We need to initialise with built in method called __init__(self)
- self refers to current class

```
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
```
- Create an object of the class in order to use methods
```
cat = Animal() # Create object of Animal class
print(cat.eat())
print(snake1.use_tongue_to_smell())
```
## Step 2: Create a file called reptile.py to abstract data and inherit from animal.py
### Let's create reptile class to inherit Animal class

- Importing Animal class. Must be in the same directory
```
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
```

- Let's create an object of Reptile class
```
smart_reptile = Reptile()
# print(smart_reptile.hunt())
# print(smart_reptile.breath()) # Inherited from Animal class
```
## Step 3: Create a file called snake.py
### Let's create a class called Snake
```
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
print(snake1.use_tongue_to_smell())
```
## Step 4: Create a file called python.py and this point should be able to utilise inheritance from multiple classes 
### Let's create python class
```
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
```