# 1. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        # because root of 1 is 1
        # & root of 0 is 0
        if x < 2:
            return x
        
        left = 2
        right = x // 2
        # hence our border is [2 to target / 2]
        # I.e. 2:8 / 2
        
        while left <= right:
            # pay attention that we use // to make
            # it without the leftover
            midd = (left + right) // 2
            if midd * midd < x:
                left = midd + 1
            elif midd * midd > x:
                right = midd - 1
            else:
                return midd
        
        return right

# 2. Guess Number Higher or Lower
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 2
        right = n
        
        while True:
            middle = (left + right) // 2
            result = guess(middle)
            
            if result == 0:
                return middle
            elif result == -1:
                right = middle - 1
            elif result == 1:
                left = middle + 1
