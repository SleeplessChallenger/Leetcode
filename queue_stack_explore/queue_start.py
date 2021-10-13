# 1. Design Circular Queue
class MyCircularQueue:
    '''
    Pay attention that `enque()` is without -1
    as we need to get next idx 
    and `Rear()` is with -1
    '''
    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        # .count is curr size
        self.count = 0
        # .capacity is overall length
        self.capacity = len(self.queue) # k
        self.headIdx = 0
    
    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False

        tailIdx = (self.headIdx + self.count) % self.capacity
        self.queue[tailIdx] = value
        self.count += 1
        
        return True

    def deQueue(self) -> bool:
        '''
        `deque` is done from head, not
        from `tail`
        '''
        if self.count == 0:
            return False
        
        self.headIdx = (self.headIdx + 1) % self.capacity
        self.count -= 1
        # change position of head
        
        return True
        
    def Front(self) -> int:
        if self.count == 0:
            return -1
        
        return self.queue[self.headIdx]
        
    def Rear(self) -> int:
        if self.count == 0:
            return -1
        
        return self.queue[self.getTail()]

    def isEmpty(self) -> bool:
        return self.count == 0
    
    def isFull(self) -> bool:
        return self.count == self.capacity
        
    def getTail(self):
        # tailIdx = (headIdx + count - 1) % capacity
        tailIdx = (self.headIdx + self.count - 1) % self.capacity
        return tailIdx

# 2. Moving Average from Data Stream
class MovingAverage:

    def __init__(self, size: int):
        self.window = [0 for _ in range(size)]
        self.count = 0
        self.capacity = len(self.window)
        self.headIdx = 0
        
    def next(self, val: int) -> float:
        if self.count == self.capacity:
            self.deque()
        
        tailIdx = (self.headIdx + self.count) % self.capacity
        self.window[tailIdx] = val
        self.count += 1
        
        return self.get_average()
            
    def deque(self):
        self.headIdx = (self.headIdx + 1) % self.capacity
        self.count -= 1
    
    def get_average(self):
        return sum(self.window) / self.count
