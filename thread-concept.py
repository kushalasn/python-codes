import _thread
import time
def print_time(thread_name,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print(thread_name,time.ctime(time.time()))
        
try:
    thread.start_new_thread