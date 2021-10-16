# 1. Top K Frequent Elements
class Solution:
    # pq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 0
            
            ht[num] += 1
        
        return heapq.nlargest(k, ht.keys(), key=ht.get)

    # bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # +1 as we need to include cases: [1].
        # And out idx is actually from 1 to len() of num
        result = [[] for i in range(len(nums) + 1)]

        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 0
            ht[num] += 1

        for key, value in ht.items():
            result[value].append(key)

        output = []
        for i in reversed(range(len(result))):
            for num in result[i]:
                output.append(num)
                if len(output) == k:
                    return output


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 0

            ht[num] += 1

        pq = PriorityQueue()
        for key, value in ht.items():
            pq.insert(key, value)

        return pq.get_elements(k)

# Hard chunk

# 2. Merge k Sorted Lists
from Queue import PriorityQueue

class Solution:
    # less optimal
    def mergeKLists(self, array: List[ListNode]) -> ListNode:

        result = []
        idx_arr = []
        lists = []
        
        for l in array:
            
            curr = l
            temp = []
            while curr:
                temp.append(curr.val)
                curr = curr.next
            
            if temp:
                lists.append(temp)
        
        for idx in range(len(lists)):
            idx_arr.append({
                'idx': idx,
                'ele_idx': 0,
                'num': lists[idx][0]
        })
        
        if not lists:
            return None
        
        min_heap = MinHeap(idx_arr)
        
        while not min_heap.check():
            ele = min_heap.remove()
            idx, element_idx, number = ele['idx'], ele['ele_idx'], ele['num']
            result.append(number)
            
            if element_idx == len(lists[idx]) - 1:
                continue
            
            min_heap.insert({
                'idx': idx,
                'ele_idx': element_idx + 1,
                'num': lists[idx][element_idx+1]})
            
        node = ListNode(result[0])
        head = node
        
        for idx in range(1, len(result)):
            num = result[idx]
            curr = ListNode(num)
            
            node.next = curr       
            node = curr
        
        return head
    

class MinHeap:
	def __init__(self, arr):
		self.heap = self.buildHeap(arr)
	
	def buildHeap(self, arr):
		parentIdx = (len(arr) - 1) // 2
		for i in reversed(range(parentIdx + 1)):
			self.siftDown(i, len(arr) - 1, arr)
		return arr
	
	def check(self):
		return len(self.heap) == 0
	
	def siftDown(self, idx, length, heap):
		idxOne = idx * 2 + 1
		while idxOne <= length:
			idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
			if idxTwo != -1 and heap[idxTwo]['num'] < heap[idxOne]['num']:
				swap = idxTwo
			else:
				swap = idxOne
			if heap[swap]['num'] < heap[idx]['num']:
				self.swapFunc(swap, idx, heap)
				idx = swap
				idxOne = idx * 2 + 1
			else:
				return
	
	def remove(self):
		drop = self.heap[0]
		value = self.heap.pop()
		if len(self.heap) > 0:
			self.heap[0] = value
			self.siftDown(0, len(self.heap) - 1, self.heap)
		return drop
	
	def peek(self):
		return self.heap[0]
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp()
	
	def siftUp(self):
		idx = len(self.heap) - 1
		while idx > 0:
			parentIdx = (idx - 1) // 2
			if self.heap[parentIdx]['num'] > self.heap[idx]['num']:
				self.swapFunc(idx, parentIdx, self.heap)
				idx = parentIdx
			else:
				return
	
	def swapFunc(self, i, j, arr):
		arr[i], arr[j] = arr[j], arr[i]

    # more optimal
    def mergeKLists(self, array: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        pq = PriorityQueue()
        
        for ele in array:
            if ele: # to bypass None
                pq.put((ele.val, ele))
                # we put value and list itself
        
        while not pq.empty():
            value, node = pq.get()
            
            # convert value to node and
            # switch to next overall
            # which we're building
            point.next = ListNode(value)
            point = point.next
            
            node = node.next
            if node:
                pq.put((node.val, node))
        
        return head.next
 
# Divide & Conquer
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            
            interval *= 2
    
        return lists[0] if amount > 0 else None

    def merge(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        
        if not l1:
            point.next = l2
        else:
            point.next = l1
        
        return head.next

# 3. Find Median from Data Stream
class MedianFinder:

    '''
1. .lower will hold values from lowest to middle
    and .upper - from middle to largest
    => when we calc. median: log n of largest
        from first chunk and log n of smallest
        from second chunk

2. Pay attention that we add .length attr. to Heap as
    it will be used quite often

3. After every number insertion we update median
    => when .findMedian() is called => everything
    is up to date

4. in .peek() don't forget to check:
    if self.length == 0
'''
    def __init__(self):
        self.median = None
        self.lower = Heap([], max_heap)
        self.upper = Heap([], min_heap)
        

    def addNum(self, num: int) -> None:
        if not self.lower.peek() or num < self.lower.peek():
            self.lower.insert(num)
        else:
            self.upper.insert(num)
        
        self.rebalance()
        self.update_median()
        
    def rebalance(self):
        if self.lower.length - self.upper.length == 2:
            self.upper.insert(self.lower.remove())
        
        elif self.upper.length - self.lower.length == 2:
            self.lower.insert(self.upper.remove())
    
    def update_median(self):
        if self.lower.length > self.upper.length:
            self.median = self.lower.peek()
        elif self.lower.length < self.upper.length:
            self.median = self.upper.peek()
        else:
            self.median = (self.lower.peek() + self.upper.peek()) / 2
    
    def findMedian(self) -> float:
        return self.median

        
class Heap:
    def __init__(self, arr, func):
        self.heap = self.buildHeap(arr)
        self.compare = func
        self.length = len(self.heap)
        
    def buildHeap(self, arr):
        parentIdx = (len(arr) - 1) // 2
        for idx in reversed(range(parentIdx + 1)):
            self.siftDown(idx, len(arr) - 1, arr)
        
        return arr
    
    def peek(self):
        if self.length == 0:
            return None
        
        return self.heap[0]
    
    def siftDown(self, idx, length, arr):
        idxOne = idx * 2 + 1
        while idxOne <= length:
            idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
            
            if idxTwo != -1 and self.compare(arr[idxTwo], arr[idxOne]):
                swap = idxTwo
            else:
                swap = idxOne
            
            if self.compare(arr[swap], arr[idx]):
                self.swap(swap, idx)
                idx = swap
                idxOne = idx * 2 + 1
            
            else:
                return
    
    def siftUp(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parentIdx = (idx - 1) // 2
            if self.compare(self.heap[idx], self.heap[parentIdx]):
                self.swap(idx, parentIdx)
                idx = parentIdx
            else:
                return
    
    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
    
    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp()
    
    def remove(self):
        drop_node = self.heap[0]
        temp = self.heap.pop()
        if self.length > 0:
            self.heap[0] = temp
            self.length -= 1
            self.siftDown(0, self.length - 1, self.heap)
        
        return drop_node
        

def max_heap(num1, num2):
    return num1 > num2

def min_heap(num1, num2):
    return num1 < num2
