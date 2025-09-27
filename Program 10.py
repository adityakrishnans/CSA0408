from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(5):
        time.sleep(1)
        message = f"Message {i+1}"
        q.put(message)
        print(f"Producer sent: {message}")

def consumer(q):
    for i in range(5):
        message = q.get()  # Blocks until a message is available
        print(f"Consumer received: {message}")
        time.sleep(1.5)

if __name__ == "__main__":
    # Create a message queue
    q = Queue()

    # Create producer and consumer processes
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print("\nAll messages have been processed.")
