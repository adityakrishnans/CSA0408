def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print(f"\nPages: {pages}")
    print(f"Frame Capacity: {capacity}\n")

    for i in range(len(pages)):
        page = pages[i]
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
                print(f"Page {page} inserted -> Memory: {memory} (Fault)")
            else:
                # Find the page that will not be used for the longest time
                future_uses = []
                for mem_page in memory:
                    if mem_page in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(mem_page))
                    else:
                        future_uses.append(float('inf'))  # Not used again

                index_to_replace = future_uses.index(max(future_uses))
                removed = memory[index_to_replace]
                memory[index_to_replace] = page
                print(f"Page {removed} removed, Page {page} inserted -> Memory: {memory} (Fault)")
        else:
            print(f"Page {page} already in memory -> Memory: {memory} (Hit)")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example input
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3
    optimal_page_replacement(pages, capacity)
