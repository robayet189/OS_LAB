def round_robin(processes, time_quantum):

    n = len(processes)

    remaining = [p[2] for p in processes]
    completion = [0] * n
    queue = []

    time = 0
    i = 0
    completed = 0

    while completed < n:

        while i < n and processes[i][1] <= time:
            queue.append(i)
            i += 1

        if not queue:
            time = processes[i][1]
            continue

        x = queue.pop(0)

        run = min(time_quantum, remaining[x])
        time += run
        remaining[x] -= run

        while i < n and processes[i][1] <= time:
            queue.append(i)
            i += 1

        if remaining[x] > 0:
            queue.append(x)
        else:
            completion[x] = time
            completed += 1

    turnaround = [completion[i] - processes[i][1] for i in range(n)]
    waiting = [turnaround[i] - processes[i][2] for i in range(n)]

    print("ROUND ROBIN")
    print("Process\tAT\tBT\tCT\tTAT\tWT")

    for i in range(n):
        print(processes[i][0], "\t",
              processes[i][1], "\t",
              processes[i][2], "\t",
              completion[i], "\t",
              turnaround[i], "\t",
              waiting[i])

    print("\nAverage Waiting Time:", sum(waiting) / n)
    print("Average Turnaround Time:", sum(turnaround) / n)


processes = [
    ('P1', 0, 7),
    ('P2', 1, 4),
    ('P3', 2, 15),
    ('P4', 3, 11),
    ('P5', 4, 20),
    ('P6', 4, 9)
]

time_quantum = 5

round_robin(processes, time_quantum)