class J:
	__a=71

class X(J):	
	def aaa():
		#print(X.__a)
		print(J.__a)


X.aaa()