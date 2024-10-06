class abcd:
	@staticmethod
	def aaa(self):
		print(self)

a=abcd()

abcd.aaa(12)
#a.aaa()  #not ok
a.aaa(23)

