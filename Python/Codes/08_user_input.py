# How to write a long prompt
prompt = "This prompt contain a very long question for the user"
prompt += "\nWhat is your name?"

# name = input(prompt)

# Numericals values in input()
# age = input("How old are you?: ")
# print(age)
# print(type(age)) # when we a give a number as an input we get str as an output 
# age = int(age)
# print(type(age)) # with this line we converted the str into int

# Exercise 1

# 7-1 Rental Car
# car = input("What kind of rental car would you like?: ")
# print(f"Let me see If I can find you a {car}")


# 7-2 Restaurant Seating
# people = input("How many of you are going to come for dinner?: ")
# people = int(people)

# if people > 8:
# 	print(f"Sorry Sir! as you are {people} people you have to wait for the table")
# else:
# 	print("Your table is ready")


# 7-3 Multiple of 10

multiple = input("Please enter a number whose multiple you want to check: ")
multiple = int(multiple)
if multiple % 10 == 0:
	print(f"Your number {multiple} is a multiple of 10")
else: 
	print(f"Your number {multiple} is not a multiple of 10")