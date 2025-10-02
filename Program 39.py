def cscan_disk_scheduling(requests, head, disk_size, direction="right"):
    print(f"\nInitial Head Position: {head}")
    print(f"Requests: {requests}")
    print(f"Disk Size: {disk_size}, Direction: {direction}\n")

    requests = sorted(requests)
    total_head_movement = 0
    sequence = []

    if direction == "right":
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]

        # Move right first
        for r in right:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

        # Go to end of disk
        if head != disk_size - 1:
            total_head_movement += abs(head - (disk_size - 1))
            print(f"Move from {head} → {disk_size-1} (Seek: {abs(head - (disk_size-1))})")
            head = disk_size - 1
            sequence.append(head)

        # Jump to start (0)
        total_head_movement += (disk_size - 1)  # full jump
        print(f"Jump from {disk_size-1} → 0 (Seek: {disk_size-1})")
        head = 0

        # Then move right again for left-side requests
        for r in left:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

    else:  # direction == "left"
        left = [r for r in requests if r <= head]
        right = [r for r in requests if r > head]
        left.reverse()

        # Move left first
        for r in left:
            total_head_movement += abs(head - r)
            print(f"Move from {head} → {r} (Seek: {abs(head - r)})")
            head = r
            sequence.append(r)

        # Go to start of disk
        if head != 0:
            total_head_movement += abs(head - 0)
            print(f"Move from {head} → 0 (Seek: {abs(head - 0)})")
            head = 0
            sequence.append(0)

        # Jump to end (disk_size-1)
        total_head_movement += (disk_size - 1)
        print(f"Jump from 0 → {disk_size-1} (Seek: {disk_size-1})")
        head = disk_size - 1

        # Then move left again for right-side requests
        right.reverse()
        for r in right:
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
    direction = "right"   # or "left"

    cscan_disk_scheduling(requests, head, disk_size, direction)
