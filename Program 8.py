from collections import deque

def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    remaining_time = burst_time[:]
    t = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = 0
    queue = deque()

    # Track which processes have arrived
    arrived = [False] * n

    while completed < n:
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_time[i] <= t and not arrived[i]:
                queue.append(i)
                arrived[i] = True

        if queue:
            idx = queue.popleft()
            # Execute process for time quantum or remaining time
            exec_time = min(time_quantum, remaining_time[idx])
            t += exec_time
            remaining_time[idx] -= exec_time

            # Add newly arrived processes during execution
            for i in range(n):
                if arrival_time[i] <= t and not arrived[i]:
                    queue.append(i)
                    arrived[i] = True

            # If process still has remaining time, put it back in queue
            if remaining_time[idx] > 0:
                queue.append(idx)
            else:
                completed += 1
                turnaround_time[idx] = t - arrival_time[idx]
                waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        else:
            t += 1  # No process is ready, increment time

    # Display results
    print("\n--- Round Robin Scheduling ---")
    print("Process\tArrival\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")


# Example usage
if __name__ == "__main__":
    processes = ["P1", "P2", "P3", "P4"]
    arrival_time = [0, 1, 2, 3]
    burst_time = [5, 4, 2, 1]
    time_quantum = 2

    round_robin(processes, arrival_time, burst_time, time_quantum)
