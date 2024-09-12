x, y, z = 0, 1, 3 # Multiple Assignments
print(x, y, z)

# we can use underscores to make large numbers more readable
universe_age = 14_000_000_000
print(universe_age) # python will ignore the underscores between a number






















# Corey Schafer

num_int = 3
num_float = 3.14
# python automatially detects the datatype of the variable
print(type(num_float), type(num_int))

#Python performs the Arithmatic operations directly
#Addition: 3 + 2
#subtration: 3 - 2
#Multiply: 3 * 2
#Division: 3 / 2 --> this give us the exat answer i.e (1.5) in this case
#Floor Division: 3//2 --> this will give us by dropping to the nearest lower integer
#Exponent: 3 ** 2 --> this is how to use power
#Modulus: 3 % 2

#BODMAS works correctly in python

num = 1
num += 1 # is actually num = num + 1 and it can be used with other operators as well

print(abs(-3)) # gives absolute value of the given number
print(round(3.14)) #rounds up to nearest integer value
print(round(3.14, 1)) # rounds upto 1 decimal

#Comparisons

#Assignment:   num = 2
#Equal: 3 == 2
#Not Equal: 3 != 2
#Greater Than: 3 > 2
#less than: 3 < 2
# Greater or Equal: 3 >= 2
#less or equal: 3 <= 2

#Converting strings to integers --> this converting method is known as casting
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)