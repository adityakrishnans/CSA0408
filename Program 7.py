def non_preemptive_sjf(processes, arrival_time, burst_time):
    n = len(processes)
    completed = 0
    t = 0
    is_completed = [False] * n

    waiting_time = [0] * n
    turnaround_time = [0] * n

    while completed != n:
        # Select process with shortest burst time among ready processes
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if arrival_time[i] <= t and not is_completed[i]:
                if burst_time[i] < min_burst:
                    min_burst = burst_time[i]
                    idx = i
                elif burst_time[i] == min_burst:
                    # If tie, choose process with earlier arrival
                    if arrival_time[i] < arrival_time[idx]:
                        idx = i

        if idx != -1:
            # Process starts at current time
            start_time = t
            t += burst_time[idx]
            finish_time = t

            turnaround_time[idx] = finish_time - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            is_completed[idx] = True
            completed += 1
        else:
            t += 1  # No process is ready, increment time

    # Display results
    print("\n--- Non-Preemptive SJF Scheduling ---")
    print("Process\tArrival\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")


# Example usage
if __name__ == "__main__":
    processes = ["P1", "P2", "P3", "P4"]
    arrival_time = [0, 1, 2, 3]
    burst_time = [6, 8, 7, 3]

    non_preemptive_sjf(processes, arrival_time, burst_time)
