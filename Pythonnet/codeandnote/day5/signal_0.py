import os 
import signal

# 处理子进程信号
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    pass
elif pid == 0:
    print("Child PID:",os.getpid())
else:
    while True:
        pass 
