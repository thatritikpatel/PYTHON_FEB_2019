class T:
	pass

class D(T):
	pass

class F(T):
	pass

class C(D,F):
	pass

class A(D,F):
	pass

class E(A,C):
	pass

print(E.mro())