def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print(f"\nPages: {pages}")
    print(f"Frame Capacity: {capacity}\n")

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                removed = memory.pop(0)   # Remove least recently used
                print(f"Page {removed} removed")
            memory.append(page)
            print(f"Page {page} inserted -> Memory: {memory} (Fault)")
        else:
            # Page hit → move page to end (most recently used)
            memory.remove(page)
            memory.append(page)
            print(f"Page {page} already in memory -> Memory: {memory} (Hit)")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example input
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3
    lru_page_replacement(pages, capacity)
