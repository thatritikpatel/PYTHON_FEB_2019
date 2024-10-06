class student:
	college='Global'

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def showInfo():
		pass

x=student('mohan',12)
y=student('vidyut',23)

#Case 3:
print(x.__dict__)
print(y.__dict__)
print(student.__dict__)

#Case 2:
'''
print(x.name)
print(y.name)
print(student.name)
'''

#Case 1:
'''
print(x.college)
print(y.college)
print(student.college)
'''