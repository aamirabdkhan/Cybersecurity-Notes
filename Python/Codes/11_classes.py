class Car:

	# Constructor Method (also known as init method)
	def __init__(self, model, year, color, for_sale):
		# Instance Variables these are defined inside the methods
		self.model = model
		self.year = year
		self.color = color
		self.for_sale = for_sale

	# Methods
	def drive(self):
		print(f"You are driving a {self.color} {self.Model}")

	def stop(self):
		print(f"You stop the {self.color} {self.Model}")

	def describe(self):
		print(f"{self.year} {self.color} {self.model}")


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2023, "blue", True)
car3 = Car("Charger", 2022, "yellow", True)