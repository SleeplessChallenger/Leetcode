# 1. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 2:
            return True
        
        left = 0
        right = num // 2
        
        while left <= right:
            midd_num = (left + right) // 2
            if midd_num * midd_num < num:
                left = midd_num + 1
            elif midd_num * midd_num > num:
                right = midd_num - 1
            else:
                return True
            
        return False

# 2. Find Smallest Letter Greater Than Target
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # as letters wrap as it's said in description
        # Also, in second check we do `>` as we need to find
        # first BIGGER value
        if letters[-1] <= target or letters[0] > target:
            return letters[0]
        
        left = 0
        right = len(letters) - 1
        
        while left <= right:
            midd = (left + right) // 2
            
            if letters[midd] <= target:
                left = midd + 1
            else: # letters[midd] < target
                right = midd - 1
        
        return letters[left]
