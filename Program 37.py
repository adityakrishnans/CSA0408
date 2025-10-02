def fcfs_disk_scheduling(requests, head):
    print(f"\nInitial Head Position: {head}")
    print(f"Requests: {requests}\n")

    total_head_movement = 0
    sequence = [head]

    for req in requests:
        movement = abs(req - head)
        total_head_movement += movement
        print(f"Move from {head} → {req} (Seek: {movement})")
        head = req
        sequence.append(req)

    print(f"\nSeek Sequence: {sequence}")
    print(f"Total Head Movement: {total_head_movement}")
    print(f"Average Seek Time: {total_head_movement/len(requests):.2f}")


if __name__ == "__main__":
    # Example input
    requests = [82, 170, 43, 140, 24, 16, 190]
    head = 50
    fcfs_disk_scheduling(requests, head)
