# 1. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        arr = [0 for _ in range(len(nums) + 1)]
        arr[1] = nums[0]
        
        for i in range(1, len(nums)):
            arr[i + 1] = max(arr[i], arr[i - 1] + nums[i])
         
        return arr[-1]
