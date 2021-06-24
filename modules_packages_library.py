# Python's extensive documentation on python.org
# - We have used functions that we have created as well as builtin
# - Import is the keyword that is used to import any module available in python.org

## math
# import math
# import random # generates a random number
#
# num1 = 22.44 # Float
#
# # In real life situations you will have to round the value
# # If the value is less than .50 round down. If it is .51 or above then round up
#
# print(math.ceil(num1))
# print(math.floor(num1))
# print(math.pi)
#
# ## Random class/methods
# import random # generates a random number
# print(random.random())
# # - Generates a random number between 0 and .99 every time the program is run

# How can we interact with our machine with python
# import os # Gives info about your OS
# import math, datetime, sys
#
# work_dir = os.getcwd() # Provides current location/Path
# print(work_dir)
#
# print(datetime.date.today()) # today's date
# print(sys.path)

# Requests is a package to interact with a live API
# We can make an API call to any web address using python requests packages
# pip is a package manager in python to install any packages
# Type into terminal `pip install requests`
# pip -v

import requests

requests_api = requests.get("https://www.bbc.co.uk/")

if requests_api.status_code == 200:
    print("Success")

print(requests_api.status_code) # Status code = 200 for successful, 404 and above = failure
print(requests_api.headers)
# print(requests_api.content)
