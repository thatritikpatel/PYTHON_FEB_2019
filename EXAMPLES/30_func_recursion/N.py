def star(n):
	if n!=0:
		print('# ',end='')
		star(n-1)

def rows(n):
	if n!=0:
		rows(n-1)
		star(n)
		print()
		
		
x=int(input('Enter a number: '))
rows(x)