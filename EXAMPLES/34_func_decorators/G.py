def aaa(func):
	def xyz():
		print('-----1')
		func()
	return xyz

def bbb(func):
	def pqr():
		print('-----2')
		func()
	return pqr

@bbb
@aaa
def mno():
	print('inside original func')

mno()