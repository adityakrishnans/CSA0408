def is_safe(n, m, alloc, max_need, avail):
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq, work = [], avail[:]

    while len(safe_seq) < n:
        progress = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + alloc[i][j] for j in range(m)]
                finish[i], progress = True, True
                safe_seq.append(i)
        if not progress:  # No process can proceed → unsafe
            return False, []
    return True, safe_seq


if __name__ == "__main__":
    n, m = 5, 3  # processes, resources
    alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    avail = [3, 3, 2]

    safe, seq = is_safe(n, m, alloc, max_need, avail)
    if safe:
        print("System is in a SAFE state.")
        print("Safe Sequence:", " -> ".join(f"P{i}" for i in seq))
    else:
        print("System is in an UNSAFE state (Deadlock may occur).")


