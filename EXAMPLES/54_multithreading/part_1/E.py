from threading import current_thread,Thread

def job():
	print('in job()',current_thread().getName())

t=Thread(target=job)
t.start()


print('in main thread ',current_thread().getName())