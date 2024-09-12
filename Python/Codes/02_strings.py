text = "ada Lovelace"
print(text.title()) #Capitalize the first character of each word

lang = "Python    "
print(lang.rstrip()) #remove white space from the right side
other_lang = "   Java"
print(other_lang.lstrip()) #remove white space from the right side
#strip() is used to remove whitespace from both sides





















# Corey Schafer

message = ("Hello World")

print(len(message)) #printing the length of the message

print(message[4]) #printing the word present at the particular index

#accessing a range of characters from the string
print(message[0:5]) #In this line it access the string from 0th index to 4th index
#first number index in inclusive and second number is exclusive
#leaving the first number blank will start it from the 0th index [:5]
#leaving the second number blank will take the string till the end [6:]

#Methods of Strings - all datatypes have their own methods
print(message.lower()) #write the whole text in lower case
print(message.upper()) #write the whole text in upper case
print(message.count('l')) #will how many times the given word is repeating
print(message.find('World')) #will show at which the given word or character is starting, if it didn't exist it will return -1

#using replace method
new_message = message.replace('World', 'Universe') #in this method we're replacing the word World with the word Universe
#we created a new variable for this method because it doesn't overwrite the orignal string instead it creates a new string by replacing the real word, that's why we're saving the it in a new variable, because old variable will give us the orignal string i.e (Hello World) in this case
print(new_message)

#Combining 2 strings
greetings = 'Hello'
name = 'John'

# msg = greetings + name #this method doesn't add the space between the strings
# msg = greetings + ', ' + name + '. Welcome.' #we have to add things to make it look cool
#putting placeholders instead of the above method (placeholder -> {})
# msg = '{}, {}. Welcome;'.format(greetings, name)

#same thing can happen with using f strings (applicable only for python3.6 and above versions)
msg = f'{greetings}, {name}. Welcome;'
print(msg)

#dir --> list all the methods available for the selected datatype
print(dir(name)) #here the variable contains strings so it will display all the methods available with the strings
#but it doesn't show how to use them

#help --> display how to use the methods but you have to mention the datatype it doesn't accept variable names
print(help(str))
#we can even speccify what method do we wants to kknow about
print(help(str.replace))