class TwoLevelDirectory:
    def __init__(self):
        # Dictionary: key = user/subdirectory, value = list of files
        self.directory = {}

    def create_user(self, user):
        if user in self.directory:
            print(f"User directory '{user}' already exists.")
        else:
            self.directory[user] = []
            print(f"User directory '{user}' created successfully.")

    def create_file(self, user, filename):
        if user not in self.directory:
            print(f"User directory '{user}' does not exist.")
        else:
            if filename in self.directory[user]:
                print(f"File '{filename}' already exists in '{user}' directory.")
            else:
                self.directory[user].append(filename)
                print(f"File '{filename}' created in '{user}' directory.")

    def delete_file(self, user, filename):
        if user not in self.directory:
            print(f"User directory '{user}' does not exist.")
        elif filename not in self.directory[user]:
            print(f"File '{filename}' not found in '{user}' directory.")
        else:
            self.directory[user].remove(filename)
            print(f"File '{filename}' deleted from '{user}' directory.")

    def search_file(self, user, filename):
        if user not in self.directory:
            print(f"User directory '{user}' does not exist.")
        elif filename in self.directory[user]:
            print(f"File '{filename}' found in '{user}' directory.")
        else:
            print(f"File '{filename}' not found in '{user}' directory.")

    def display_files(self, user):
        if user not in self.directory:
            print(f"User directory '{user}' does not exist.")
        elif not self.directory[user]:
            print(f"No files in '{user}' directory.")
        else:
            print(f"Files in '{user}' directory:")
            for file in self.directory[user]:
                print(f"- {file}")


# Main Program
if __name__ == "__main__":
    dir_system = TwoLevelDirectory()

    while True:
        print("\n--- Two-Level Directory Operations ---")
        print("1. Create User Directory")
        print("2. Create File")
        print("3. Delete File")
        print("4. Search File")
        print("5. Display Files")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            user = input("Enter user name to create directory: ")
            dir_system.create_user(user)
        elif choice == "2":
            user = input("Enter user name: ")
            filename = input("Enter file name to create: ")
            dir_system.create_file(user, filename)
        elif choice == "3":
            user = input("Enter user name: ")
            filename = input("Enter file name to delete: ")
            dir_system.delete_file(user, filename)
        elif choice == "4":
            user = input("Enter user name: ")
            filename = input("Enter file name to search: ")
            dir_system.search_file(user, filename)
        elif choice == "5":
            user = input("Enter user name to display files: ")
            dir_system.display_files(user)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1-6.")
