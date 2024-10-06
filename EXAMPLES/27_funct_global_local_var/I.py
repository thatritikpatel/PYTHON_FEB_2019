def aaa():
	global a
	a=12
	print(a)

def bbb():
	global a
	a=34
	print(a)

print(globals())
aaa()
print(globals())
bbb()
print(globals())
