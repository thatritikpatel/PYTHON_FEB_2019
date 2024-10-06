#Keyword Arg
def showInfo(name,age,address,phone):
	print('My name is:',name,'and age is:',age,'Address:',address,'Phone:',phone)

#showInfo('mohan',21,'Jabalpur','98787897897')

#showInfo('Jabalpur',21,'98787897897','mohan')

showInfo(age=21,phone='98787897897',address='Jabalpur',name='mohan')