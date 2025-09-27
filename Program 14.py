# Single-Level Directory Simulation
class SingleLevelDirectory:
    def __init__(self):
        self.files = []  # List to store file names

    def create_file(self, filename):
        if filename in self.files:
            print(f"File '{filename}' already exists.")
        else:
            self.files.append(filename)
            print(f"File '{filename}' created successfully.")

    def delete_file(self, filename):
        if filename in self.files:
            self.files.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' not found.")

    def search_file(self, filename):
        if filename in self.files:
            print(f"File '{filename}' found.")
        else:
            print(f"File '{filename}' not found.")

    def display_files(self):
        if not self.files:
            print("Directory is empty.")
        else:
            print("Files in directory:")
            for file in self.files:
                print(f"- {file}")


# Main Program
if __name__ == "__main__":
    directory = SingleLevelDirectory()

    while True:
        print("\n--- Single-Level Directory Operations ---")
        print("1. Create File")
        print("2. Delete File")
        print("3. Search File")
        print("4. Display All Files")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            filename = input("Enter file name to create: ")
            directory.create_file(filename)
        elif choice == "2":
            filename = input("Enter file name to delete: ")
            directory.delete_file(filename)
        elif choice == "3":
            filename = input("Enter file name to search: ")
            directory.search_file(filename)
        elif choice == "4":
            directory.display_files()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
