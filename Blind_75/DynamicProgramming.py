# 1. easy - Climbing Stairs
class Solution:
    # top-down
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        memo = [-1  for _ in range(n)]
        memo[0] = 1
        memo[1] = 2
        # as we placed values in first 2 positions,
        # we'll decrease overall `n`
        return self.findWays(n - 1, memo)
     
    def findWays(self, n, memo):
        if memo[n] < 0:
            memo[n] = self.findWays(n - 1, memo) +\
                self.findWays(n - 2, memo)
        return memo[n]
    
    # bottom-up with O(n) Space
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        memo = [0 for _ in range(n)]
        memo[0] = 1
        memo[1] = 2
        # as we put values in idx = 0/1
        # start from idx = 2
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[-1]
    
    # bottom-up with O(1) Space
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(2, n):
            temp = first + second
            first = second
            second = temp
            ## or another way
            # temp = second
            # second = first + second
            # first = temp
        return second

