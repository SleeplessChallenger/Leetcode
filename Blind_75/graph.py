# medium chunk
# 1. medium - Number of Islands
# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = [[False for col in range(len(grid[0]))] for row in grid]
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                token = grid[i][j]
                if token != '1':
                    continue
                if explored[i][j]:
                    continue
                
                result += self.traverse([[i, j]], explored, grid)
        
        return result
                
                
    def traverse(self, stack, explored, grid):
        while len(stack) > 0:
            i, j = stack.pop()
            if explored[i][j]:
                continue
            
            explored[i][j] = True
            if grid[i][j] != '1':
                continue
            
            self.visit_neighbours(explored, i, j, stack, grid)
        
        return 1
            

    def visit_neighbours(self, explored, i, j, stack, grid):
        if i > 0 and not explored[i - 1][j]:
            stack.append([i - 1, j])
        if j > 0 and not explored[i][j - 1]:
            stack.append([i, j - 1])
        if i < len(grid) - 1 and not explored[i + 1][j]:
            stack.append([i + 1, j])
        if j < len(grid[i]) - 1 and not explored[i][j + 1]:
            stack.append([i, j + 1])

    # Union Find
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        ones = self.count_ones(grid)
        
        uf = UnionFind(rows*cols, ones)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    continue
                
                index = i * cols + j

                # `rows - 1` is last idx =>
                # we use `<` to allow one step
                if i < rows - 1 and grid[i+1][j] == '1':
                    uf.union(index, index + cols)

                if j < cols - 1 and grid[i][j+1] == '1':
                    uf.union(index, index + 1)
                
        
        return uf.count
                
    def count_ones(self, grid):
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
     
        return count
        

class UnionFind:
    def __init__(self, size, ones_count):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in self.root]
        self.count = ones_count
    
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
            

# 2 medium - Pacific Atlantic Water Flow
class Solution:
    # bfs
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid or not grid[0]:
            return []
        
        height = len(grid) # we don't need -1 as range() already exclusive
        length = len(grid[0]) # we don't need -1 as range() already exclusive
        
        queue1 = deque()
        queue2 = deque()
        # putting rows
        for i in range(height):
            queue1.append((i, 0))
            queue2.append((i, length - 1))
        
        # putting columns
        for j in range(length):
            queue1.append((0, j))
            queue2.append((height - 1, j))
        
        reach1 = self.bfs(grid, queue1, height, length)
        reach2 = self.bfs(grid, queue2, height, length)
        
        # return list(reach1.intersection(reach2))
        
        result = []
        for r in reach1:
            if r in reach2:
                result.append(r)
        
        return result
    
    def bfs(self, grid, queue, height, length):
        reachable = set()
        while len(queue) != 0:
            row, col = queue.popleft()
            reachable.add((row, col))
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = row + i
                new_col = col + j
                
                if new_row < 0 or new_row >= height or\
                    new_col < 0 or new_col >= length:
                    continue
                if (new_row, new_col) in reachable:
                    continue
                if grid[row][col] > grid[new_row][new_col]:
                    continue
                
                queue.append((new_row, new_col))
            
        return reachable

    # dfs
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid or not grid[0]:
            return []
        
        visited1 = set()
        visited2 = set()
        
        length = len(grid[0])
        height = len(grid)
        
        for i in range(height):
            self.dfs(grid, length, height, visited1, i, 0)
            self.dfs(grid, length, height, visited2, i, length - 1)
        
        for j in range(length):
            self.dfs(grid, length, height, visited1, 0, j)
            self.dfs(grid, length, height, visited2, height - 1, j)
        
        return list(visited1.intersection(visited2))
        
        
    def dfs(self, grid, length, height, visited, row, col):
        visited.add((row, col))
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row = row + i
            new_col = col + j
            if new_row < 0 or new_row >= height or\
                new_col < 0 or new_col >= length:
                continue
            if (new_row, new_col) in visited:
                continue
            if grid[new_row][new_col] < grid[row][col]:
                continue
            
            self.dfs(grid, length, height, visited, new_row, new_col)
   

# 3. Course Schedule
class Solution:
    # class structure
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.create_graph(numCourses, prerequisites)
        return self.can_finish(graph)
        
    def create_graph(self, num, prerequisites):
        graph = Courses(num)
        
        for main, prereq in prerequisites:
            graph.update(prereq, main)
        
        return graph
    
    def can_finish(self, graph):

        for vertex in graph.verticies:
            isCycle = self.dfs(vertex, graph)
            if isCycle:
                return False
        
        return True
    
    def dfs(self, vertex, graph):
        if vertex.visiting:
            return True
        if vertex.visited:
            return False
        
        vertex.visiting = True
        
        for prereq in vertex.prereqs:
            isCycle = self.dfs(prereq, graph)
            if isCycle:
                return True
        
        vertex.visited = True
        vertex.visiting = False
        return False
        

class Courses:
    def __init__(self, courses):
        self.graph = {}
        self.verticies = []
        for course in range(courses):
            self.insert(course)
            
    def insert(self, course):
        course_node = Course(course)
        self.verticies.append(course_node)
        self.graph[course] = course_node
    
    def get_node(self, course):
        return self.graph[course]
    
    def update(self, a, b):
        node_a = self.get_node(a)
        node_b = self.get_node(b)
        node_a.prereqs.append(node_b)

        
class Course:
    def __init__(self, course):
        self.course = course
        self.prereqs = []
        self.visited = False
        self.visiting = False
        
    # adjacency list
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True
        
        graph = {}
        inDegree = {}
        
        for i in range(numCourses):
            graph[i] = []
            inDegree[i] = 0
        
        for main, prereq in prerequisites:
            graph[main].append(prereq)
            inDegree[prereq] += 1
        
        queue = []
        for node in inDegree:
            if inDegree[node] == 0:
                queue.append(node)
        
        while len(queue) != 0:
            node = queue.pop(0)
            
            for vertex in graph[node]:
                inDegree[vertex] -= 1
                if inDegree[vertex] == 0:
                    queue.append(vertex)
            
            
        for vertex in inDegree:
            if inDegree[vertex] != 0:
                return False
            
        return True
