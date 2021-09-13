


import time
import random
from process import MProcess
from utility import *

high_queue = []
medium_queue = []
low_queue = []
def partition_queue():
    #priority = 1--------system
    #priority = 2--------interactive
    #priority = 3--------batch
    for p in ready_queue:
        if p.priority == 1:
            high_queue.append(p)
        elif p.priority == 2:
            medium_queue.append(p)
        else:
            low_queue.append(p)

def order_partition():
    partition_queue()
    system_queue(high_queue)
    interactive_queue(medium_queue)
    batch_queue(low_queue)



def main():
    order_partition()
    #this is the time tracking for how long the medium/interactive queue waiting time
    medium_waiting = 15

    #this is the time tracking for how long the low/batch queue waiting time
    low_waiting = 25 
    
    process_start_time = time.localtime().tm_sec

    while high_queue:
        time_start = time.localtime().tm_sec
        cur = medium_queue[0]
        burst_time = time_start + cur.burst_time
        interupt_signal = False
        while time.localtime().tm_sec < burst_time:
            time.sleep(0.999)
            if (time.localtime().tm_sec - process_start_time)% medium_waiting == 0:
                high_queue.append(medium_queue.pop(0))
            
            if random.randint(5,10) == 7:
                print("from high queue")
                print(f"Process: {high_queue[0].process_id} interupted\n")
                high_queue[0].burst_time = time.localtime().tm_sec - time_start
                medium_queue.append(high_queue.pop(0))

        if not interupt_signal and high_queue:
            print("from high queue")
            print(f"Process: {high_queue[0].process_id}  Burst time:{high_queue[0].burst_time}   arrived_at:{high_queue[0].arrival_time}   priority:{high_queue[0].priority} finished executing.\n")
            high_queue.pop(0)
 

    while medium_queue:
        quantum = 3
        time_start = time.localtime().tm_sec
        cur = medium_queue[0]
        burst_time = time_start + cur.burst_time
        interupt_signal = False
        while time.localtime().tm_sec < burst_time:
            
            if time.localtime().tm_sec > (time_start + quantum):
                interupt_signal = True
                print(f"Process: {medium_queue[0].process_id}  Burst_time:{medium_queue[0].burst_time} interupted")
                medium_queue[0].burst_time = burst_time - time.localtime().tm_sec
                print(f"Burst_time_left: {medium_queue[0].burst_time}\n")
                medium_queue.append(medium_queue.pop(0))
                
                break

            if (time.localtime().tm_sec - process_start_time)% low_waiting == 0:
                medium_queue.append(low_queue.pop(0))
            time.sleep(0.999)
        if not interupt_signal:
            print("from medium queue")
            print(f"Process: {medium_queue[0].process_id}  Burst time:{medium_queue[0].burst_time}   arrived_at:{medium_queue[0].arrival_time} priority:{medium_queue[0].priority} finished executing.\n")
            medium_queue.pop(0)


    while low_queue:
        time_start = time.localtime().tm_sec
        cur = low_queue[0]
        burst_time = time_start + cur.burst_time
        while time.localtime().tm_sec < burst_time:
            time.sleep(0.999)
            pass
        print("from low queue")  
        print(f"Process: {low_queue[0].process_id}  Burst time:{low_queue[0].burst_time}   arrived_at:{low_queue[0].arrival_time}  priority:{low_queue[0].priority} finished executing.\n")
        low_queue.pop(0)



ready_queue = [MProcess(1,1,2,1),MProcess(2,0,3,1),MProcess(3,1,8,2),MProcess(4,3,6,3),MProcess(5,0,2,2),MProcess(6,0,1,3)]

main()

