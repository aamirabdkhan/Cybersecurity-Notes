from abc import ABC, abstractmethod

class Vehicle(ABC):

 	@abstractmethod
 	def go(self):
 		pass

 	@abstractmethod
 	def stop(self):
 		pass

class Car(Vehicle):

	def go(self):
 		print("You drive the Car")

	def stop(self):
 		print("You stop the car")

class Motorcycle(Vehicle):

	def go(self):
 		print("You ride the Motorcycle")

	def stop(self):
 		print("You stop the Motorcycle")

class Boat(Vehicle):

	def go(self):
 		print("You sail the boat")

	def stop(self):
 		print("You anchor the boat")

car = Car()
motorcycle = Motorcycle()
boat = Boat()

car.stop()
motorcycle.go()
boat.go()
boat.stop()