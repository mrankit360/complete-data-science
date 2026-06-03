import threading
import time

def print_number():
    for num in numbers:
        print(num)

numbers = [1,2,3,4,5]

def letters():
    for letter in 'abcde':
        print(letter)

t=time.time()
# t1=threading.Thread(target=print_number)
# t2=threading.Thread(target=letters)

# ## start the thread
# t1.start()
# t2.start()

# ## wait for thread to complete
# t1.join()
# t2.join()

# print(f'finished time: {(time.time()-t)}')

## threading with thread pool executor
 
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(lambda f:f(), [print_number,letters])