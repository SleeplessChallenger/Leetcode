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

# 2. easy  - Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # don't sort
        temp = nums[0]
        total =  nums[0]
        for i in range(1, len(nums)):
            temp = max(temp  + nums[i], nums[i])
            total = max(temp, total)
        
        return total
+ look at  d. & c.

# 3. easy - Contains duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for val in nums:
            if val in ht:
                return True
            ht[val] = True
        
        return False

# 4. easy - Best Time to Buy and Sell stock
        def maxProfit(self, prices: List[int]) -> int:
            minPrice = float('inf')
            maxProfit = 0
            for i in range(len(prices)):
                if prices[i] < minPrice:
                    minPrice = prices[i]
                elif maxProfit < prices[i] - minPrice:
                    maxProfit = prices[i] - minPrice
            
            return maxProfit
