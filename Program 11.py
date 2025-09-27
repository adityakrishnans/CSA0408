import threading
import time

# Function to simulate a task
def task(name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"Thread {name} is running iteration {i+1}")

if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=task, args=("A", 1))
    t2 = threading.Thread(target=task, args=("B", 1.5))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print("\nAll threads have finished execution.")
