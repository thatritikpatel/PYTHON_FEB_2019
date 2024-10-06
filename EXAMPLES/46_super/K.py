class Person:
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password

class Employee(Person):
	def __init__(self,name,email,password,designation,experience,salary):		
		super().__init__(name,email,password)
		self.designation=designation
		self.experience=experience
		self.salary=salary
	
	def showInfo(self):
		print("Name: {}, email: {}, password: {}, desig.: {}, exp.: {}, salary: {}".format(self.name,self.email,self.password,self.designation,self.experience,self.salary))

e=Employee('mohan','m@g.c','1111111','Manager',12,60000)
e.showInfo()
print(e.__dict__)


class Student(Person):
	def __init__(self,name,email,password,degree,branch,semester):		
		super().__init__(name,email,password)
		self.degree=degree
		self.branch=branch
		self.semester=semester

	def showInfo(self):
		print("Name: {}, email: {}, password: {}, degree.: {}, branch: {}, semester: {}".format(self.name,self.email,self.password,self.degree,self.branch,self.semester))

s=Student('ganesh','g@g.c','222222','BTech','CS','1st')
s.showInfo()
print(s.__dict__)







