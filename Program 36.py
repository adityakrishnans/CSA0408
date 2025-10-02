class Block:
    """Represents a single disk block"""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next block


class LinkedFile:
    def __init__(self, filename):
        self.filename = filename
        self.start = None  # Pointer to first block
        self.end = None    # Pointer to last block

    def add_record(self, record):
        """Append record as a new block in linked list"""
        new_block = Block(record)
        if self.start is None:
            self.start = self.end = new_block
        else:
            self.end.next = new_block
            self.end = new_block
        print(f"Record '{record}' stored in new block.")

    def read_records(self):
        """Read all records sequentially by traversing linked blocks"""
        if self.start is None:
            print("File is empty.")
            return
        print(f"\nReading records from file '{self.filename}':")
        current = self.start
        i = 1
        while current:
            print(f"Block {i} → {current.data}")
            current = current.next
            i += 1

    def display_structure(self):
        """Display the linked allocation structure"""
        if self.start is None:
            print("File is empty.")
            return
        print(f"\nLinked Structure of File '{self.filename}':")
        current = self.start
        while current:
            if current.next:
                print(f"[{current.data}] -> ", end="")
            else:
                print(f"[{current.data}] -> None")
            current = current.next


if __name__ == "__main__":
    file = LinkedFile("MyFile")

    while True:
        print("\n--- Linked File Allocation Menu ---")
        print("1. Add Record")
        print("2. Read All Records")
        print("3. Display File Structure")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            data = input("Enter record data: ")
            file.add_record(data)
        elif choice == "2":
            file.read_records()
        elif choice == "3":
            file.display_structure()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Enter 1-4.")
