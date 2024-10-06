class circle:
	pi=3.14

	def __init__(self,r):
		self.r=r
	
	def calcA(self):
		#print(pi*r*r)
		print(circle.pi * self.r * self.r)
 

c1=circle(20)
c2=circle(30)

c1.calcA()
c2.calcA()