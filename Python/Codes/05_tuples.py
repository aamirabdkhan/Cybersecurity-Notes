# Note:  Tuples are technically defined by the presence of a comma; the paranthesis make them look neater and more readable.
# 		 If you want to define a tuple with one element you need to include a trailing comma.
my_tuple = (3, )
# It doesn't often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.


# wrting over a Tuple

dimensions = (200, 50)
# dimension[0] = 400  #We can't modify a tuple
print(dimensions)
dimensions = (400, 100) #here we redefined the whole the tuple
	print(dimensions) 























# Corey Scahfer


#tuples
#tuples are immutable which means once created they can't be changed

tuple = ('History', 'Maths', 'Physics', 'CompSci')
#WE can perform almost all the methods we applied to Lists but we can't use the methods where the values in the tuple will be mutated
# which means in tuples we can't add, append, remove, push, pop and perfrom similar mutable methods



#Creating Empty Tuple
et = ()
et_2 = Tuple() #any of the 2 method can be used to make an empty tuple