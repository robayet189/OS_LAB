def fcfs_disk_scheduling(requests, head):
    total_seek = 0
    current_head = head

    print("Seek Sequence:", end=" ")
    print(current_head, end=" ")

    for request in requests:
        seek = abs(request - current_head)
        total_seek += seek
        current_head = request

        print("->", request, end=" ")

    print()
    print("Total Head Movement:", total_seek)
    print("Average Head Movement:", total_seek / len(requests))
    
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53

fcfs_disk_scheduling(requests, head)