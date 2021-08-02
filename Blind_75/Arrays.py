# 1. easy - Two Sum
# Time: O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1
        while i < len(nums):
            while j < len(nums):
                total = nums[i] + nums[j]
                if total == target:
                    return [i, j]
                j += 1
            i += 1
            j = i + 1

# Time: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ht:
                return [i, ht[diff]]

        	ht[nums[i]] = i
