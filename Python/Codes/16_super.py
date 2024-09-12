# super Function --> super()

class Shape:

	def __init__(self, color, is_filled):
		self.color = color
		self.is_filled = is_filled

	def describe(self):
		print(f"It is {self.color} and {'Filled' if self.is_filled else 'not Filled'}")

class Circle(Shape):

	def __init__(self, color, is_filled, radius):
		super().__init__(color, is_filled)
		self.radius = radius

	def describe(self):
		print(f"It is a circle with an Area of {3.14 * self.radius * self.radius}cm")
		super().describe()

class Square(Shape):

	def __init__(self, color, is_filled, side):
		super().__init__(color, is_filled)
		self.side = side

	def describe(self):
		print(f"It is a Square with an Area of {self.side * self.side}cm")
		super().describe()

class Rectangle(Shape):

	def __init__(self, color, is_filled, height, width):
		super().__init__(color, is_filled)
		self.height = height
		self.width = width

	def describe(self):
		print(f"It is a circle with an Area of {self.height * self.width}cm")
		super().describe()

cricle = Circle('Red', True, 5)
square = Square("Blue", False, 6)
rectangle = Rectangle("Black", True, 10, 20)

square.describe()
cricle.describe()
rectangle.describe()