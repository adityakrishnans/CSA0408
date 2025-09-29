import threading
import time
import random

# Shared resource
shared_data = 0

# Semaphores and counters
mutex = threading.Lock()        # Protects read_count
rw_mutex = threading.Semaphore(1)  # Ensures writer exclusivity
read_count = 0

def reader(rid):
    global read_count, shared_data
    while True:
        time.sleep(random.uniform(0.5, 2))  # Simulate delay

        # Entry section
        mutex.acquire()
        read_count += 1
        if read_count == 1:    # First reader locks writers
            rw_mutex.acquire()
        mutex.release()

        # Critical section (Reading)
        print(f"Reader-{rid} reads value: {shared_data}")

        # Exit section
        mutex.acquire()
        read_count -= 1
        if read_count == 0:    # Last reader unlocks writers
            rw_mutex.release()
        mutex.release()

def writer(wid):
    global shared_data
    while True:
        time.sleep(random.uniform(1, 3))  # Simulate delay

        rw_mutex.acquire()  # Writer gets exclusive access
        shared_data += 1
        print(f"Writer-{wid} writes value: {shared_data}")
        rw_mutex.release()

if __name__ == "__main__":
    # Create multiple readers and writers
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    # Start threads
    for t in readers + writers:
        t.daemon = True  # Allows program to exit if main thread ends
        t.start()

    # Run simulation for 15 seconds
    time.sleep(15)
    print("\nSimulation finished.")
