import csv

with open('bb.csv','r') as f:
	r=csv.reader(f)
	#print(list(r))	
	l=list(r)
	#print(l)
	for row in l:
		for col in row:
			print(col,'\t',end='')
		print()
	