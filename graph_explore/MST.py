# 1. Min Cost to Connect All Points

'''
At first, let's understand that Kruskal's algo works on edges
whilst Prim's algo works on verticies. What does it mean?
=> Kruskal's algo will connect edges step by step skipping
when they have same root, whilst Prim's will do the same, but
with verticies. Check "Optimize Water Distribution in a Village" LC solution to get clearer
understanding.

1. We need real graph as what we have is a bunch of points.
* Why we don't have `range()`
spanning from 0 to len(points)?
=> We start from 0 vertex and connect
with every other one. When we switch to
vertex 1: don't need to connect with
0 again as we've already done it + we
don't build true-**adjacency list,** hence no
need to create **bi-directional** edges. 
So, from node 1 we need to connect to
any other node except for 0 as we've
already have it.
* Why in the upper loop we have `-1`? Remember that
when we reach last node it'll be connected with any other node already, so
reconnecting will create cycles.

   
2. As stated in Kruskal's algo rules: sort() all edges from smallest cost to
the biggest.

3. After having been sorted, we'll start connect vertices. But how do we
ensure that our MST (minimum spanning tree) is real?

Features of MST:
* it is constructed of smallest weights
* it is constructed of smallest amount on edges
=> we implemented `sort() ` for this purpose.

But what about second feature? Union Find will rescue us as it does
have functionality to reject connection of already connected verticies
by checking their root nodes. If roots are the same => don't connect.
So, we won't have any excessive edges.

4. And to improve Time Complexity we can have additional check: number of edges
in MST is** number of nodes - 1** (it's a rule), so when we've connected required amount => break even if we still have something. Due to being sorted we've ensured smallest weight, so no need to proceed.

Ways to improve? When we sort() it takes us `n*logn`. When we use **min heap** we can decrease this to `logn`.

Overall, Time complexity of Kruskal's algo is `e*loge` where e is edge. **UnionFind** is swift in T & S Complexity. + we have basic sorting which is `n*logn`. So, `2 * n*logn` or `n*logn + logn` if with **Heap**.

'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 0
        
        graph = self.create_graph(points)
        graph.sort(key=lambda x: x[2])
        
        n = len(points)
        uf = UnionFind(n)
        
        result = 0
        count = 0
        
        for i in graph:
            vertex, node, cost = i
        
            if count == n - 1:
                break
            
            if uf.union(vertex, node):
                result += cost
                count += 1
            else:
                continue
        
        return result

    def create_graph(self, points):
        graph = []
  
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                
                curr_point = points[i]
                next_point = points[j]
                result = self.difference(curr_point[0], curr_point[1],
                                        next_point[0], next_point[1])
                
                graph.append([i, j, result])

        return graph
    
    def difference(self, a, b, c, d):
        return abs(a - c) + abs(b - d)


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in self.root]
    
    def find(self, vertex):
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
            
            return True
        
        else:
            return False


    # Prim's Algo
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {}
        self.create_graph(points, graph)
     
        visited = {0}
        min_heap = MinHeap(graph[0])

        result = 0

        while len(visited) < len(points):
            cost, vertex = min_heap.remove()
            if vertex not in visited:
                visited.add(vertex)
                result += cost
                
                # if vertex not in graph:
                #     continue
                
                for i in graph[vertex]:
                    cost, node = i
                    if node not in visited:
                        min_heap.insert((cost, node))

        return result
        
    def create_graph(self, points, graph):
        for point in range(len(points)):
            graph[point] = []
        
        for i in range(len(points) - 1):
            # can be with -1 or without
            for j in range(i + 1, len(points)):
                curr_point = points[i]
                next_point = points[j]
                result = self.difference(curr_point[0], curr_point[1],
                                        next_point[0], next_point[1])
                    
                graph[i].append((result, j))
                graph[j].append((result, i))
    
    
    def difference(self, a, b, c, d):
        return abs(a - c) + abs(b - d)
     

class MinHeap:
    def __init__(self, arr):
        self.heap = self.buildHeap(arr)
    
    def check(self):
        return len(self.heap) == 0
    
    def buildHeap(self, arr):
        parentIdx = (len(arr) - 2) // 2
        for i in reversed(range(parentIdx + 1)):
            self.siftDown(i, len(arr) - 1, arr)
        return arr
    
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        to_remove = self.heap[0]
        node = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = node
            self.siftDown(0, len(self.heap) - 1, self.heap)
        return to_remove
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
    
    def siftDown(self, idx, length, arr):
        idxOne = idx * 2 + 1
        while idxOne <= length:
            idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
            if idxTwo != -1 and arr[idxOne][0] > arr[idxTwo][0]:
                swap = idxTwo
            else:
                swap = idxOne
            
            if arr[swap][0] < arr[idx][0]:
                self.swapValues(swap, idx, arr)
                idx = swap
                idxOne = idx * 2 + 1
            else:
                return
    
    def swapValues(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]
    
    def siftUp(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parentIdx = (idx - 1) // 2
            if self.heap[idx][0] < self.heap[parentIdx][0]:
                self.swapValues(idx, parentIdx, self.heap)
                idx = parentIdx
            else:
                return        
