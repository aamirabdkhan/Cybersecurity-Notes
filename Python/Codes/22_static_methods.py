# Static Method

class Employee:

	def __init__(self, name, position):
		self.name = name
		self.position = position

	def get_info(self):
		return f"{self.name} = {self.position}"

	@staticmethod
	def is_valid_position(position):
		valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
		return position in valid_position


employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Spongebob", "Cook")
employee3 = Employee("Squiward", "Cashier")

print(Employee.is_valid_position("Cashier"))
print(Employee.is_valid_position("Scientist"))


print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())