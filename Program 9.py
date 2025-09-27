from multiprocessing import Process, Value, Lock
import time

def writer(shared_num, lock):
    for i in range(5):
        time.sleep(1)
        with lock:
            shared_num.value += 1
            print(f"Writer updated value to: {shared_num.value}")

def reader(shared_num, lock):
    for i in range(5):
        time.sleep(1.5)
        with lock:
            print(f"Reader reads value: {shared_num.value}")

if __name__ == "__main__":
    # Shared memory integer
    shared_num = Value('i', 0)  # 'i' = integer
    lock = Lock()  # Synchronization lock

    # Create writer and reader processes
    p1 = Process(target=writer, args=(shared_num, lock))
    p2 = Process(target=reader, args=(shared_num, lock))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print(f"\nFinal value in shared memory: {shared_num.value}")
