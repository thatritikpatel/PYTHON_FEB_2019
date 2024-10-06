class abcd:
	def aaa():
		def bbb():
			print('hello')

		bbb()
		bbb()
		bbb()

abcd.aaa()
abcd.aaa().bbb()  #not ok

#print(abcd.aaa())