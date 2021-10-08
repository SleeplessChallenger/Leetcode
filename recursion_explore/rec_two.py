# 1. Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case
        if len(nums) == 1:
            return nums
        
        middle = (0 + len(nums)) // 2
        arr1 = self.sortArray(nums[:middle])
        arr2 = self.sortArray(nums[middle:])
        return self.merge(arr1, arr2, 0, 0)
        
    def merge(self, arr1, arr2, idx1, idx2):
        result = []
        
        while idx1 < len(arr1) and idx2 < len(arr2):
            if arr1[idx1] < arr2[idx2]:
                result.append(arr1[idx1])
                idx1 += 1
            else:
                result.append(arr2[idx2])
                idx2 += 1
        
        while idx1 < len(arr1):
            result.append(arr1[idx1])
            idx1 += 1
        
        while idx2 < len(arr2):
            result.append(arr2[idx2])
            idx2 += 1
        
        return result

# 2. Search a 2D Matrix II
class Solution:
    # binary search solution
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        for i in range(min(len(matrix[0]), len(matrix))):
            res1 = self.binary_search(matrix, i, target, True)
            res2 = self.binary_search(matrix, i, target, False)
            if res1 or res2:
                return True
        
        return False
    
    def binary_search(self, matrix, i, t, V):
        left = i
        right = len(matrix) - 1 if not V else len(matrix[0]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if V:
                if matrix[i][mid] < t:
                    left = mid + 1
                elif matrix[i][mid] > t:
                    right = mid - 1
                else:
                    return True
            else:
                if matrix[mid][i] < t:
                    left = mid + 1
                elif matrix[mid][i] > t:
                    right = mid - 1
                else:
                    return True
        
        return False
    
    # search space reduction
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        
        row = h - 1
        col = 0
        
        while col < w and row >= 0:
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True
            
        return False 


# 3. N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [0 for _ in range(n)]
        return self.get_count(board, 0, n)
    
    def get_count(self, board, row, n):
        if row == n:
            return 1
        
        count = 0
        for i in range(len(board)):
            if self.check(row, i, board):
                board[row] = i
                count += self.get_count(board, row + 1, n)
        
        return count        
                
    def check(self, row, col, board):
        for idx in range(row):
            prev_col = board[idx]
            similar_cols = prev_col == col
            similar_axes = abs(prev_col - col) == abs(row - idx)
            if similar_cols or similar_axes:
                return False
        return True
'''
`board` is our rows where we put columns.
We start by looking at first row. When we enter
`check` method for the first time, we don't enter the
loop as we have row == 0. Then we mark board[row=0] = 0.
Eventually, we'll find out it's False (for 4*4) and we need
to change it. But we again don't enter the loop and simply get
True, and then we mark board[row=0] = 1 (change the value).

In `check` method row is our limit till which we go. As
range() is exlusive, if curr row is 2, so we need to check everything
below 2 (0 and 1 respectively).
'''

# 4. N-Queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [0 for _ in range(n)]
        result = []
        
        self.get_result(board, result, n, 0)
        return self.populate_result(result, n)
    
    def get_result(self, board, result, n, row):
        if row == n:
            result.append(list(board))
            # list() is crucial
            return True
        
        for i in range(len(board)):
            if self.check(i, row, board):
                board[row] = i
                self.get_result(board, result,
                                         n, row + 1)  
    
    def check(self, col, row, board):
        for j in range(row):
            prev_col = board[j]
            similar_col = prev_col == col
            similar_axes = abs(col - prev_col) ==\
                abs(row - j)
            
            if similar_col or similar_axes:
                return False
            
        return True
    
    def populate_result(self, result, n):
        final = []
        full_row = ['.' for _ in range(n)]
        # to decrease Time Compl. we precalc. it here

        for r in result:
            # list() in crucial to avoid duplicates
            temp_list = []
            for col in r:
                curr_row = list(full_row)
                curr_row[col] = 'Q'
                temp_list.append(''.join(curr_row))
                

            final.append(temp_list)

        return final

# 5. Robot Room Cleaner
class Solution:
    def cleanRoom(self, robot):
        '''
        1. Pay attention that we don't remove from
            visited as in this task backtracking doesn't
            simply revert the whole action, but explored
            another cells.
        
        2. We use "right-hand-rule": when an obstacle
            in front: turn right.
        
        3. Use (0,0) as starting points as we don't know
            anything about precise position of the robot.
        '''
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        return self.backtrack((0,0), 0, directions, visited, robot)
    
    def backtrack(self, cell, d, directions, visited, robot):
        visited.add(cell)
        robot.clean()
        
        for i in range(4):
            new_d = (i + d) % 4
            new_cell = (cell[0] + directions[new_d][0],
                        cell[1] + directions[new_d][1]
            )
            
            if not new_cell in visited and robot.move():
                self.backtrack(new_cell, new_d, directions, visited, robot)
                self.go_back(robot)
            
            robot.turnRight()
        
    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

# 6. Sudoku Solver
    def solveSudoku(self, board: List[List[str]]) -> None:
        '''
        1. At first, look in `number_checker`. It's our
            backtracking template. Loop with check
            then so-called modification. After that we
            backtrack and if result is negative, unmark.
            
        2. Due to task specifics, at first we convert all
            to int and after all the work - back to str.
        '''
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
        
        self.traverse_board(0, 0, board)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = str(board[i][j])
    
    def traverse_board(self, row, col, board):
        if col == len(board[0]):
            col = 0
            row += 1
            if row == len(board):
                return True
        
        if board[row][col] == 0:
            return self.number_checker(row, col, board)
        
        return self.traverse_board(row, col + 1, board)
    
    def number_checker(self, row, col, board):
        for num in range(1, 10):
            if self.valid_check(num, row, col, board):
                board[row][col] = num
                if self.traverse_board(row, col + 1, board):
                    return True
        
        board[row][col] = 0
        return False

    def valid_check(self, num, row, col, board):
        inCol = num in board[row]
        inRow = num in map(lambda x: x[col], board)
        
        if inCol or inRow:
            return False
        
        r, c = row // 3, col // 3
        
        for rowIdx in range(3):
            for colIdx in range(3):
                real_row = rowIdx + r * 3
                real_col = colIdx + c * 3
                
                number = board[real_row][real_col]
                if num == number:
                    return False
        
        return True

# 7. Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        1. If you place `low` as low for recursive function
            => duplicates and further issues with checks.
            Hence use `idx + 1` as it'll be the base for
            the next round.
        '''
        result = []
        self.traverse(result, 1, n + 1, k)
        return result

    def traverse(self, result, low, high, k, temp=[]):
        if len(temp) == k:
            result.append(list(temp))
            # return/no return doesn't matter here
            return
        
        
        for idx in range(low, high):
            temp.append(idx)
            self.traverse(result, idx + 1, high, k, temp)
            temp.pop()
