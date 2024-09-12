# Reading from a File

filename = "read.txt"

with open(filename) as f:
	contents = f.read()

# print(contents)
# print(contents.rstrip()) # When python print a file it leaves an extra space in the end thus we use rstrip() to remove the whitespace after the output

# File Paths --> 2 types --> Absolute and Relative

# Relative file path--> Tells python to look for a given location relative to the directory where the currently running program file is stored.

# Absolute file path --> Tells Python exactly wher the file is on your computer regardless of where the program that's being executed is stored.


# Reading Line by Line

with open(filename) as f:
	for line in f:
		# print(line.rstrip())
		pass

# Retaining access to a file outside it's block
with open(filename) as f:
	lines = f.readlines()

for line in lines:
	# print(line.rstrip()) 
	pass


# Working with a File's content

filename = 'pi_digits.txt'

with open(filename) as f:
	lines = f.readlines()

pi_strings = ''
for line in lines:
	pi_strings += line.strip()

print(pi_strings)
print(len(pi_strings))

# Like the above example we can easily large files


# Is your bday contain in pi
filename = 'pi_digits.txt'

with open(filename) as f:
	lines = f.readlines()

pi_strings = ''
for line in lines:
	pi_strings += line.strip()

birthday = input("Enter your Birtday, in the form mmddyy: ")
if birthday in pi_strings:
	print("Your birthday appears in the first million digit of pi!!!")
else:
	print("Your birthday does not appears in the first million digit of pi!!!")
