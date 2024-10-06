import pickle

class Student:
	def __init__(self,a,b,c,d):
		self.name=a
		self.college=b
		self.degree=c
		self.semester=d
	
	def show(self):
		print(self.name,'\t',self.college,'\t',self.degree,'\t',self.semester)

with open('tty.txt','wb') as f:
	x=Student('gotam','jec','be','7th')
	pickle.dump(x,f)

with open('tty.txt','rb') as g:
	y=pickle.load(g)
	y.show()
