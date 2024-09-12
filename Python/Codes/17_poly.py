# Polymorphism

from abc import ABC, abstractmethod

class Shape(ABC):

	@abstractmethod
	def area(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14 * self.radius ** 2


class Square(Shape):
	def __init__(self, side):
		self.side = side

	def area(self):
		return self.side ** 2

class Rectangle(Shape):
	def __init__(self, height, base):
		self.height = height
		self.base = base

	def area(self):
		return self.height * self.base

class Pizza(Circle):
	def __init__(self, toppings, radius):
		super().__init__(radius)
		self.toppings = toppings


shapes = [Circle(5), Square(5), Rectangle(5, 6), Pizza("Cheese", 5)]

for shape in shapes:
	print(f'{shape.area()}sqcm')