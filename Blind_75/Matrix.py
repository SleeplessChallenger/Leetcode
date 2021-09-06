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
