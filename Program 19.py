import threading
import time

# Shared resource
shared_counter = 0

# Mutex lock
lock = threading.Lock()

def increment(name):
    global shared_counter
    for i in range(5):
        print(f"{name} trying to access shared resource...")
        lock.acquire()  # Enter critical section
        try:
            print(f"{name} entered critical section.")
            temp = shared_counter
            time.sleep(0.5)  # Simulate work
            shared_counter = temp + 1
            print(f"{name} updated counter to {shared_counter}")
        finally:
            print(f"{name} leaving critical section.\n")
            lock.release()  # Exit critical section
        time.sleep(0.5)

if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=increment, args=("Thread-1",))
    t2 = threading.Thread(target=increment, args=("Thread-2",))

    # Start threads
    t1.start()
    t2.start()

    # Wait for completion
    t1.join()
    t2.join()

    print(f"Final counter value: {shared_counter}")

