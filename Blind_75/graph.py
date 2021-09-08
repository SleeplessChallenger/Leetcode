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
