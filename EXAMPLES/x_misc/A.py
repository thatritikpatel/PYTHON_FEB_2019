import sys

class A:
	pass

a1=A()

a2=a1
a3=a1
a4=a1

print(sys.getrefcount(a1))