class MProcess:
    process_id = None
    arrival_time = None 
    burst_time = None
    priority = None

    def __init__(self,process_id,arrival_time, burst_time,priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
