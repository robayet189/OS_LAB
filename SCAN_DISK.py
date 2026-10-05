def scan(requests, head, disk_size, direction):
    requests = sorted(requests)

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    sequence = []
    current = head
    total = 0

    if direction == "right":
        sequence = right + [disk_size - 1] + left[::-1]

    else:
        sequence = left[::-1] + [0] + right

    for request in sequence:
        total += abs(request - current)
        current = request

    print("Seek Sequence:", head, "->", " -> ".join(map(str, sequence)))
    print("Total Head Movement:", total)
    print("Average Head Movement:", total / len(requests))


requests = [98, 183, 37, 122, 14, 124, 65, 67]

scan(requests, 53, 200, "right")