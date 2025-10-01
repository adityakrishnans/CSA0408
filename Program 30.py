import threading
import time
import sys

# (i) Create Thread
def create_demo():
    def worker():
        print(f"[{threading.current_thread().name}] is running...")
        time.sleep(1)
        print(f"[{threading.current_thread().name}] finished.")

    t = threading.Thread(target=worker, name="CreatedThread")
    t.start()
    t.join()   # ensure clean exit

# (ii) Join Thread
def join_demo():
    def task():
        print("Task started...")
        time.sleep(2)
        print("Task completed.")

    t = threading.Thread(target=task)
    t.start()
    print("Main thread waiting for child (join)...")
    t.join()
    print("Main thread continues after join.")

# (iii) Equal Threads
def equal_demo():
    def dummy():
        time.sleep(1)

    t1 = threading.Thread(target=dummy, name="T1")
    t1.start()
    main_thread = threading.current_thread()

    print(f"Main thread id: {main_thread.ident}")
    print(f"T1 thread id: {t1.ident}")

    if t1.ident == main_thread.ident:
        print("T1 and Main thread are equal")
    else:
        print("T1 and Main thread are different")

    t1.join()

# (iv) Exit Thread
def exit_demo():
    def worker():
        print("Thread starting work...")
        time.sleep(1)
        print("Thread exiting now...")
        sys.exit()  # Equivalent to pthread_exit

    t = threading.Thread(target=worker)
    t.start()
    t.join()
    print("Main thread finished after child exit.")

# Menu-driven interface
if __name__ == "__main__":
    while True:
        print("\n--- Thread Operations Menu ---")
        print("1. Create Thread")
        print("2. Join Thread")
        print("3. Equal Threads")
        print("4. Exit Thread")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            create_demo()
        elif choice == "2":
            join_demo()
        elif choice == "3":
            equal_demo()
        elif choice == "4":
            exit_demo()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
