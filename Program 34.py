class SequentialFile:
    def __init__(self):
        self.records = []  # Simulate file storage

    def add_record(self, record):
        """Add a record at the end (sequentially)"""
        self.records.append(record)
        print(f"Record '{record}' added.")

    def read_record(self, position):
        """Read record at given position (1-based index)"""
        if position < 1 or position > len(self.records):
            print("Invalid position!")
            return
        print(f"Accessing record at position {position}:")
        for i in range(position):
            print(f"Record {i+1}: {self.records[i]}")

    def display_all(self):
        """Display all records"""
        print("\nAll records in file:")
        for i, record in enumerate(self.records, start=1):
            print(f"Record {i}: {record}")


if __name__ == "__main__":
    file = SequentialFile()

    while True:
        print("\n--- Sequential File Allocation Menu ---")
        print("1. Add Record")
        print("2. Read Record")
        print("3. Display All Records")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            data = input("Enter record data: ")
            file.add_record(data)
        elif choice == "2":
            pos = int(input("Enter record position to read: "))
            file.read_record(pos)
        elif choice == "3":
            file.display_all()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Enter 1-4.")
