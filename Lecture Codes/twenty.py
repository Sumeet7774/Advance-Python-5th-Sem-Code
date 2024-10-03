from time import sleep
from threading import Thread
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end, result, index):
    total = 0
    for number in range(start, end):
        if is_prime(number):
            total += number
    result[index] = total  

def main():
    start_time = time.time()
    ranges = [(2,2500), (2501,5000), (5001,7500), (7501,10000)]
    result = [0] * 4
    threads = []
    
for i,(start,end) in enumerate ranges:
    thread = Thread(target=sum_of_primes, args=(start, end, result, i))
    threads.append(thread)
    thread.start()

    thread.join()
    totalsum=sum(result)
    end_time=time.time()