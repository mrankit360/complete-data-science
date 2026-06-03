# Running Multiple Process At the same time

'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(2)
        print(f"square: {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(2)
        print(f'cube:{i*i*i}')

if __name__ == "__main__":
    #create 2 process
    p1=multiprocessing.Process(target=square_num)
    p2=multiprocessing.Process(target=cube_num)
    t=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    finished_time=time.time()-t
    print(finished_time)

