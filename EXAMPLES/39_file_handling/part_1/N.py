#exclusive creation mode-'x'
#try when file does not-exists or exists

f=open('mno.txt','x')

f.write('bye')

f.close()