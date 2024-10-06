class B:
	def aaa():
		print('~~~~~~')

	def aaa(x):
		print('######')

B.aaa(12)
#B.aaa()

print(B.__dict__)


