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



SJF(Non-preemptive):-
def sjf_non_preemptive(processes):
    n = len(processes)

    processes_sorted = sorted(processes, key=lambda x: (x[1], x[2]))

    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [0] * n

    completed = [False] * n
    current_time = 0
    completed_count = 0

    execution_order = []

    while completed_count < n:

         shortest_idx = -1
         shortest_burst = float('inf')

         for i in range(n):
             if (not completed[i] and 
                 processes_sorted[i][1] <= current_time and 
                 processes_sorted[i][2] < shortest_burst):
                 shortest_burst = processes_sorted[i][2]
                 shortest_idx = I

         if shortest_idx == -1:
              current_time += 1
              continue

          if response_time[shortest_idx] == 0:
               response_time[shortest_idx] = current_time - processes_sorted[shortest_idx][1]

          current_time += processes_sorted[shortest_idx][2]
          completion_time[shortest_idx] = current_time

          execution_order.append(processes_sorted[shortest_idx][0])

          completed[shortest_idx] = True
          completed_count += 1

          arrival = processes_sorted[shortest_idx][1]
          burst = processes_sorted[shortest_idx][2]
          turnaround_time[shortest_idx] = completion_time[shortest_idx] - arrival
          waiting_time[shortest_idx] = turnaround_time[shortest_idx] - burst

   avg_waiting = sum(waiting_time) / n
   avg_turnaround = sum(turnaround_time) / n
   return {
        'completion_time': completion_time,
        'waiting_time': waiting_time,
        'turnaround_time': turnaround_time,
        'response_time': response_time,
        'avg_waiting': avg_waiting,
        'avg_turnaround': avg_turnaround,
        'execution_order': execution_order,
        'processes_sorted': processes_sorted
}

def print_table(processes, result):
 
       sorted_processes = result['processes_sorted']
       n = len(processes)

       print("\n" + "="*90)
       print("NON-PREEMPTIVE SJF SCHEDULING RESULTS")
       print("="*90)

       print("\n| Process | Arrival | Burst | Completion | Turnaround | Waiting | Response |")
       print("|---------|---------|-------|------------|------------|---------|----------|")

       for i, (pid, arr, burst) in enumerate(sorted_processes):
             comp = result['completion_time'][i]
             tat = result['turnaround_time'][i]
             wait = result['waiting_time'][i]
             resp = result['response_time'][i]
             print(f"| {pid:^7} | {arr:^7} | {burst:^5} | {comp:^10} | {tat:^10} | {wait:^7} | {resp:^8} |")

       print("\n" + "="*90)

       print(f"Average Turnaround Time: {result['avg_turnaround']:.1f}")
       print(f"Average Waiting Time: {result['avg_waiting']:.1f}")
       print("="*90)

      print(f"\nExecution Order: {' → '.join(result['execution_order'])}")

      print("\nGantt Chart:")
      print("-"*70)

      current = 0
      gantt_chart = []
      for i, pid in enumerate(result['execution_order']):

            for idx, (p, arr, burst) in enumerate(sorted_processes):
                  if p == pid:
                      start = current
                      end = result['completion_time'][idx]
                      gantt_chart.append((pid, start, end))
                      current = end
                      break

       print("\n", end="")
       for pid, start, end in gantt_chart:
           duration = end - start
           print(f"| {pid:<{duration*2}} ", end="")
        print("|")

        print("0", end="")
        for _, start, end in gantt_chart:
            print(f"{' ' * (len(str(end)) + (end-start)*2 - 1)}{end}", end="")
        print("\n")


processes = [
('P1', 3, 3),
('P2', 2, 1),
('P3', 5, 2),
('P4', 0, 3),
('P5', 1, 2)
]

result = sjf_non_preemptive(processes)
print_table(processes, result)

print("\n" + "="*90)
print("TABLE IN ORIGINAL PROCESS ORDER (P1, P2, P3, P4, P5)")
print("="*90)

sorted_processes = result['processes_sorted']
print("\n| Process | Arrival | Burst | Completion | Turnaround | Waiting | Response |")
print("|---------|---------|-------|------------|------------|---------|----------|")

for pid in ['P1', 'P2', 'P3', 'P4', 'P5']:

      for i, (p, arr, burst) in enumerate(sorted_processes):
               if p == pid:
                   comp = result['completion_time'][i]
                   tat = result['turnaround_time'][i]
                   wait = result['waiting_time'][i]
                   resp = result['response_time'][i]
                   print(f"| {pid:^7} | {arr:^7} | {burst:^5} | {comp:^10} | {tat:^10} | {wait:^7} | {resp:^8} |")
                   break
print("\n" + "="*90)
print(f"Average Turnaround Time: {result['avg_turnaround']:.1f}")
print(f"Average Waiting Time: {result['avg_waiting']:.1f}")
print("="*90)
