def aaa(func):
	def xyz():
		x=func()
		return x*2
	return xyz

def bbb(func):
	def pqr():
		y=func()
		return y*y
	return pqr

@bbb
@aaa
def mno():
	print('hello')
	return 2

print(mno())