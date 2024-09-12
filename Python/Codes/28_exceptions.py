# Exceptions

# try and except block
# Exceptions are used to prevent crashes
# try:
# 	print(5/0)
# except:
# 	print("You can't divide by zero!")

# print("Give me 2 number, and I'll divide them.")
# print("Enter q to quit")

# while True:

# 	first_number = input("\nfirst number:")
# 	if first_number == 'q':
# 		break
# 	second_number = input("\nsecond number:")
# 	if second_number == 'q':
# 		break

# 	try:
# 		answer = int(first_number) / int(second_number)
# 	except ZeroDivisionError:
# 		print("You can't divide by 0")
# 	else:
# 		print(answer) # When try block doesn't have any error it jumps to else block
# Handling the fileNotFoundError:
# filename = 'alice.txt'

# try:
# 	with open(filename, encoding='utf-8') as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	print(f"Sorry, the file {filename} does not exist")
# else:
# 	# Count the approximate number of words in the file
# 	words = contents.split()
# 	num_words = len(words)
# 	print(f"The file {filename} has about {num_words} words.")



# Working with Multiple Files

def count_words(filename):
	try:
	 	with open(filename, encoding='utf-8') as f:
	 		contents = f.read()
	except FileNotFoundError:
	 	print(f"Sorry, the file {filename} does not exist")
	else:
	 	# Count the approximate number of words in the file
	 	words = contents.split()
	 	num_words = len(words)
	 	print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)
filename = 'alices.txt'
count_words(filename)


# Failing silently --> we can not give user any info related to the error by writing pass. When an error occurs and except block contains pass it just pass through the error without notifying any thing