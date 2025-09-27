def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        for j, block in enumerate(blocks):
            if block >= process:
                allocation[i] = j
                blocks[j] -= process
                break
    return allocation

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        best_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= process
    return allocation

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        worst_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= process
    return allocation

def display_allocation(processes, allocation):
    print("Process No.\tProcess Size\tBlock No.")
    for i, block in enumerate(allocation):
        if block != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{block+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")

if __name__ == "__main__":
    # Memory blocks and process sizes
    memory_blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    print("\n--- First Fit Allocation ---")
    allocation = first_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation)

    print("\n--- Best Fit Allocation ---")
    allocation = best_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation)

    print("\n--- Worst Fit Allocation ---")
    allocation = worst_fit(memory_blocks.copy(), processes)
    display_allocation(processes, allocation)
