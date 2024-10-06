def rows(n):
	if n!=0:
		rows(n-1)
		for i in range(n):
			print('* ',end='')
		print()
		
		

rows(3)