class circle:
	pi=3.14

	def __init__(self,r):
		self.r=r
	
	def calcA(self):
		#print(pi*r*r)
		print(circle.pi * self.r * self.r)

	def calcP(self):
		print(2 * circle.pi * self.r)
	
	@classmethod
	def showPI(cls):
		print(circle.pi)

	@staticmethod
	def defineCircle():
		print('Circle is a..........,.,....')
 

c1=circle(20)
c2=circle(30)

c1.calcA()
c2.calcA()

c1.calcP()
c2.calcP()

#calcA()
#circle.calcA()
#circle.calcA(1)









