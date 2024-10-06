class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary

	
class Timesheet:
	def __init__(self,name,days):
		self.name=name
		self.days=days

e=Employee('mohan',1000)
t=Timesheet('mohan',30)

print(e*t)