def first_fit(block_size, process_size):
    n, m = len(block_size), len(process_size)
    allocation = [-1] * m  # Stores block assigned to each process

    for i in range(m):  # For each process
        for j in range(n):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break

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

    print("First Fit Memory Allocation Simulation")
    first_fit(block_size, process_size)

