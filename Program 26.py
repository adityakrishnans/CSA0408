import os

def create_file(filename):
    with open(filename, "w") as f:
        print(f"File '{filename}' created successfully.")

def write_file(filename, data):
    with open(filename, "w") as f:  # overwrite mode
        f.write(data)
        print(f"Data written to '{filename}'.")

def append_file(filename, data):
    with open(filename, "a") as f:  # append mode
        f.write("\n" + data)
        print(f"Data appended to '{filename}'.")

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print(f"\nContents of '{filename}':")
            print(f.read())
    else:
        print(f"File '{filename}' not found!")

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"File '{old_name}' not found!")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' not found!")

if __name__ == "__main__":
    while True:
        print("\n--- File Management Menu ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Append File")
        print("4. Read File")
        print("5. Rename File")
        print("6. Delete File")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            filename = input("Enter file name: ")
            create_file(filename)
        elif choice == "2":
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")
            write_file(filename, data)
        elif choice == "3":
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            append_file(filename, data)
        elif choice == "4":
            filename = input("Enter file name: ")
            read_file(filename)
        elif choice == "5":
            old = input("Enter current file name: ")
            new = input("Enter new file name: ")
            rename_file(old, new)
        elif choice == "6":
            filename = input("Enter file name: ")
            delete_file(filename)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Enter 1-7.")
