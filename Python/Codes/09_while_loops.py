# Letting user choose when to quit

prompt = "Tell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program"
prompt += "\nType Here: "

# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	print(f"Repeat: {message}")




# Using a FLAG

# active = True
# while active:
# 	message = input(prompt)
# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(f"Repeat: {message}\n")




# Using break statement to exit a loop

# while True:
# 	message = input(prompt)
# 	if message == 'quit':
# 		break
# 	else:
# 		print(f"Repeat: {message}\n")





# Using a Continue statement
# --> Rather than breaking out of a loop entirly without executing the rest of the code, we can use the continue statement to return to the beginning of the loop based on the result of a conditional test

# Loop that counts from 1 to 10 but only prints odd numbers
# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue
# 	else:
# 		print(current_number)


# Exercise 2

# 7-4 Pizza Topping







# Moving Items from one list to another

# unconfirmed_users = ['Alice', 'brian', "Candice"]
# confirmed_users = []

# while unconfirmed_users:
# 	current_users = unconfirmed_users.pop() 

# 	print(f"Verifying users: {current_users.title()}")
# 	confirmed_users.append(current_users)

# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user)




# Removing all instances of specific values from a list

pets = ['dog', 'cat', 'hen', 'cat', 'rabbit', 'cat', 'goldfish', 'cat']

print(pets)
while 'cat' in pets:
	pets.remove('cat')

print(pets)






# Filling a Dictionary with user Input

responses = {}  # defining empty dictionary

polling_active = True # Flag to indicate that the polling is active

while polling_active:
	name = input("What is your name?: ")
	reponse = input("Which Ice-Cream do you want to eat?: ")

	# Storing responses in the dictionary
	responses[name] = reponse

	# Finding out if anyone else i going to take the poll
	repeat = input("Would you like to let another person take the poll? (yes/no)")
	if repeat == 'no':
		polling_active = False

# Polling is complete
print("\n---Poll Results---")
for name, response in responses.items():
	print(f"{name}, here is your {response} Ice-Cream.")







# Corey Schafer

# While Loops
# It will run infinely if the condition is true
# x = 0
# while x < 5:
# 	print(x)
# 	x += 1

# The below while loop will run infinitely To stop this we whave to use break for the loop to end
# while True:
# 	print(x)
# 	x += 1
 # CTRL + C can used to get out of the loop