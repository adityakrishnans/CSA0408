import threading
import time
import random

# Buffer settings
BUFFER_SIZE = 5
buffer = []

# Synchronization primitives
empty = threading.Semaphore(BUFFER_SIZE)  # Count of empty slots
full = threading.Semaphore(0)             # Count of filled slots
mutex = threading.Lock()                  # Mutual exclusion lock

def producer():
    while True:
        item = random.randint(1, 100)  # Produce an item
        empty.acquire()   # Wait for empty slot
        mutex.acquire()   # Enter critical section
        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")
        mutex.release()   # Exit critical section
        full.release()    # Signal item available
        time.sleep(random.uniform(0.5, 2))

def consumer():
    while True:
        full.acquire()    # Wait for available item
        mutex.acquire()   # Enter critical section
        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")
        mutex.release()   # Exit critical section
        empty.release()   # Signal slot free
        time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    # Create producer and consumer threads
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
