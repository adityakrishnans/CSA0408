def best_fit(block_size, process_size):
    n, m = len(block_size), len(process_size)
    allocation = [-1] * m   # Stores block assigned to each process

    for i in range(m):  # For each process
        best_index = -1
        for j in range(n):  # Find the smallest suitable block
            if block_size[j] >= process_size[i]:
                if best_index == -1 or block_size[j] < block_size[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[i]

    # Display allocation
    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(m):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{process_size[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{process_size[i]}\t\tNot Allocated")

if __name__ == "__main__":
    # Example input
    block_size = [100, 500, 200, 300, 600]  # Memory blocks
    process_size = [212, 417, 112, 426]     # Processes

    print("Best Fit Memory Allocation Simulation")
    best_fit(block_size, process_size)

