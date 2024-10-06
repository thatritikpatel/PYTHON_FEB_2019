class Student:
	def __init__(self,a,b,c,d):
		self.name=a
		self.college=b
		self.degree=c
		self.semester=d
	
	def show(self):
		print(self.name,'\t',self.college,'\t',self.degree,'\t',self.semester)

s1=Student('mohan','GGITS','BE','2nd')
s2=Student('sohan','SRIT','BTech','3rd')


######################################
s1.show()
print('~~~~~~~~~~~~~~~~~~')
s2.show()
####################################
'''
print(s1.name)
print(s1.college)
print(s1.degree)
print(s1.semester)
print()
print(s2.name)
print(s2.college)
print(s2.degree)
print(s2.semester)
'''
######################################
'''
l=[s1,s2]

for x in l:
	print(x.name)
	print(x.college)

'''
######################################