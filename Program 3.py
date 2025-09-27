def fcfs_scheduling(processes, burst_times):
    n = len(processes)

    # Initialize waiting and turnaround times
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Waiting time calculation
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]

    # Turnaround time = burst time + waiting time
    for i in range(n):
        turnaround_time[i] = burst_times[i] + waiting_time[i]

    # Average times
    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    # Display results
    print("\n--- FCFS CPU Scheduling ---")
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


# Example usage
if __name__ == "__main__":
    # Define processes and burst times
    processes = ["P1", "P2", "P3", "P4"]
    burst_times = [5, 8, 12, 6]   # Example burst times

    fcfs_scheduling(processes, burst_times)
