# Medium chunk
# 1. Spiral Matrix
class Solution:
	    '''
    [
     [1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]
    ]
    
    after first full iteration: 
        start_row = 1/end_row = 1/start_col = 1/end_col = 2
    => only first `for` loope will go, then second will be skipped
    as start_row == end_row. Then we go into third loop where
    `break` condition turns in. Then fourth loop where loop
    will be skipped as start_row + 1 > end_row
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        s_r, s_c = 0, 0
        e_r, e_c = len(matrix) - 1, len(matrix[0]) - 1
        
        while s_r <= e_r and s_c <= e_c:
            for idx in range(s_c, e_c + 1):
                result.append(matrix[s_r][idx])
            
            for idx in range(s_r + 1, e_r + 1):
                result.append(matrix[idx][e_c])
            
            for idx in reversed(range(s_c, e_c)):
                if s_r == e_r:
                    break
                
                result.append(matrix[e_r][idx])
            
            for idx in reversed(range(s_r + 1, e_r)):
                if s_c == e_c:
                    break
                
                result.append(matrix[idx][s_c])
            
            s_r += 1
            s_c += 1
            e_r -= 1
            e_c -= 1
        
        return result

# 2 Set Matrix Zeroes
class Solution:
    # Mine (not-optimal)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # flipped values are not considered as zeros
        real_zeros = []
        self.findRealZeros(matrix, real_zeros)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                figure = matrix[i][j]
                
                if figure != 0:
                    continue
                
                if [i, j] not in real_zeros:
                    continue
                    
                self.flipValues(matrix, i, j)
    
    def flipValues(self, matrix, i, j):
        for a in range(len(matrix[i])):
            matrix[i][a] = 0
        
        for b in range(len(matrix)):
            matrix[b][j] = 0
        
    def findRealZeros(self, matrix, real_zeros):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                figure = matrix[i][j]
                if figure != 0:
                    continue

                real_zeros.append([i, j])

    # Optimal (non-mine)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                # if we need to set 0
                # for first column
                is_col = True
            
            # start with second row so as
            # not to mess first row as we can
            # simply check first row in the end
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Traverse from second row & col and if
        # first row or col was marked (0 is False in bool
        # hence `not` is a nice check)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

# 3. Word Search
class Solution:
    # mine
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    result = self.backtrack(visited, board, i, j, word, 1)
                    if result:
                        return True
        
        return False
    
    def backtrack(self, visited, board, row, col, word, idx):
        if idx == len(word):
            return True
        
        visited.add((row,col))
        # for i in range(idx, len(word)):
        cells = self.explore(visited, board, row, col, idx, word)
        for cell in cells:

            res = self.backtrack(visited, board, cell[0],
                        cell[1], word, idx+1)

            if res:
                return True
            
        visited.remove((row,col))
        return False
            
    # 1. check that cell is within ranges of board
    # 2. check that cell isn't in visited
    # 3. check that letter in cell == curr letter
    def explore(self, visited, board, row, col, idx, word):
        result = []
        
        if row > 0:
            if (row-1,col) not in visited and board[row-1][col] == word[idx]:
                result.append([row-1,col])
        
        if row + 1 <= len(board) - 1:
            if (row+1,col) not in visited and board[row+1][col] == word[idx]:
                result.append([row+1,col])
        
        if col > 0:
            if (row,col-1) not in visited and board[row][col-1] == word[idx]:
                result.append([row,col-1])
        
        if col + 1 <= len(board[0]) - 1:
            if (row,col+1) not in visited and board[row][col+1] == word[idx]:
                result.append([row,col+1])
        
        return result
    
    # not mine
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.backtrack(board, word, i, j):
                    return True
        
        return False
    
    def backtrack(self, board, word, row, col):
        if len(word) == 0:
            return True
        
        if row < 0 or col < 0 or row > len(board) - 1 or\
            col > len(board[0]) - 1 or board[row][col] != word[0]:
            return False
        
        # used inside loop
        result = False
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        board[row][col] = '#'
        
        for d in directions:
            result = self.backtrack(board, word[1:], row+d[0], col+d[1])
            if result:
                break
        
        board[row][col] = word[0]
        return result

# Hard chunk
# 4. Word Search II

class Solution:
    # Time: O(N*M(4*3^L-1))
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        visited = [[False for col in row]
                  for row in board]
        
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                # pay attention that we give .root of trie
                self.grid_search(i, j, visited, trie.root, result, board)
        
        return result
    
    def grid_search(self, row, col, visited, node, result, board):
        # check for if letter in node => proceed
        # else break away is a type of backtracking
        if visited[row][col]:
            return
        letter = board[row][col]
        if letter not in node:
            return
        node = node[letter]
        
        visited[row][col] = True
        if '*' in node:
            if node['*'] not in result:
                result.append(node['*'])
        
        # continue search even after word was found
        adjacent_cells = self.explore(row, col, visited, board)
        for r, c in adjacent_cells:
            self.grid_search(r, c, visited, node, result, board)
            # why we don't  `return` here?
            # => we need to go further as there can be more
            # word down this path: dog - OK, but what if
            # we also have dogs? -> proceed down the trie
        visited[row][col] = False
    
    def explore(self, row, col, visited, board):
        temp = []
        
        if row > 0:
            if not visited[row-1][col]:
                temp.append([row-1, col])
        
        if col > 0:
            if not visited[row][col - 1]:
                temp.append([row, col-1])
        
        if row + 1 <= len(board) - 1:
            if not visited[row+1][col]:
                temp.append([row+1, col])
        
        if col + 1 <= len(board[0]) - 1:
            if not visited[row][col+1]:
                temp.append([row, col+1])
        
        return temp
        

class Trie:
    def __init__(self):
        self.root = {}
        self.mark = '*'
    
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        
        node[self.mark] = word
