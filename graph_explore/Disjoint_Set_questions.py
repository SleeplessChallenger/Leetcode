# 1. Number of Provincies
class Solution:
    '''
    cities belong to one province if they're
    drectly or indirectly connected => we need
    to count only distinct provincies.
    And due to construction of Disjoint Set,
    `self.root` will contain roots of provincies.
    
    Ex: [1, 2, 3, 4] with [[1,1,0,0], [1,1,0,1],
    [0,0,1,0], [0,1,0,1]] will have
    self.root = [0, 0, 2, 1] => when we count
    UNIQUE provincies, i.e. value == i, it'll
    be 2.
    '''
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = DisjointSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                figure = isConnected[i][j]
                if figure == 0:
                    continue
                    
                graph.union(i, j)
        
        count = 0
        for i in range(len(graph.root)):
                if graph.root[i] == i:
                    count += 1
        
        return count


class DisjointSet:
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
    
    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

# LC solution
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		graph = DisjointSet(len(isConnected))

		for i in range(len(isConnected)):
			for j in range(len(isConnected[i])):
				if isConnected[i][j] == 1:
					graph.union(i, j)

		return graph.get_count()


class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in self.root]
        self.count = size
    
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
            self.count -= 1
    
    def get_count(self):
    	return self.count

# 2. Graph Valid Tree
class Solution:
    # UnionFind
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph must contain n-1 edges
        # otherwise: 4 & [[0,1],[2,3]] is True but should be False

        if len(edges) != n - 1:
            return False
    
        graph = UnionFind(n)
        
        # without adjacency list
        for e1, e2 in edges:
            # if roots are equal
            # => already put
            # in the graph and 
            # it must be False
            if not graph.union(e1, e2):
                # [[0,1],[1,2],[2,3],[1,3],[1,4]]
                # here 0 - 1, 0 - 2, 0 - 3. Hence
                # when we `union(1,3)`, both roots
                # are 0 => return False
                return False
        
        return True
        

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self, vertex):
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1
            return True
        else:
            return False

    # DFS
    '''
    graph is a tree when:
    1. all nodes are connected
    2. no cycles
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        in undirected graph simple check
        "if node in seen = False" doesn't work
        as adj. list has two-sided connection
        I.e. 4 <-> 1.
        That's why there're 2 options: either delete
        opposite direction edge or use hashtable to keep
        parents of nodes
        '''
        if len(edges) != n - 1:
            return False
        
        adj = [[] for i in range(n)]
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        parent = {0: -1}
        stack = [0]
        while len(stack) != 0:
            node = stack.pop()
            for edge in adj[node]:
                if parent.get(node) == edge:
                    # 0: [1,2,3]; 1: [0,4]
                    continue
                
                if edge in parent:
                    return False
                
                parent[edge] = node
                stack.append(edge)
        
        return len(parent) == n

    # DFS2
    '''
    nodes must be equal to n - 1 edges. Why?
    If there're more edges -> cycles and if
    there're fewer edges -> not fully connected
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = {0}
        stack = [0]
        
        adj = [[] for i in range(n)]
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        while len(stack) != 0:
            node = stack.pop()
            for edge in adj[node]:
                if edge in visited:
                    '''
                    bypass trivial cycles.
                    And if there are real
                    cycles, we'll caught them
                    during final check
                    '''
                    continue
                stack.append(edge)
                visited.add(edge)
        
        return len(visited) == n

# 3. Number of Connected Components in an Undirected Graph
class Solution:
    # Union Find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = set()
        graph = UnionFind(n)
        
        for e1, e2 in edges:
            graph.union(e1, e2)
        
        for r in range(len(graph.root)):
            '''
            traverse all roots from 0 to n.
            Find root of every node, add to
            hash set.
            
            ATTENTION: when we have
            [[0,1],[2,3],[1,2]]. Here
            we have 0-1 & 2-3, but last
            sublist unite 0-1 & 2-3. And
            what happens in this case? We change
            root value of 2 to 0, but root value
            of 3 stays 3.
            => simple traversal over self.root
            and dumping into hashset won't work
            '''
            root = graph.find(r)
            result.add(root)
        
        return len(result)

        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self, vert):
        if self.root[vert] == vert:
            return vert
        self.root[vert] = self.find(self.root[vert])
        return self.root[vert]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1

    # DFS
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        number of times we start visiting
        unconnected node (unvisited vertex)
        => +1 to new component
        '''
        adj = [[] for _ in range(n)]
        visited = set()
        count = 0
        stack = [0]
        
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(i, adj, visited)
        
        return count
    
    def dfs(self, curr, adj, visited):
        if curr in visited:
            return
        
        visited.add(curr)
        for edge in adj[curr]:
            self.dfs(edge, adj, visited)

# 4. The Earliest Moment When Everyone Become Friends

# Union Find
class Solution:
    '''
    When we have identical roots =>
    `count` won't be decreased. 
    Hecnce, [[0,1],[3,4],[2,3],
    [1,5],[2,4],[0,3]].
    1. union(0,1) -> different roots
    2. union(3,4) -> different roots
    3. union(2,3) -> different roots
    4. union(1,5) -> different roots
    
    5. union(2,4) -> SAME ROOTS. As
    2 has root of 3 and 4 has root of 3
    hence we don't decrease -1
    
    6. union(0,3) -> different roots
    And at this moment we have
    graph.count == 1
    
    '''
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        graph = UnionFind(n)
        
        for data in logs:
            graph.union(data[1], data[2])
            if graph.count == 1:
                return data[0]
    
        return -1


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size
    
    def find(self, vert):
        if self.root[vert] == vert:
            return vert
        self.root[vert] = self.find(self.root[vert])
        return self.root[vert]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1

            self.count -= 1

# 5. Evaluate Division
class Solution:
# dfs
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        for (d1, d2), value in zip(equations, values):
            graph[d1][d2] = value
            graph[d2][d1] = 1/value
        
        def dfs(explored, v1, v2, val):
            explored.add(v1)
            adjacent = graph[v1]
            result = -1.0
            
            if v2 in adjacent:
                result = val * adjacent[v2]
            else:
                for k, v in adjacent.items():
                    if k in explored:
                        continue
                    # we need to mult `val` as we're
                    # traversing node
                    result = dfs(explored, k, v2, val * v)
                    if result != -1.0:
                        break
                        
            explored.remove(v1)
            return result
        
        total = []
        
        for q1, q2 in queries:
            if q1 not in graph or q2 not in graph:
                result = -1.0
            elif q1 == q2:
                result = 1.0
            else:
                visited = set()
                result = dfs(visited, q1, q2, 1)
                
            total.append(result)
        
        return total

# Union Find


# 6. Optimize Water Distribution in a Village
class Solution:
    # Prim's with Min Heap
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        '''
        In traditional MST we can't have weighted
        vertices, only edges. In our case we have pipes
        construction cost as edges and wells construction
        cost as verticies weights. Hence we're to remove
        weights from verticies to edges by creating 
        virtual edge.
        
        1. `adjacency list` to keep our graph
        2. `set` to keep our final MST and determine
        whether the vertex has been added
        3. Min Heap to determine min cost vertex
        '''
        graph = {0: []}
        
        for vertex in range(len(wells)):
            cost = wells[vertex]
            '''
            +1 because we want to simulate
            other vertices => they start from 1
            '''
            graph[0].append((cost, vertex + 1))
        
        for vertex1, vertex2, cost in pipes:
            if vertex1 not in graph:
                graph[vertex1] = []
            
            graph[vertex1].append((cost, vertex2))
            
            if vertex2 not in graph:
                graph[vertex2] = []
            
            graph[vertex2].append((cost, vertex1))
        
        explored = set([0])
        heap = MinHeap(graph[0])
        
        result = 0
        while len(explored) < n + 1:
            cost, next_vertex = heap.remove()
            if next_vertex not in explored:
                explored.add(next_vertex)
                result += cost
                if next_vertex not in graph:
                    continue
                else:
                    for new_cost, adjacent_vertex in graph[next_vertex]:
                        if adjacent_vertex not in explored:
                            heap.insert((new_cost, adjacent_vertex))
        
        return result

    
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

    # Kruskal's with Union Find
        def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
            '''
            create virtual vertex as well as we're
            to deal with wells. But here we need
            to use list() as dict() cannot be sorted
            '''
            graph = []
            for vertex in range(len(wells)):
                cost = wells[vertex]
                graph.append((cost, 0, vertex + 1))

            for v1, v2, cost in pipes:
                graph.append((cost, v1, v2))

            '''
            sort edges including virtual one. And hence
            here we don't start from 0 as with Prim.
            And by doing so we start from smallest cost.
            '''
            graph.sort(key=lambda x: x[0])
            '''
            pay attention that we start
            from 0 node, not 1 (simply speaking
            we need one more node)
            '''
            union_graph = UnionFind(n + 1)
            result = 0

            for component in graph:
                cost, v1, v2 = component
                if union_graph.union(v1, v2):
                    result += cost
                else:
                    continue

            return result
        
        
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
