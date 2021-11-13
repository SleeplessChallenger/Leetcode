# 1. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:        
        curr = 0
        res = 0
        for num in nums:
            if num == 1:
                curr += 1
                res = max(res, curr)
            else:
                curr = 0
        
        return res

# 2. Find Numbers with Even Number of Digits
class Solution:
    # simpler
    def findNumbers(self, nums: List[int]) -> int:
        length = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                length += 1
        
        return length
