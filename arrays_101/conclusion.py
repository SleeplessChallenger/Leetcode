# 1. Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                count += 1
        
        return count

# 2. Max Consecutive Ones II
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # v1
#         if len(nums) < 2:
#             return 1
        # we need right as 0:
    # [0, 0] in this case edge case check won't help
        right = 0
        left = 0
        longest = 0
        zeroIdx = 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeroIdx += 1
            
            while zeroIdx == 2:
                # if left != 0: just move right
                # elif 0: decrease count & move right
                if nums[left] == 0:
                    zeroIdx -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest
