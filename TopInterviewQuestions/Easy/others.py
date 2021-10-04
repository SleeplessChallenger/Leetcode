# 1. Pascal's Triangle
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dp = [[1]]
        prev = None
        
        for i in range(1, n):
            prev = dp[i - 1]
            curr = [1]
            for j in range(1, i):
                curr.append(prev[j - 1] + prev[j])
            
            curr.append(1)
            dp.append(curr)
        
        return dp
# ver. 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        count = 0
        while count < numRows - 1:
            count += 1
            curr = [1]
            for i in range(1, count):
                curr.append(result[count-1][i-1] + 
                           result[count-1][i])
            curr.append(1)
            result.append(curr)
        
        return result

# 2. Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x > 0 or y > 0:
            count += (x % 2) ^ (y % 2)
            x >>= 1
            y >>= 1
        
        return count
