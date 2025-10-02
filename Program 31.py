from collections import deque

def fifo_page_replacement(pages, capacity):
    memory = deque()       # Queue to hold pages in memory
    page_faults = 0

    print(f"\nPages: {pages}")
    print(f"Frame Capacity: {capacity}\n")

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                removed = memory.popleft()   # Remove oldest page
                print(f"Page {removed} removed")
            memory.append(page)
            print(f"Page {page} inserted -> Memory: {list(memory)} (Fault)")
        else:
            print(f"Page {page} already in memory -> Memory: {list(memory)} (Hit)")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example input
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3
    fifo_page_replacement(pages, capacity)
