class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	
	def __mul__(self,other):
		return self.salary*other.days
	
class Timesheet:
	def __init__(self,name,days):
		self.name=name
		self.days=days

	def __mul__(self,other):
		return self.days*other.salary

e=Employee('mohan',1000)
t=Timesheet('mohan',30)

print(e*t)
print(t*e)
