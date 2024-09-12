# Using if statements with Lists

requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green pepper':
		print("Sorry, we're out of green peppers right now")
	else:
		print("Adding {requested_topping}")

print("\nFinished making Pizza")

# Checking that a list is not empty

requested_toppings = [] # When the list of a list is used in an if statement. Python returns True if the list contains at least one item, 
						# An empty list evaluates to False

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print("Finished making Pizza")
else:
	print("Are you sure you want a plain Pizza.\n")



# Exercise

# 5-8 Hello Admin
usernames = ['admin', 'jack', 'jadon', 'messi', 'ronaldo']

for username in usernames:
	if username == 'admin':
		print(f"Hello {username}, would you like to see the status report?\n")
	else:
		print(f"Hello {username}, thank you for logging in again.\n")

# 5-9 No users
usernames = []

if usernames:
	for username in usernames:
	if username == 'admin':
		print(f"Hello {username}, would you like to see the status report?\n")
	else: # mistake: didn't wrote this and the below line
		print(f"Hello {username}, thank you for logging in again.\n")
else:
	print("We need to find some users.\n")

# 5-10 Checking Usernames

current_users = ['aamir', 'deadboy', 'demon', 'messi', 'alvarez']
new_users = ['Eve', 'steve', 'MESSI', 'Deadboy', 'tony']

for user in new_users:
	if user.lower() in current_users:
		print(f"\nusername {user} already exists.\nPlease enter new username.\n")
	else:
		print('Account is successfully created.')

# 5-11 Ordinal Numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] mistake
numbers = list(range(1, 10))

for n in numbers:
	if n == 1:
		print(f'{n}st')
	elif n == 2:
		print(f'{n}nd')
	elif n == 3:
		print(f'{n}rd')
	else:
		print(f'{n}th')



















# Corey Schafer

#Conditionals and Booleans

#Comparisons

#Assignment:   num = 2
#Equal: 3 == 2
#Not Equal: 3 != 2
#Greater Than: 3 > 2
#less than: 3 < 2
# Greater or Equal: 3 >= 2
#less or equal: 3 <= 2
# Object Identity: is

language = "python"

if language == "python":
	print('Conditional is True')
else:
	print('Not Conditional')

if language == "python":
	print('Conditional is True')
elif language == 'Java':
	print('Language is Java  ')
elif language == 'Javascript':
	print('Language is Javascript  ')
else:
	print('Not Conditional')


#Boolean Operators
#and
#or
#not

user = 'Admin'
logged_in = True

#Both should be True if and is used
if user == 'Admin' and logged_in:
	print('Account Logged In')
else:
	print("Bad Creds")

#Anyone should be True if or is used
if user == 'Admin' or logged_in:
	print('Account Logged In')
else:
	print("Bad Creds")

# using not
if not logged_in:
	print('please log in')
else:
	print("Bad Creds")

# Object Identity: is

# it checks if the two things have the same identity or not

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b) # when using == we got the answer as True because both the variable were identical
print(a is b) # when using is keyword we got the answer as False because although they were identical they have different id i.e they were both stored in different memory location


c = [1, 2, 3]
d = c
print(id(c))
print(id(d))
print(c == d) #this is true because now c and d both have been given the same assignment
print(c is d) #this is also true because d is pointing to c that means both will have the same id

# in conclusion (c is d) can be written as (id(c) == id(d))

# False Values in Python
	# False
	# None
	# Zero of any numeric type: 0 evaluates to false
	# Any Empty sequence. For Example: '', (), [],
	# Any Empty Mapping. For Example: {}