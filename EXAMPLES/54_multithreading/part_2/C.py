from threading import *

def job():
	x=current_thread()
	print('thread name:',x.name,'is daemon:',x.isDaemon())


t=Thread(target=job,name='abc')

#Case 1:
t.setDaemon(True)

t.start()

#Case 2:
#t.setDaemon(True)


x=current_thread()
print('thread name:',x.name,'is daemon:',x.isDaemon())