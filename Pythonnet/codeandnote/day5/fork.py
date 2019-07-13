import os 
from time import sleep 

print("************************")
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(2)
    print("a = ",a)
    a = 10000
    print("The new process")
else:
    sleep(3)
    print("The old process")
    print("a:",a)
print("Fork test over",a)
