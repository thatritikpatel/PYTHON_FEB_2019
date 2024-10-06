from threading import current_thread,Thread

def job():
	for i in range(20):
		print(i,current_thread().getName(),'####')

t=Thread(target=job)
t.setName('mohan')
t.start()


for i in range(20):
	print(i,current_thread().getName(),'~~')