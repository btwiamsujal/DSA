class TaskManager:
    def __init__(self, tasks):
        self.taskPri = {}  # Maps taskId to its priority
        self.taskUser = {}  # Maps taskId to its userId
        self.pq = []  # A priority queue implemented with heapq
        
        for task in tasks:
            userId, taskId, priority = task
            self.taskUser[taskId] = userId
            self.taskPri[taskId] = priority
            # Push the task into the priority queue
            heapq.heappush(self.pq, (-priority, -taskId))  # Use negative to simulate max-heap
        
    def add(self, userId, taskId, priority):
        self.taskUser[taskId] = userId
        self.taskPri[taskId] = priority
        heapq.heappush(self.pq, (-priority, -taskId))  # Insert into the heap with negated values for max-heap behavior
    
    def edit(self, taskId, newPriority):
        self.taskPri[taskId] = newPriority
        heapq.heappush(self.pq, (-newPriority, -taskId))  # Insert the updated task with new priority
    
    def rmv(self, taskId):
        if taskId in self.taskUser:
            del self.taskUser[taskId]
            del self.taskPri[taskId]
    
    def execTop(self):
        while self.pq:
            priority, taskId = heapq.heappop(self.pq)
            taskId = -taskId  # Convert back to positive taskId
            if self.taskPri.get(taskId, -1) == -priority:  # Check if the task is still valid
                userId = self.taskUser[taskId]
                # Remove task from taskUser and taskPri after executing it
                del self.taskUser[taskId]
                del self.taskPri[taskId]
                return userId
        return -1  # If no valid task exists