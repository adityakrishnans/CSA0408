def sjf_scheduling(processes, burst_times):
    n = len(processes)

    # Sort processes by burst time (Shortest Job First)
    sorted_processes = sorted(zip(processes, burst_times), key=lambda x: x[1])

    # Initialize waiting and turnaround times
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Waiting time calculation
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + sorted_processes[i - 1][1]

    # Turnaround time = burst time + waiting time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + sorted_processes[i][1]

    # Average times
    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    # Display results
    print("\n--- Shortest Job First (SJF) Scheduling ---")
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        p, bt = sorted_processes[i]
        print(f"{p}\t{bt}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


# Example usage
if __name__ == "__main__":
    # Define processes and burst times
    processes = ["P1", "P2", "P3", "P4"]
    burst_times = [6, 8, 7, 3]   # Example burst times

    sjf_scheduling(processes, burst_times)
