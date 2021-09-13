def system_queue(high_queue):
    for x in range(1,len(high_queue)):
        cur = high_queue[x]
        y = x
        while y > 0 and high_queue[y-1].burst_time < cur.burst_time:                
            high_queue[y] = high_queue[y-1] 
            y -= 1
        y = x
        while y > 0 and high_queue[y-1].burst_time == cur.burst_time and high_queue[y-1].arrival_time > cur.arrival_time:
            high_queue[y] = high_queue[y-1] 
            y -= 1
        high_queue[y] = cur
    return high_queue
   

def interactive_queue(medium_queue):
    for x in range(1,len(medium_queue)):
        cur = medium_queue[x]
        y = x
        while y > 0 and medium_queue[y-1].arrival_time > cur.arrival_time:
            medium_queue[y] = medium_queue[y-1] 
            y -= 1
        medium_queue[y] = cur
    return medium_queue

def batch_queue(low_queue):
    for x in range(1,len(low_queue)):
        cur = low_queue[x]
        y = x
        while y > 0 and low_queue[y-1].arrival_time > cur.arrival_time:
            low_queue[y] = low_queue[y-1] 
            y -= 1
        low_queue[y] = cur

    return low_queue