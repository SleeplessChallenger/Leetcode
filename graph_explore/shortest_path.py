# 1. Network Delay Time

# https://leetcode.com/problems/network-delay-time/discuss/1490760/Python-Dijkstra's-with-array-and-self-made-heap

class Solution:
    # 1. First with array
    '''
    As we have from 1 to n:
    1. when creating graph (adjacency list), 
        decrease `source` and `destination`
        nodes by one
    
    2. in minDist when defining start node:
        don't forget to decrease by 1 as well
        
    3. As Dijkstra's algo opts for smallest
        distance at first, if we receive float('inf')
        as min dist => all other nodes are of the same
        scale => no need to proceed (generally it does mean
        we have detached verticies)
    
    '''
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        self.createGraph(times, graph)
        
        minDist = [float('inf') for _ in range(n)]
        minDist[k - 1] = 0
        visited = set()
        
        while len(visited) != n:
            currDist, currVertex = self.explore(visited, minDist)
            
            if currDist == float('inf'):
                break
            
            visited.add(currVertex)
            
            for node in graph[currVertex]:
                vertex, cost = node
                if vertex in visited:
                    continue
                
                newCost = cost + currDist
                
                if newCost < minDist[vertex]:
                    minDist[vertex] = newCost
  
        return -1 if float('inf') in minDist else max(minDist)
            
    def explore(self, visited, minDist):
        smallestDist = float('inf')
        smallestNode = -1
        
        for i in range(len(minDist)):
            if i in visited:
                continue
                
            weight = minDist[i]
            if weight <= smallestDist:
                smallestDist = weight
                smallestNode = i
        
        return smallestDist, smallestNode
    
    def createGraph(self, times, graph):
        for time in times:
            source, dest, cost = time
            graph[source - 1].append((dest - 1, cost))

    # 2. Second with Heap
        def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        1. Why do we need `self.vertex`? => At first idx in heap
            corresponds with idx in `self.vertex`. But !!after even first!!
            update, placed value will chage position in heap, hence we need
            some way to track changes. `self.vertex` will keep initial
            idx which will allow us to get current poisition of element in heap.
        
        2. For this purpose we also need to change `swap` method as when we swap
            values inside heap, we also need to take care of mentioned above `self.vertex`
        
        3. And we also tweak `.remove()` as we need to remove not only value from heap
        (in our case it's a group: value & distance), but also remove key from `self.vertex`
        
        '''
        graph = [[] for _ in range(n)]
        self.createGraph(graph, times)
        
        minDist = [float('inf') for _ in range(n)]
        minDist[k - 1] = 0
        
        min_heap = MinHeap([(idx, float('inf')) for idx in range(n)])
        min_heap.update(k - 1, 0)

        while not min_heap.check():
            
            vertex, cost = min_heap.remove()
            
            if cost == float('inf'):
                break
            
            for i in graph[vertex]:
                node, dist = i
                
                newDist = dist + cost
                if newDist < minDist[node]:
                    minDist[node] = newDist
                    min_heap.update(node, newDist)
        
        return -1 if float('inf') in minDist else max(minDist)
    
    def createGraph(self, graph, times):
        for time in times:
            source, dest, cost = time
            graph[source - 1].append((dest - 1, cost))

    
class MinHeap:
    def __init__(self, arr):
        self.vertex = {idx: idx for idx in range(len(arr))}
        self.heap = self.buildHeap(arr)
    
    def check(self):
        return len(self.heap) == 0
    
    def buildHeap(self, arr):
        parentIdx = (len(arr) - 2) // 2
        for i in reversed(range(parentIdx + 1)):
            self.siftDown(i, len(arr) - 1, arr)
        return arr
    
    def remove(self):
        if self.check():
            return
        
        self.swapValues(0, len(self.heap) - 1, self.heap)
        idx, node = self.heap.pop()
        del self.vertex[idx]
        
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return idx, node
    
    def siftDown(self, idx, length, arr):
        idxOne = idx * 2 + 1
        while idxOne <= length:
            idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
            if idxTwo != -1 and arr[idxOne][1] > arr[idxTwo][1]:
                swap = idxTwo
            else:
                swap = idxOne
            
            if arr[swap][1] < arr[idx][1]:
                self.swapValues(swap, idx, arr)
                idx = swap
                idxOne = idx * 2 + 1
            else:
                return
    
    def swapValues(self, i, j, arr):
        self.vertex[arr[i][0]] = j
        self.vertex[arr[j][0]] = i
        arr[i], arr[j] = arr[j], arr[i]
    
    def siftUp(self, curr_idx):
        parentIdx = (curr_idx - 1) // 2
        while curr_idx > 0:
            if self.heap[curr_idx][1] < self.heap[parentIdx][1]:
                self.swapValues(curr_idx, parentIdx, self.heap)
                curr_idx = parentIdx
                parentIdx = (curr_idx - 1) // 2
            else:
                return
                
    def update(self, idx, value):
        curr_idx = self.vertex[idx]
        self.heap[curr_idx] = (idx, value)
        self.siftUp(curr_idx)
