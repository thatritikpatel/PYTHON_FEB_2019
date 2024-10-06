from threading import *

def job():
	x=current_thread()
	print('thread name:',x.name,'is daemon:',x.isDaemon())


t=Thread(target=job,name='abc')
t.start()


x=current_thread()
print('thread name:',x.name,'is daemon:',x.isDaemon())