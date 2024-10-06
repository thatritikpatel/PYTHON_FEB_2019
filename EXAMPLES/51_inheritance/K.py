class D:
	pass

class A(D):
	pass

class B(D):
	pass

class C:
	pass

class E(A,B,C):
	pass

print(E.mro())