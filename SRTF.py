def srtf_scheduling(processes):
 
    n = len(processes)
    
    pid = [p[0] for p in processes]
    arrival = [p[1] for p in processes]
    burst = [p[2] for p in processes]
    
    remaining = burst.copy()
    completion = [0] * n
    turnaround = [0] * n
    waiting = [0] * n
    response = [0] * n
    start_time = [-1] * n
    is_completed = [False] * n
    
    current_time = 0
    completed = 0
    gantt_chart = []
    previous_pid = None
    
    while completed < n:
        shortest_idx = -1
        min_remaining = float('inf')
        
        for i in range(n):
            if (arrival[i] <= current_time and 
                not is_completed[i] and 
                remaining[i] < min_remaining):
                min_remaining = remaining[i]
                shortest_idx = i
        
        if shortest_idx == -1:
            if previous_pid != "IDLE":
                gantt_chart.append(("IDLE", current_time, current_time + 1))
                previous_pid = "IDLE"
            current_time += 1
            continue
        
        if start_time[shortest_idx] == -1:
            start_time[shortest_idx] = current_time
        
        current_time += 1
        remaining[shortest_idx] -= 1
        
        if previous_pid != pid[shortest_idx]:
            gantt_chart.append((pid[shortest_idx], current_time - 1, current_time))
        else:
            gantt_chart[-1] = (pid[shortest_idx], gantt_chart[-1][1], current_time)
        
        previous_pid = pid[shortest_idx]
        
        if remaining[shortest_idx] == 0:
            is_completed[shortest_idx] = True
            completion[shortest_idx] = current_time
            turnaround[shortest_idx] = completion[shortest_idx] - arrival[shortest_idx]
            waiting[shortest_idx] = turnaround[shortest_idx] - burst[shortest_idx]
            completed += 1
    
    for i in range(n):
        response[i] = start_time[i] - arrival[i]
    
    avg_turnaround = sum(turnaround) / n
    avg_waiting = sum(waiting) / n
    avg_response = sum(response) / n
    
    return {
        'pid': pid,
        'arrival': arrival,
        'burst': burst,
        'completion': completion,
        'turnaround': turnaround,
        'waiting': waiting,
        'response': response,
        'gantt_chart': gantt_chart,
        'avg_turnaround': avg_turnaround,
        'avg_waiting': avg_waiting,
        'avg_response': avg_response,
        'total_time': current_time
    }

def display_results(result):
    """Display SRTF scheduling results - Clean version"""
    
    print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting\tResponse")
    
    for i in range(len(result['pid'])):
        print(f"{result['pid'][i]}\t\t{result['arrival'][i]}\t\t"
              f"{result['burst'][i]}\t\t{result['completion'][i]}\t\t\t"
              f"{result['turnaround'][i]}\t\t\t{result['waiting'][i]}\t\t"
              f"{result['response'][i]}")
    
    
    print(f"\nAverage Turnaround Time:{result['avg_turnaround']}")
    print(f"Average Waiting Time:{result['avg_waiting']}")

processes = [
    ('P1', 3, 3),
    ('P2', 2, 1),
    ('P3', 5, 2),
    ('P4', 0, 3),
    ('P5', 1, 2)
]
    
result = srtf_scheduling(processes)
display_results(result)