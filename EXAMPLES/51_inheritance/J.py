class E:
	pass

class B(E):
	pass

class A:
	pass

class C(B,A):
	pass

print(C.mro())
