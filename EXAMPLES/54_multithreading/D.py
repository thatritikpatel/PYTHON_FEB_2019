from threading import *

a=Lock()

x=current_thread()
print(x.name,'is going to acquire the lock')
a.acquire()

print(x.name,'is again going to acquire the lock')
a.acquire()

print(x.name,'is going to release the lock')
a.release()