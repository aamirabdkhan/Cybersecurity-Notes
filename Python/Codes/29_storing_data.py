# Storing Data


# Using json.dump() & json.load()




# json.dump() --> Takes two arguments: a piece of data to store and a file  object it can use to store the data

# Example

# import json
# numbers = [1,2 ,3, 4, 5,6, 7]

# filename = 'numbers.json'
# with open(filename, 'w') as f:
# 	json.dump(numbers, f)

# # json.load() to read the list back into memory
# with open(filename) as f:
# 	numbers = json.load(f)

# print(numbers




# saving and reading user-generated data

# import json


# # file 1
# username = input("What is your name? ")
# filename = 'username.json'
# with open(filename, 'w') as f:
# 	json.dump(username, f)
# 	print(f"We'll remember you when you come back, {username}")

# # file 2
# with open(filename) as f:
# 	username = json.load(f)
# 	print(f"Welcome back, {username}")


# Combining File one and file 2


import json

# Load the username if it has been stored previously
# Otherwise, prompt for the username and store it.

filename = 'username.json'

try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username}")
else:
	print(f"Welcome back, {username}")