# Function
# def greet_user(username): # username is the parameter
# 	print(f"Hello, {username.title()}")
# greet_user("aamir") # aamir is the argument




# Positional Arguments --> Arguments should match with the sequence of the parameters
# def describe_pet(animal_type, pet_name):
# 	print(f"\nI have a {animal_type}")
# 	print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet("dog", "jack")




# Keywords Arguments --> Argument and parameter's sequence are not required as we are providing arguments with the appropriate parameter's knwon as keywords we want to associate them with

# def describe_pet(animal_type, pet_name):
# 	print(f"\nI have a {animal_type}")
# 	print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet(pet_name="jack", animal_type="dog")






# Default Values --> If an argument is not passed for a parameter it uses it's default value
# def describe_pet(pet_name, animal_type = "dog"):
# 	print(f"\nI have a {animal_type}")
# 	print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet(pet_name="jack")
# Note: Always write parameters without default values before the parameter with default values







# Equivalent Function Calls
# A dog named jack
# describe_pet("jack")
# describe_pet(pet_name="jack")

# # A hamster named harry
# describe_pet("harry", "hamster")
# describe_pet(pet_name="harry", animal_type="hamster")
# describe_pet(animal_type="hamster", pet_name="harry")

# Each of these function calls would have the same output as the previous examples






# Returning a sample value
# def get_formatted_name(f_name, l_name):
# 	"""Return a full name, neatly formatted"""
# 	full_name = f"{f_name} {l_name}"
# 	return full_name.title()

# musician = get_formatted_name('harry', "potter")
# print(musician)

# Note: When you call a function that returns a value, you need to provide a variable that the retrun value can be assigned to






# Making an Argument Optional
# def get_formatted_name(f_name, l_name, m_name=""):
# 	"""Return a full name, neatly formatted"""
# 	if m_name:
# 		full_name = f"{f_name} {m_name} {l_name}"
# 	else:
# 		full_name = f"{f_name} {l_name}"
# 	return full_name.title()

# musician = get_formatted_name('harry', "potter")
# print(musician)

# musician = get_formatted_name('harry', "potter", "lee")
# print(musician)

# Note: Python intrepret non empty string as True, so if m_name evaluates to True, full_name with m_name will be given as output





# Returning a Dictionary
# def build_person(f_name, l_name):
# 	"""Return a Dictionary of info about a person"""
# 	person = {'first': f_name, 'last': l_name}
# 	return person

# musician = build_person("Harry", "Potter")
# print(musician)

# Extending the above Dictionary
# def build_person(f_name, l_name, age=None):
# 	"""Return a Dictionary of info about a person"""
# 	person = {'first': f_name, 'last': l_name}
# 	if age:
# 		person['age'] = age
# 	return person

# musician = build_person("Harry", "Potter", age = 27)
# print(musician)






# Using the function with a While Loop
# def get_formatted_name(f_name, l_name):
# 	"""Return a full name, neatly formatted"""
# 	full_name = f"{f_name} {l_name}"
# 	return full_name.title()

# while True:
# 	print("\nPlease tell me your name: ")
# 	print("(enter 'q' at any time to quit)")

# 	f_name = input("First name: ")
# 	if f_name == 'q':
# 		break

# 	l_name = input("Last name: ")
# 	if l_name == 'q':
# 		break

# 	formatted_name = get_formatted_name(f_name, l_name)
# 	print(f"\nHello, {formatted_name.title()}")







# Passing a List
def greet_users(names):
	"""Print a simple greet to each user in the list"""
	for name in names:
		msg = f"Hello, {name.title()}"
		print(msg)

usernames = ["hannah", "clay", "dustin"]
greet_users(usernames)






# Modifying a List in Function
# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent








# Corey Schafer

# Functions

# def hello_func(): # Functions are defined by using the def keyword and () is used to declare parameters it can be empty if there are no parameters
# 	print('Hello Fucntion')
# 	# pass --> a function can be kept empty by using the pass keyword

# hello_func() # Function is called like this () is compulsory to be present

# Functions are used to keep the code DRY (Don't Repeat Yourself)

# def greet_func(greeting, name = "You"): #here we are declaring parameters, name='You' means You is the default of the name parameter, if nothing is declared for name parameter the You is going to be used
# 	return '{}, {}'.format(greeting, name) # Return -->  learn more about this concept

# print(greet_func('Hi'))

# # Know more about the below concept
# def student_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)

# courses = ['Maths', 'Art']
# info = {'name': 'John', 'age': 22}

# student_info(courses, info)
# student_info(*courses, **info)

# know the difference between the above 2 statements



# Leap Year checker and days in month provider

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# # Creating a leap year function
# def is_leap(year):
# 	"""Returns True for leap year and False for Non Leap year"""
# 	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# # Days in Month Checker
# def days_in_month(year, month):
# 	""" Returns number of days in that month in that year"""
# 	if not 1 <= month <= 12:
# 		return 'Invalid Month'

# 	if month == 2 and is_leap(year):
# 		return 29

# 	return month_days[month]


# # print(is_leap(2020))
# print(days_in_month(2017, 2))

