"прога для работы с процом"
import time
import os

def main():
    print("starting")
    print(f"PID main: {os.getpid()}")
    print(f"PID parent main: {os.getppid()}")
    proc = mp.Process()
    proc.start()
    proc.start(welcome())
    proc.join()
    time.sleep(5)
    welcome()
def welcome():
    print("welcome")
    os.getpid()
    time.sleep(5)
    work()

def work():
    print("working")
    time.sleep(5)
    finish()

def finish():
    print("finished")
    time.sleep(5)

proc_main = mp.Process(main())
proc_start()