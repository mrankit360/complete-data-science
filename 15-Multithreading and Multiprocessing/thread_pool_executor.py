# it automatically creates a pool of worker threads and assign tasks to them

# MultiThreading Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Numbers: {number}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3)as executor:
    results = executor.map(print_numbers,numbers)

    for result in results:
        print(result)


# Multiprocessing Thread Pool Executor

def square_numbers(number):
    time.sleep(1)
    return f"square: {number*number}"

numbers=[1,2,3,4,5]
if __name__=='__main__':

    with ThreadPoolExecutor(max_workers=3)as executor:
        results = executor.map(square_numbers,numbers)

    for result in results:
        print(result)


# MultiThreading Pool Executor

def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} finished")

# Create a thread pool with 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(task, i)