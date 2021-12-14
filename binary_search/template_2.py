# 1. First Bad Version
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            midd = (left + right) // 2
            result = isBadVersion(midd)

            if result is False:
                left = midd + 1
            # if it's True, we need to check midd-1 index
            elif isBadVersion(midd - 1) is False:
                return midd
            else:
                right = midd - 1

# 2. Find Peak Element
class Solution:
    # O(n) linear search
    def findPeakElement(self, nums: List[int]) -> int:    
        '''
        nums adjacent figures are NEVER equal => we need to compare only
        with the next value and ignore previous for 3 reasons:
        1. ascending line: peak is the last element
        2. descending line: peak is the first element
        3. swinging: we can reach peak ONLY when previous is smaller
            than current. Hence, if CURR > next, it's automatically
            is bigger than previous.
            I.e. [7,3,8]: 0; [1,2,]
        '''
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        
        return len(nums) - 1
            
            
    
    # optimal with Binary Search
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            midd = (left + right) // 2
            
            if nums[midd] < nums[midd + 1]:
                # ascending
                left = midd + 1
            
            elif nums[midd] > nums[midd + 1]:
                # descending
                right = midd
        
        return left

