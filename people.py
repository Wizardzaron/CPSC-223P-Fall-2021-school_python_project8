
class Person:
	def __init__(self_object, first_name, last_name):
		self_object.firstname = first_name
		self_object.lastname = last_name
class Faculty(Person):
	def __init__(self_object, first_name, last_name, department):
		Person.__init__(self_object, first_name, last_name)
		self_object.department = department
class Student(Person):
	def __init__(self_object, first_name, last_name):
		Person.__init__(self_object, first_name, last_name)
	def set_class(self_object, class_year):
		self_object.classyear = class_year
	def set_major(self_object, major):
		self_object.major = major
	def set_advisor(self_object, Faculty):
		self_object.advisor = Faculty
