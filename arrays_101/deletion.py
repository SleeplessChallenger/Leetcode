# Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) < 1:
            return 0
        i = 0
        left = 0
        
        while i < len(nums):
            if nums[left] == val:
                self.helper(left, nums, val)
                i += 1
            else:
                left += 1
                i += 1
        
        return left
    
    def helper(self, idx, nums, val):
        while idx + 1 < len(nums):
            nums[idx] = nums[idx + 1]
            idx += 1
        
        nums[idx] = val
