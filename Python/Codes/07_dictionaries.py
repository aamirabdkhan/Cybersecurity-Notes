# Exercise 1



fav_lang = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'C++'
}

# Looping through all key-value pairs
for name, lang in fav_lang.items(): # When you have to loop through both key and value the you should use items() method
	print(f"{name.title()}, you have polled for {lang.upper()}")
print('\n')



# Looping through all the keys

	# Method 1 --> # using the keys() method
for name in fav_lang.keys(): 
	print(f'Key: {name.title()}')
print('\n')

	# Method 2 --> Not using the keys() method
for name in fav_lang: 
	print(f'Key: {name.title()}')
print('\n')



# Looping by keys
friends = ['phil', 'sarah']
for name in fav_lang.keys():
	print(f'Hi {name.title()}')

	if name in friends:
		language = fav_lang[name].title()
		print(f'\t{name.title()}, I see you love {lang.title()}')
print('\n')



# Looping through dictionary in a particular order
for name in sorted(fav_lang.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
print('\n')




# Looping through all the Values in a dictionary
print("The following Languages have been mentioned: ")
for lang in fav_lang.values():
	print(lang.title())
print('\n')

	# The above method will show every values that are present in the dictionary without checking for the repeats.

	# To avoid repeatation we should use sets
	# SET --> A collection in which each item is unique.

for lang in set(fav_lang.values()):
	print(lang.title())
print('\n')


# Exercise 

# 6-7 People

person_0 = {
	first_name : "Aamir",
	last_name : "Khan",
	age : 21,
	city : "Mumbra"
}

person_1 = {
	first_name : "Aquib",
	last_name : "Khan",
	age : 20,
	city : "Mumbra"
}

person_2 = {
	first_name : "Asjad",
	last_name : "Khan",
	age : 11,
	city : "Mumbra"
}












# Corey Schafer
#dictionaries

student = {'name': 'John', 'age': 21, 'courses':['Math', 'CompSci']}
# in the above line we defined the the dictionary with {} and there are key value pairs present in it, left side of the semi-colon is KEY and right side of the semi-colon is VALUE

print(student) #printing the whole dictionary
print(student['name']) #printing the value of a particular KEY

print(student.get('phone')) #commonly this is use to access the value of the dictinary because instead of getting error for an non existing item we will get none for it
print(student.get('phone', 'Not Found')) # if the phone key is not present the we will get Not Found instead of None

student['Phone'] = '9002929993' #adding key and value to the dictionary

student.update({'name': 'jane', 'age': 23, 'Phone': '55555555'}) # takes dict as an argument, useful when we wanted to update multiple key and values in the dict
# del student['age'] #deletes the key and value from the dict but we can save that in a variable

age = student.pop('age') #removes the mentioned key and also can be saved in a variable

print(len(student)) #key and value are combined considered as 1
print(student.keys()) #display all the keys
print(student.values()) #display all the values
print(student.items()) #display keys and values

for key in student:
	print(key)
for key, value in student.items():
 	print(f"Key: {key} & Value: {value}")