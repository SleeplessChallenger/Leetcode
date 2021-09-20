# 1. Find if Path Exists in Graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        
        graph = {}
        for vertex in range(n):
            graph[vertex] = []
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        visited = {start}
        
        for edge in graph[start]:
            if edge not in visited:
                result = self.dfs(edge, visited, graph, end)
                if result:
                    return True
        
        return False
    
    def dfs(self, node, visited, graph, end):
        if node == end:
            return True
        
        if node not in visited:
            visited.add(node)
            for edge in graph[node]:
                result = self.dfs(edge, visited, graph, end)
                if result:
                    return True

# Union Find
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        '''
        We cannot simply check if
        root of start == root of end
        because when we connect 2 different
        graphs (for example, each has 4 nodes),
        then we change the root of the connecting
        node, but others are left untouched.
        
        '''
        graph = UnionFind(n)

        for e1, e2 in edges:
            graph.union(e1, e2)
    
        root1 = graph.find(start)
        root2 = graph.find(end)

        return root1 == root2


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


# 2. All Paths From Source to Target

# DFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        full_path = []
        n = len(graph)

        for vertex in graph[0]:
            arr = [0, vertex]
            self.dfs(vertex, graph, n, arr, full_path)

        return full_path
    
    def dfs(self, vertex, graph, n, arr, full_path):
        if vertex == n - 1:
            # list() is crucial otherwise
            # .pop() will affect it also
            full_path.append(list(arr))
            # return 
        else:
            for node in graph[vertex]:
                arr.append(node)
                self.dfs(node, graph, n, arr, full_path)
                arr.pop()

# Just another position of `arr`
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        full_path = []
        n = len(graph)

        for vertex in graph[0]:
            arr = [0]
            self.dfs(vertex, graph, n, arr, full_path)

        return full_path
    
    def dfs(self, vertex, graph, n, arr, full_path):
        arr.append(vertex)
        if vertex == n - 1:
            # list() is crucial otherwise
            # .pop() will affect it also 
            full_path.append(list(arr))
            # return 
        else:
            for node in graph[vertex]:
                # arr.append(node)
                self.dfs(node, graph, n, arr, full_path)
                arr.pop()

# 3. Clone Graph
class Solution:
    # DFS
    def cloneGraph(self, node: 'Node', visited=dict()) -> 'Node':
        # base case
        if not node:
            return node
        
        # to prevent loop
        if node in visited:
            return visited[node]
        
        curr = Node(node.val, [])
        
        visited[node] = curr
        
        for adj_node in node.neighbors:
            returned_node = self.cloneGraph(adj_node, visited)
            curr.neighbors.append(returned_node)
            
        return curr

    # BFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = [node]
        result = Node(node.val, [])
        visited = {node: result}
        
        while len(queue) != 0:
            curr = queue.pop(0)
            
            for adj_node in curr.neighbors:                
                if adj_node not in visited:
                    temp = Node(adj_node.val, [])
                    visited[adj_node] = temp
                    queue.append(adj_node)
                
                temp = visited[adj_node]
                visited[curr].neighbors.append(temp)

        return visited[node]
