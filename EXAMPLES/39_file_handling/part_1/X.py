import csv

with open('bb.csv','a',newline='') as f:
	w=csv.writer(f)
	w.writerow(['Name','Deg','Sem','College'])
	n=int(input('How many students?: '))
	for x in range(n):
		nm=input('Enter your name: ')
		dg=input('Enter your degree: ')
		sm=input('Enter Semester: ')
		cl=input('Enter your college: ')
		w.writerow([nm,dg,sm,cl])
		print()
