from people import Faculty,Student
faculty = []
students = []
choice = 0
while (True):
	print ("1.) Add Faculty")
	print ("2.) Print Faculty")
	print ("3.) Add Student")
	print ("4.) Print Student")
	print ("5.) Exit the program")
	choice = int(input("Please choose from the above choices"))
	if choice == 1:
		firstname = input("Enter first name:")
		lastname = input("Enter last name:")
		department = input("Enter department:")
		faculty.append(Faculty(firstname, lastname, department))
	elif choice == 2:
		print ("Contact List \n First Name          Last name        Department")
		for peoples in faculty:
			print (peoples.firstname,"                " ,peoples.lastname, "          "  ,peoples.department)
	elif choice == 3:
		firstname = input("Enter first name:")
		lastname = input("Enter last name:")
		classyear = input("Enter class year:")
		major = input("Enter major:")
		s = Student(firstname, lastname)
		s.set_major(major)
		s.set_class(classyear)
		students.append(s)
	elif choice == 4:
		print ("Contact List \n  First Name          Last Name        Class Year          Major")
		for student in students:
			print (student.firstname, "             ", student.lastname, "           ", student.classyear, "         ", student.major)
	elif choice == 5:
		break
