# First Come First Served 
    It is the simplest algorithm of scheduling
    Schedules process based on arrival time
    It execute sequentially

# Multilevek FeedBack Scheduling
    Multi Level Feedback Queue Scheduling algorithm
    The algorith divivide the ready_queue into three sub-queue
    Sub-queue partitioned based on priority given to the process
    Partition Queues are High-Queue(system process),Medium-Queue(interactive process),Low-Queue(batch process)
    High-Queue work with  PRIORITY SCHEDULING(priority based on cpu burst time)
    Medium-Queue works with ROUND ROBIN SCHEDULING(quantum value assign)
    Low-Queue works with FCFSS 
    Higher priority process might be removed from High-Queue and moved to Medium-Queue if interupt occur
    Medium priority process might move up if Medium-Queue head wait for long time
    Lower priority process might move up if Low-Queue head is wait for logn time 

# Comparision 
    FCFS can't handle interrupt or no other process can stop the current executing process, Whereas MLSQ supports interrupt and, also based on priority it schedule execution of process.

    MLSQ is composed of different scheduling might include FCFS, Round Robin and priority scheduling

    MLSQ is more favored because it gives priority to interactive and system process while, the FCFS will execute based on the arrival time this cause interactive process to freeze and makes our interaction with the computer unpleasant .