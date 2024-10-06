def rows(n):
	if n!=0:
		for i in range(n):
			print('* ',end='')
		print()
		rows(n-1)
		

rows(4)