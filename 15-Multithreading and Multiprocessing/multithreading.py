import threading
import time

#multi threading is done to increase throughput :- concurrent execution

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter: {letter}")

t = time.time()
#create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

#start the thread
t1.start()
t2.start()
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)