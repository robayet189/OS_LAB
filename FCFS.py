def fcfs(parameters):
    sort=sorted(parameters, key=lambda x: x[1])
    
    n=len(sort)
    completion_time=[0]*n
    turnaroun_time=[0]*n
    waiting_time=[0]*n
    
    current_time=0
    for i,(pid,arrival,burst) in enumerate(sort):
        if current_time<arrival:
            current_time=arrival
        current_time=current_time+burst
        completion_time[i]=current_time
        
        turnaroun_time[i]=completion_time[i]-arrival
        waiting_time[i]=turnaroun_time[i]-burst
    
    return{
        'process_id':sort,
        'completion_time':completion_time,
        'turnaround_time':turnaroun_time,
        'waiting_time':waiting_time
    }
    
parameters=[
    ('p1',3,3),
    ('p2',2,1),
    ('p3',5,2),
    ('p4',0,3),
    ('p5',1,2)
    ]

result=fcfs(parameters)

print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i,(pid,arrival,burst) in enumerate(result['process_id']):
    print(f"{pid}\t{arrival}\t{burst}\t{result['completion_time'][i]}\t{result['turnaround_time'][i]}\t{result['waiting_time'][i]}")
    
avg_turnaround_time=sum(result['turnaround_time'])/len(result['turnaround_time'])
avg_waiting_time=sum(result['waiting_time'])/len(result['waiting_time'])
print(f"Average Turnaround Time:{avg_turnaround_time}")
print(f"Average Waiting Time:{avg_waiting_time}")