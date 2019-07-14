import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0 :
    sleep(1)
    print("Child PID:",os.getpid())
    print("Get parent pid:",os.getppid())
else:
    print("Parent PID:",os.getpid())
    print("Get child PID:",pid)