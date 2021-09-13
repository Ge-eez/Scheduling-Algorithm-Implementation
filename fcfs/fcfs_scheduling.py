



from fcfs_process import MProcess
import time

ready_queue = [MProcess(1,2,3),MProcess(2,5,2),MProcess(3,6,1),MProcess(4,0,0),MProcess(5,4,1)]

def main():  
    sq = sort_queue(ready_queue)
    for i in range(len(sq)):
        p = sq[i]
        start_time = time.localtime().tm_sec
        cpu_time = p.burst_time
        
        while time.localtime().tm_sec < (start_time + cpu_time):
            pass
        print(f'Process Id: {p.process_id}  Arrival Time: {p.arrival_time}  Burst Time: {p.burst_time}');

        if(i < len(sq)-1):
            interval_time = sq[i+1].arrival_time - p.arrival_time
            if(interval_time > p.burst_time):
                start_time = time.localtime().tm_sec
                while time.localtime().tm_sec < (start_time + (interval_time - p.burst_time)):
                    pass

def sort_queue(q):

    for i in range(len(q)):
        cur = q[i]
        j = i
        while j > 0 and q[j-1].arrival_time > cur.arrival_time:
            q[j] = q[j-1]
            j -= 1
        q[j] = cur
    return q

main()

