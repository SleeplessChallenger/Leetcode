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
