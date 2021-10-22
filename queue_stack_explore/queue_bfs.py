# 1. Walls and Gates
class Solution:
    # TLE. Time: O(n^2) Space: O(n)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates, walls = self.get_arrays(rooms)
        
        while len(gates) != 0:
            gate = gates.pop(0)
            value = rooms[gate[0]][gate[1]]
            
            adjacent = self.get_adjacent(rooms, gates,
                            walls, gate[0], gate[1])
            
            for a in adjacent:
                i, j = a
                rooms[i][j] = value + 1
                gates.append([i,j])
            
    def get_adjacent(self, rooms, gates, walls, i, j):
        result = []
        
        if i > 0:
            if [i - 1,j] not in gates and [i - 1,j] not in walls and rooms[i - 1][j] == 2147483647:
                result.append([i - 1, j])
              
        if i + 1 <= len(rooms) - 1:
            if [i + 1, j] not in gates and [i + 1,j] not in walls and rooms[i + 1][j] == 2147483647:
                result.append([i + 1, j])
        
        if j > 0:
            if [i, j - 1] not in gates and [i,j - 1] not in walls and rooms[i][j - 1] == 2147483647:
                result.append([i, j - 1])
        
        if j + 1 <= len(rooms[0]) - 1:
            if [i, j + 1] not in gates and [i,j + 1] not in walls and rooms[i][j + 1] == 2147483647:
                result.append([i, j + 1])
        
        return result
        
    def get_arrays(self, rooms):
        gates = []
        walls = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                value = rooms[i][j]
                if value == 0:
                    gates.append([i,j])
                elif value == -1:
                    walls.append([i,j])
        
        return gates, walls
    
    # Time: O(n*m)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        '''
        1. Add only gates
        2. In loop if out of boundaries or
            not empty -> skip
        '''
        gates = 0
        free = 2147483647
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                value = rooms[i][j]
                if value != gates:
                    continue
                queue.append([i,j])
        
        while len(queue) != 0:
            node = queue.pop(0)
            r, c = node
            
            for d in directions:
                row = r + d[0]
                col = c + d[1]
                
                if row < 0 or col < 0 or row > len(rooms) - 1 or\
                    col > len(rooms[0]) - 1 or rooms[row][col] != free:
                    continue
                
                rooms[row][col] = rooms[r][c] + 1
                queue.append([row, col])

# 2. Open the Lock
class Solution(object):
    def openLock(self, deadends, target):
        visited = {'0000'}
        queue = [('0000', 0)]
        deadends = set(deadends)
        
        while len(queue) != 0:
            node, depth = queue.pop(0)
            
            if node == target:
                return depth
            elif node in deadends:
                continue
            
            # for i in self.get_numbers(node):
            #     if i not in visited:
            #         visited.add(i)
            #         queue.append((i, depth+1))  
            
            temp = self.get_numbers(node)
            
            for i in temp:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, depth+1))
        
        return -1
    
    # def get_numbers(self, num):
    #     for idx in range(4):
    #         curr = int(num[idx])
    #         for i in (-1,1):
    #             x = (curr + i) % 10
    #             yield num[:idx] + str(x) + num[idx + 1:]
    
    def get_numbers(self, num):
        temp = []
        
        for idx in range(4):
            curr = int(num[idx])
            for i in (-1,1):
                x = (curr + i) % 10
                temp.append(num[:idx] + str(x) + num[idx + 1:])
        
        return temp

# 3. Perfect Squares
class Solution:
    # dp
    # Time: O(n * root of n)
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]
        # math.sqrt(n): 3.4641016151377544
        # squares: [0, 1, 4, 9]

        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        
        # bottom-up
        for i in range(1, n + 1):
            for square in squares:
                if i >= square:
                    # in dp we save amount of numbers
                    # till the particular square
                    dp[i] = min(dp[i], 1 + dp[i - square])
        
        return dp[-1]

