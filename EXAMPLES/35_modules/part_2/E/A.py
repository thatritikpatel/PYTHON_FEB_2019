def f1():
	if __name__=='__main__':
		print('A.py called directly')
		print('__name__:',__name__)
	else:
		print('A.py called from outside')
		print('__name__:',__name__)

f1()