from threading import *

x=current_thread()

print('thread name:',x.name,'is daemon:',x.daemon)