class D:
	def aaa(self,*n):
		sum=0
		for i in n:
			sum = sum + i
		return sum

x=D()

#print(x.aaa())
#print(x.aaa(10))
#print(x.aaa(10,20))
#print(x.aaa(10,20,30))
#print(x.aaa(10,20,30,40))
print(x.aaa(10,20,30,40,50))
		