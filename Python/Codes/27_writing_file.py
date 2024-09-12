# Writing to a File

filename = 'write.txt'

with open(filename, 'w') as f:
	f.write("I love programming.\n")
	f.write("I love creating new game.\n")


# Appending to a File
with open(filename, 'a') as f:
	f.write("I love playing football.\n")
	f.write("I love watching movies.\n")



# Arguments

# read mode ('r')
# write mode ('w')
# append mode ('a')