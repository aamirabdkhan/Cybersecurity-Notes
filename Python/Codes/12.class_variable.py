

class Student:

	# Class Variable
	pass_year = 2025
	num_students = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Student.num_students += 1


student1 = Student("Jack", 21)
student2 = Student("Daisy", 23)
student3 = Student("Oslo", 19)

print(f"My graduation year is {Student.pass_year} and We are {Student.num_students} students in the class")
