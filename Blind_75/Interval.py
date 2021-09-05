# easy chunk
# 1. Meeting Rooms
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda x: x[0])
        
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prev[1]:
                return False
            prev = curr
        
        return True

# medium chunk
# 1. Merge Intervals
class Solution:
	'''
    in first `if` we modify interval already
    in the list, whilst in the second we `.append()`
    it and now prev becomes curr => for the next iteration
    if first `if` works => it'll be modified in-place
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        result = [ prev]
        
        for curr in intervals:
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                prev = curr
                result.append(prev)

        return result

# 2. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        # as `intervals` already sorted, we can
        # make a couple of edge checks
        for idx in range(len(intervals)):
            if intervals[idx][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[idx:]
            
            elif intervals[idx][1] < newInterval[0]:
                result.append(intervals[idx])
            
            else:
            # elif intervals[idx][1] >= newInterval[0] and\
            #   intervals[idx][0] <= newInterval[1]:
                
                newInterval = [min(newInterval[0], intervals[idx][0]),
                              max(newInterval[1], intervals[idx][1])]
        
        # as we break out of `for` only in case
        # we didn't enter first check => append
        # newInterval
        result.append(newInterval)
        return result

# 3. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0][1]
        
        count = 0
        for idx in range(1, len(intervals)):
            curr = intervals[idx]
            if curr[0] < prev:
                count += 1
                prev = min(prev, curr[1])
            else:
            # elif curr[0] >= prev:
                prev = curr[1]
        
        return count

# 4. Meeting Rooms 2
class Solution:
    # 1. heap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Sort by first value to access earliest, but
        sort in Heap based on last value, i.e. the smallest
        last will be the first as it does end earlier
        '''
        if len(intervals) <= 1:
            return 1
        
        intervals.sort(key=lambda x: x[0])
        minHeap = Heap([intervals[0]])
        count = 1

        for idx in range(1, len(intervals)):
            curr = intervals[idx]
            
            if minHeap.peek()[1] > curr[0]:
                count += 1
            else:
                minHeap.remove()
                
            minHeap.insert(curr)
        
        return count

        
class Heap:
    def __init__(self, arr):
        self.heap = self.buildHeap(arr)

    def buildHeap(self, arr):
        parentIdx = (len(arr) - 2) // 2
        for i in reversed(range(parentIdx + 1)):
            self.siftDown(i, len(arr) - 1, arr)
        return arr
    
    def siftDown(self, idx, length, heap):
        idxOne = idx * 2 + 1
        while idxOne <= length:
            idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
            if idxTwo != -1 and heap[idxTwo][1] < heap[idxOne][1]:
                swap = idxTwo
            else:
                swap = idxOne
            
            if heap[swap][1] < heap[idx][1]:
                self.swap_values(swap, idx)
                idx = swap
                idxOne = idx * 2 + 1
            else:
                return
                
    def swap_values(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def siftUp(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parentIdx = (idx - 1) // 2
            if self.heap[parentIdx][1] > self.heap[idx][1]:
                self.swap_values(idx, parentIdx)
                idx = parentIdx
            else:
                return
        
    def remove(self):
        drop = self.heap[0]
        temp = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = temp
            self.siftDown(0, len(self.heap) - 1, self.heap)
        return drop
    
    def peek(self):
        return self.heap[0]
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp()

        # 2. array
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            if len(intervals) <= 1:
                return 1
            start = sorted(x[0] for x in intervals)
            end = sorted(x[1] for x in intervals)
            
            s = 0
            e = 0
            count = 0
            
            while s < len(intervals):
                if start[s] >= end[e]:
                    count -= 1
                    e += 1
                count += 1
                s += 1
            
            return count
