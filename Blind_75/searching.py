# middle chunk
# 1. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            
            elif nums[middle] >= nums[left]:
            # means all numbers from left to middle are sorted
                if nums[left] <= target and target < nums[middle]: 
                    right = middle - 1
                else:
                    left = middle + 1
                
            elif nums[middle] < nums[right]:
            # means all numbers from middle to right are sorted
                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1

# 2.  Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        if nums[right] > nums[left]:
            # no rotation
            return nums[left]
        
        while left <= right:
            middle = (left + right) // 2
            
            # as even with `[4, 3]` middle is
            # to the left (4 in this case) =>
            # middle + 1 is safe
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            # hence middle is smaller than next one
            # and if it's smaller than prev => return
            # here middle being 0 becomes -1
            # in `nums[middle - 1]`
            elif nums[middle] < nums[middle - 1]:
                return nums[middle]
            
            elif nums[middle] > nums[left]:
                # go right as before middle everything is growing
                left = middle + 1
            elif nums[middle] < nums[right]:
                # go left as after middle all increase
                right = middle - 1
