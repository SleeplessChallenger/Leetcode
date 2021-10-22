# Target Sum
class Solution:
    # not mine
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ht = {} # (index, total)
        
        def backtrack(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            
            if (idx,total) in ht:
                return ht[(idx,total)]
            
            ht[(idx,total)] = \
                backtrack(idx+1, total+nums[idx]) +\
                backtrack(idx+1, total-nums[idx])
            
            return ht[(idx,total)]
            
        return backtrack(0, 0)
