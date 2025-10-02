class IndexedFile:
    def __init__(self, filename):
        self.filename = filename
        self.index_block = {}   # Maps block number → record
        self.next_block = 0     # Keeps track of available block

    def add_record(self, record):
        """Add record at the next available block"""
        self.index_block[self.next_block] = record
        print(f"Record '{record}' stored at block {self.next_block}")
        self.next_block += 1

    def read_record(self, block_number):
        """Access record directly using block number (random access)"""
        if block_number in self.index_block:
            print(f"Block {block_number} → Record: {self.index_block[block_number]}")
        else:
            print(f"Block {block_number} is empty or invalid!")

    def display_index_block(self):
        """Display the index block (file pointer table)"""
        print(f"\nIndex Block for File '{self.filename}':")
        if not self.index_block:
            print("No records stored yet.")
            return
        for block, record in self.index_block.items():
            print(f"Index[{block}] → {record}")


if __name__ == "__main__":
    file = IndexedFile("MyFile")

    while True:
        print("\n--- Indexed File Allocation Menu ---")
        print("1. Add Record")
        print("2. Read Record by Block Number")
        print("3. Display Index Block")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            data = input("Enter record data: ")
            file.add_record(data)
        elif choice == "2":
            block = int(input("Enter block number to read: "))
            file.read_record(block)
        elif choice == "3":
            file.display_index_block()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Enter 1-4.")
