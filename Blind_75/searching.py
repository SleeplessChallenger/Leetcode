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
