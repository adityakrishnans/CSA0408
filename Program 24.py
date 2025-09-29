import os

def create_file(filename):
    with open(filename, "w") as f:
        print(f"File '{filename}' created successfully.")

def write_file(filename, data):
    with open(filename, "a") as f:  # Append mode
        f.write(data + "\n")
        print(f"Data written to '{filename}'.")

def read_file(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return
    with open(filename, "r") as f:
        print(f"\nContents of '{filename}':")
        print(f.read())

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"File '{old_name}' does not exist.")

if __name__ == "__main__":
    while True:
        print("\n--- File Management Simulation ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Delete File")
        print("5. Rename File")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            filename = input("Enter file name to create: ")
            create_file(filename)
        elif choice == "2":
            filename = input("Enter file name to write: ")
            data = input("Enter data to write: ")
            write_file(filename, data)
        elif choice == "3":
            filename = input("Enter file name to read: ")
            read_file(filename)
        elif choice == "4":
            filename = input("Enter file name to delete: ")
            delete_file(filename)
        elif choice == "5":
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1-6.")
