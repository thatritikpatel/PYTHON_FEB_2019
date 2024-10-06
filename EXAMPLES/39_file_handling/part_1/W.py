f1=open('a.jpg','rb')
f2=open('b.jpg','wb')

x=f1.read()
f2.write(x)

f1.close()
f2.close()