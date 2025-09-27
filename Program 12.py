import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Create a lock for each fork
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

def philosopher(phil_id):
    left_fork = forks[phil_id]
    right_fork = forks[(phil_id + 1) % NUM_PHILOSOPHERS]

    for _ in range(3):  # Eat 3 times
        print(f"Philosopher {phil_id} is thinking.")
        time.sleep(random.uniform(0.5, 2))  # Thinking

        # To prevent deadlock, the last philosopher picks up right fork first
        if phil_id == NUM_PHILOSOPHERS - 1:
            first_fork, second_fork = right_fork, left_fork
        else:
            first_fork, second_fork = left_fork, right_fork

        with first_fork:
            print(f"Philosopher {phil_id} picked up first fork.")
            time.sleep(0.1)
            with second_fork:
                print(f"Philosopher {phil_id} picked up second fork and starts eating.")
                time.sleep(random.uniform(0.5, 1.5))  # Eating
                print(f"Philosopher {phil_id} finished eating and put down forks.")

if __name__ == "__main__":
    threads = []

    # Create philosopher threads
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\nAll philosophers have finished eating.")
