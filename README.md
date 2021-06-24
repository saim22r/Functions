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