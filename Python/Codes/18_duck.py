# Duck Typing

class Animal:
	alive = True

class Dog(Animal):
	def speak(self):
		print("WOOF!")

class Cat(Animal):
	def speak(self):
		print("MEOW!")

class Car:
	alive = False
	def speak(self):
		print("HONK!")

animals = [Dog(), Cat(), Car()]
for animal in animals:
	animal.speak()
	print(animal.alive)


# All though in the above example the Car is not no Inheriting from the Animal class but it has all the requries attributes and methods to become similar to Animal class 
