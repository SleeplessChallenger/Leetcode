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

# 8. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.traverse(result, 0, 0, n, [])
        return result

    def traverse(self, result, left, right, n, temp):
        if len(temp) == 2 * n:
            result.append("".join(temp))
            return

        if left < n:
            temp.append('(')
            self.traverse(result, left + 1, right, n, temp)
            temp.pop()

        if left > right:
            temp.append(')')
            self.traverse(result, left, right + 1, n, temp)
            temp.pop()

# 9. Convert Binary Search Tree to Sorted Doubly Linked List
class Solution:
    # Time: O(n) Space: O(n)
    '''
    As it's BST => inorder traversal will
    create already sorted list
    '''
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        nodes = self.in_order_traversal(root)
        
        if len(nodes) == 0:
            return None
        
        elif len(nodes) == 1:
            node = nodes[0]
            node.left = node
            node.right = node
            return node

        for idx in range(1, len(nodes)):
            prev = nodes[idx - 1]
            curr = nodes[idx]
            
            prev.right = curr
            curr.left = prev
        
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]
        
        return nodes[0]
        
        
    def in_order_traversal(self, node):
        # morris traversal
        if node is None:
            return []
        elif node.left is None and node.right is None:
            return [node]
        
        result = []
        curr = node
        
        while curr:
            if curr.left:
                temp_node = curr.left
                while temp_node.right and temp_node.right != curr:
                    temp_node = temp_node.right
                
                if not temp_node.right:
                    temp_node.right = curr
                    curr = curr.left
                    
                elif temp_node.right == curr:
                    temp_node.right = None
                    result.append(curr)
                    curr = curr.right
    
            else:
                result.append(curr)
                curr = curr.right
        
        return result


    # in place
    head = None
    prev = None
    # Time: O(n) Space: O(d)
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        rightmost node in left subtree and
        leftmost node in right subtree
        '''
        if not root:
            return None
        self.traverse(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
    
    def traverse(self, node):
        if not node:
            return node
        self.traverse(node.left)
        if self.prev: # not head
            self.prev.right = node
            node.left = self.prev
        else: # head
            # here we enter inly ones
            # when leftmost branch is visited
            self.head = node
        self.prev = node
        self.traverse(node.right)

# 10. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.traverse(nums, result, 0)
        return result
    
    def traverse(self, nums, result, idx):
        if idx == len(nums):
            result.append(list(nums))
            return
        
        for i in range(idx, len(nums)):
            self.swap(i, idx, nums)
            self.traverse(nums, result, idx + 1)
            self.swap(i, idx, nums)
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

# 11. Largest Rectangle in Histogram
class Solution:
    # Time: O(n^2) Space: O(1)
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        
        total = 0
        
        for idx in range(len(heights)):
            left = idx
            right = idx
            count_left = 0
            count_right = 0
            
            while left > 0:
                if heights[left - 1] >= heights[idx]:
                    left -= 1
                    count_left += 1
                else:
                    break
            
            while right < len(heights) - 1:
                if heights[right + 1] >= heights[idx]:
                    right += 1
                    count_right += 1
                else:
                    break
            
            total = max(total, (count_left + count_right + 1) * heights[idx])
        
        return total
    
    # Time: O(n) Space: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        We put in stack idx, not values themselves
        
        1. Put -1 in stack and start traversal from 0
        
        2. While values in `heights` appear in increasing
            order -> append() them

        3. When we meet num with smaller value: `.pop()` from
            stack and use `idx` as current-smaller num as right
            border. Subtract next idx on the stack as left border.

        4. Then, if `curr` is still smaller -> pop() and do the same
            as above, else append() idx to the stack

        5. If there is only -1 left on the stack => simply append().
            But there CAN be case when left border is -1.
        
        6. As we `.pop()` only when values are greater on the stack
            than current => they'll encompass the range
        
        
        '''
        stack = [-1]
        max_value = 0
        
        for idx in range(len(heights)):
            curr = heights[idx]
            
            while stack[-1] != -1 and curr <= heights[stack[-1]]:
                node_idx = stack.pop()
                node = heights[node_idx]
                
                diff = idx - stack[-1] - 1
                # `curr` as we need smallest value and
                # we enter here only if curr <= top on stack
                value = diff * node
                max_value = max(max_value, value)
            
            stack.append(idx)
        
        # to deal with remaining
        while stack[-1] != -1:
            node_idx = stack.pop()
            node = heights[node_idx]
            
            diff = len(heights) - stack[-1] - 1
            value = diff * node
            max_value = max(max_value, value)
        
        return max_value

# 12. Letter Combinations of a Phone Number
class Solution: 
    '''
    We don't use `for loop`. but [idx] as we need
    to lock letter and loop will constantly shift it
    '''
    # first
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        ht = {
        '1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': []
        }
        
        result = []
        self.traverse(result, digits, [0 for _ in range(len(digits))], 0, ht)
        return result
    
    def traverse(self, result, digits, temp, idx, ht):
        if idx == len(digits):
            result.append(''.join(temp))
            return
        else:
            digit = digits[idx]
            for letter in ht[digit]:
                temp[idx] = letter
                self.traverse(result, digits, temp, idx + 1, ht)
    
    # second
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        ht = {
        '1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': []
        }
        
        result = []
        self.traverse(result, digits, [], 0, ht)
        return result
    
    def traverse(self, result, digits, temp, idx, ht):
        if len(temp) == len(digits):
            result.append(''.join(temp))
            return
        else:             
            digit = digits[idx]
            for letter in ht[digit]:
                temp.append(letter)
                self.traverse(result, digits, temp, idx + 1, ht)
                temp.pop()

# 13. The Skyline Problem
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return []
        
        elif len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        mid = len(buildings) // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])
        
        return self.merge_output(left_skyline, right_skyline)
    
    def merge_output(self, left, right):
        l = r = 0
        curr_y = left_y = right_y = 0
        result = []
        
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                # `left_y` same as in the start
                x, left_y = left[l]
                l += 1
            else:
                x, right_y = right[r]
                r += 1
            # between both
            max_y = max(left_y, right_y)
            # change in Skyline
            if curr_y != max_y:
                self.update_output(result, x, max_y)
                curr_y = max_y

        while l < len(left):
            x, y = left[l]
            l += 1
            if y != curr_y:
                self.update_output(result, x, y)
                curr_y = y
            
        while r < len(right):
            x, y = right[r]
            r += 1
            if y != curr_y:
                self.update_output(result, x, y)
                curr_y = y
        
        return result
    
    def update_output(self, result, x, max_y):
        # horizontal
        if len(result) == 0 or result[-1][0] != x:
            result.append([x, max_y])
        # vertical
        else:
            result[-1][1] = max_y
