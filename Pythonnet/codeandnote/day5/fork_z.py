import os 
from time import sleep

pid = os.fork()

if pid == 0:
    print("Child process:",os.getpid())
    os._exit(0)
else:
    print("Parent process,长点心吧..")
    while True:
        pass 

