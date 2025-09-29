import threading, time, random

BUFFER_SIZE = 5
buffer = []

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Counts empty slots
full = threading.Semaphore(0)             # Counts filled slots
mutex = threading.Semaphore(1)            # Binary semaphore for mutual exclusion

def producer():
    for i in range(10):
        item = random.randint(1, 100)
        empty.acquire()        # Wait for empty slot
        mutex.acquire()        # Lock buffer
        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")
        mutex.release()        # Unlock buffer
        full.release()         # Signal item available
        time.sleep(random.uniform(0.5, 1.5))

def consumer():
    for i in range(10):
        full.acquire()         # Wait for available item
        mutex.acquire()        # Lock buffer
        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")
        mutex.release()        # Unlock buffer
        empty.release()        # Signal empty slot
        time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    # Create threads
    p = threading.Thread(target=producer)
    c = threading.Thread(target=consumer)

    # Start threads
    p.start()
    c.start()

    # Wait for completion
    p.join()
    c.join()

    print("\nAll items have been produced and consumed.")

