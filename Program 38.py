def scan_disk_scheduling(requests, head, disk_size, direction="left"):
    print(f"\nInitial Head Position: {head}")
    print(f"Requests: {requests}")
    print(f"Disk Size: {disk_size}, Initial Direction: {direction}\n")

    requests = sorted(requests)   # Sort requests
    total_head_movement = 0
    sequence = []

    if direction == "left":
        left = [r for r in requests if r < head]
        right = [r for r in requests if r >= head]
        left.reverse()  # Move leftwards first

        # First go left
        for r in left:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

        # Go to track 0 (end of disk on left)
        if head != 0:
            total_head_movement += abs(head - 0)
            print(f"Move from {head} → 0 (Seek: {abs(head - 0)})")
            head = 0
            sequence.append(0)

        # Then go right
        for r in right:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

    else:  # direction == "right"
        left = [r for r in requests if r < head]
        right = [r for r in requests if r >= head]

        # First go right
        for r in right:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

        # Go to disk end
        if head != disk_size - 1:
            total_head_movement += abs(head - (disk_size - 1))
            print(f"Move from {head} → {disk_size-1} (Seek: {abs(head - (disk_size-1))})")
            head = disk_size - 1
            sequence.append(head)

        # Then go left
        left.reverse()
        for r in left:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

    print(f"\nSeek Sequence: {sequence}")
    print(f"Total Head Movement: {total_head_movement}")
    print(f"Average Seek Time: {total_head_movement/len(requests):.2f}")


if __name__ == "__main__":
    # Example input
    requests = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 50
    disk_size = 200
    direction = "left"   # or "right"

    scan_disk_scheduling(requests, head, disk_size, direction)
