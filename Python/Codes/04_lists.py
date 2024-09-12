# Modifying the List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

del motorcycles[2] # delete the item but don't let us use it
print(motorcycles)

index_popped = motorcycles.pop(0) #we can even pop any item by specifying their index number
print(index_popped)
print(motorcycles)



# Organizing the List
cars = ['audi', 'toyato', 'kia', 'bmw']
print(sorted(cars)) # gives us the sorted list but doesn't make any changes to the orignal list
print(cars)


# making Numerical Lists

for value in range(1, 6):
	print(value)

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
	# sqaure = value**2
	# squares.append(sqaure)
	squares.append(value**2)

print(squares)

# List Comprehensions --> Allows us to make same list in just one line of code

# Example
squares = [value**2 for value in range(1,11)]
print(squares)
# Explanation
# To use this syntax, begin with descriptive name for the list, such as sqaures in the above case
# Next, open a set of square brackets and define the expression for the values you want to store in the new list.
# In this example, the expression is value**2, which raises the value to the second power.
# Then write a for loop to generate the numbers you want to feed into the expressions and close the sqaure brackets.
# The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2.
# Notice that no colon is used at the end of the for statement.
# Note: the variable: value in expression: value**2 and in for loop: for value.... is same 


# Copying a list

my_foods = ['burger', 'pizza', 'fries']
friends_foods = my_foods[:] # lists are copied using the slice notation without slice notation they're one list

my_foods.append('ice cream')
friends_foods.append('soda')

print(my_foods)
print(friends_foods)
# output down below
# ['burger', 'pizza', 'fries', 'ice cream']
# ['burger', 'pizza', 'fries', 'soda']

# Example if we not use the slice notation
my_foods = ['burger', 'pizza', 'fries']
friends_foods = my_foods # lists are copied using the slice notation without slice notation they're one list

my_foods.append('ice cream')
friends_foods.append('soda')

print(my_foods)
print(friends_foods)
# output down below
# ['burger', 'pizza', 'fries', 'ice cream', 'soda']
# ['burger', 'pizza', 'fries', 'ice cream', 'soda']

#Creating Empty List
el = []
el_2 = list() #any of the 2 method can be used to make an empty list




# Corey Schafer

#Lists

courses = ['History', 'Maths', 'Physics', 'CompSci']

print(len(courses)) #prints the length of the list
print(courses[3]) #using the index value to access the values of the list (-1 will give us the last item)
print(courses[0:2]) #accessing range of a values first num is inclusive and second number is exclusive (first number blank means we have to start from the beginning and second number blank mean we want to go till the end)

courses.append('Art') #adding value to the list (this will always add value to the last)
courses.insert(1, 'Geography') #unlike append, insert is use to add the value to a specific location in the list

courses_2 = ['DSA', 'Algorithm']
courses.insert(1, courses_2) #this method will add an another list in the orignal list
#output for the above line --> ['History', ['DSA', 'Algorithm'], 'Geography', 'Maths', 'Physics', 'CompSci', 'Art']
print(courses)

courses.extend(courses_2) #will add the values of the courses_2 to the courses
print(courses)

#removing elements to the list
courses.remove('Maths') #removes the given value from the list
print(courses)

popped = courses.pop() # defaultly removes the last value from the list and also let us use it with the help of a variable
print(popped) #display the popped value
print(courses)

courses.reverse() #reverses the arrangement of the list
print(courses) 

alphabet = ['A', 'C', 'E', 'D', 'B']
num = [1, 3, 4, 2, 7, 5, 6]
alphabet.sort() #sorts words alphabatically
num.sort() #sorts number in ascending order
print(alphabet)
print(num)

#to write the above results in descending order

alphabet.sort(reverse=True) #sorts words in descending Alphabatical order
num.sort(reverse=True) #sorts number in descending order
print(alphabet)
print(num)

#What if we wanted the sorted version of our sorted list without altering the orignal list
#we use sorted function in this case
#orignal courses list
courses = ['History', 'Maths', 'Physics', 'CompSci']

sorted_courses = sorted(courses) #creates a new sorted list without altering the orignal list
print(courses)
print(sorted_courses)

num = [1, 3, 4, 2, 7, 5, 6]
print(min(num)) #prints the minimum value from the list
print(max(num)) #prints the maximum value from the list
print(sum(num)) #prints the sum of the numbers of the list

print(courses.index('Maths')) #prints the index value of the given subject from the list
#above line shows error if the thing is not in the list

print('Art' in courses) #checks if the given thing is present in the list or not

#Looping Values
#accessing value in the list
for course in courses:
	print(course)


#accessing courses along with their index
#here start=1 tells the loop that index counting should start from 1
for index, course in enumerate(courses, start=1):
	print(index, course)

#Join the values of string
course_str = ' - '.join(courses)
print(course_str)

#now joining the given data into the string
new_list = course_str.split(' - ')
print(new_list)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List Comprehensions Example

# Example 1
# Normal method
# I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
# 	my_list.append(n)
# print( my_list)

# Comprehension method
# my_list = [n for n in nums]
# print(my_list)


# Example 2
# Normal Method
# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
# 	my_list.append(n*n)
# print(my_list)

# Comprehension Method
# my_list = [n*n for n in nums]
# print(my_list)


# Example 3
# Normal Method
# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
# 	if n%2 == 0:
# 		my_list.append(n)
# print(my_list)

# Comprehension Method
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# Normal Method
# my_list = []
# for letter in 'abcd':
# 	for num in range(4):
# 		my_list.append((letter, num))
# print(my_list)

#Comprehension Method
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

