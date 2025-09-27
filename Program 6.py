def preemptive_priority_scheduling(processes, arrival_time, burst_time, priority):
    n = len(processes)
    
    # Initialize variables
    remaining_time = burst_time[:]
    complete = 0
    t = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    is_completed = [False] * n

    # While not all processes are completed
    while complete != n:
        # Select process with highest priority among arrived processes
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            if arrival_time[i] <= t and not is_completed[i]:
                if priority[i] < highest_priority:
                    highest_priority = priority[i]
                    idx = i
                elif priority[i] == highest_priority:
                    # If tie → choose process with earlier arrival
                    if arrival_time[i] < arrival_time[idx]:
                        idx = i

        if idx != -1:
            remaining_time[idx] -= 1
            t += 1

            if remaining_time[idx] == 0:
                complete += 1
                finish_time = t
                turnaround_time[idx] = finish_time - arrival_time[idx]
                waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
                is_completed[idx] = True
        else:
            t += 1  # No process is ready yet, increment time

    # Display results
    print("\n--- Preemptive Priority Scheduling ---")
    print("Process\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")


# Example usage
if __name__ == "__main__":
    processes = ["P1", "P2", "P3", "P4"]
    arrival_time = [0, 1, 2, 3]   # Arrival times
    burst_time = [7, 4, 1, 4]     # Burst times
    priority = [2, 1, 3, 2]       # Smaller = higher priority

    preemptive_priority_scheduling(processes, arrival_time, burst_time, priority)



