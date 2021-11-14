# Duplicate Zeros
class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        '''
        1. we start from the beginning
        2. if curr num isn't 0=> increase by 1
        3. if it's: go into helper where:
            - traverse from the end and
                shift values by 1
            - after that we need to increase by 2
                our i. Why? => we shifted 0 as well
                hence without increasing by 2 => all 0
        '''
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                self.helper(nums, i + 1)
                i += 2
            else:
                i += 1
    
    def helper(self, nums, idx):
        for i in reversed(range(idx, len(nums))):
            nums[i] = nums[i-1]
