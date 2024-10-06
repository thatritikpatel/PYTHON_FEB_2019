import emp,pickle

with open('dt.txt','wb') as f:
	n=int(input('How many students?: '))
	for i in range(n):
		nm=input('Enter your name: ')
		cl=input('Enter your college: ')
		dg=input('Enter your degree: ')
		sm=input('Enter your semester: ')
		st=emp.Student(nm,cl,dg,sm)
		pickle.dump(st,f)
		print()