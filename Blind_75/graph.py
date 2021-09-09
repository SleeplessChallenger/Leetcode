# medium chunk
# 1. medium - Number of Islands
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
   
