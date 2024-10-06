class Student:
	def __init__(self,a,b,c,d):
		self.name=a
		self.college=b
		self.degree=c
		self.semester=d
	
	def show(self):
		print(self.name,'\t',self.college,'\t',self.degree,'\t',self.semester)
