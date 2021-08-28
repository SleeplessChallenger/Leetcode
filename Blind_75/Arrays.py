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

# Kadane's Algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # don't sort
        temp = nums[0]
        total =  nums[0]
        for i in range(1, len(nums)):
            temp = max(temp  + nums[i], nums[i])
            total = max(temp, total)
        
        return total

# DP
def maxSubArray(self, nums: List[int]) -> int:
    dp = [0 for _ in nums]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] + nums[i] > nums[i]:
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = nums[i]

    return max(dp)

# D & C
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        middle = len(nums) // 2
        leftPart = self.maxSubArray(nums[:middle])
        rightPart = self.maxSubArray(nums[middle:])
        bothParts = self.findMax(nums, middle)
        # opt between single numbers (leftPart/rightPart
        # or the best sum out of them)
        return max(leftPart, rightPart, bothParts)

    def findMax(self, arr, middle):
        temp1 = temp2 = 0
        sum1 = float('-inf')
        
        for i in range(middle - 1, -1, -1):
            temp1 += arr[i]
            sum1 = max(sum1, temp1)

        sum2 = float('-inf')
        for j in range(middle, len(arr)):
            temp2 += arr[j]
            sum2 = max(sum2, temp2)

        return sum1 + sum2

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
        # mine
            minPrice = prices[0]
            best = 0
            for i in range(1, len(prices)):
                if minPrice > prices[i]:
                    minPrice = prices[i]
                else:
                    best = max(best, -minPrice + prices[i])
            
            return best
        
        # not mine
            minPrice = float('inf')
            maxProfit = 0
            for i in range(len(prices)):
                if prices[i] < minPrice:
                    minPrice = prices[i]
                elif maxProfit < prices[i] - minPrice:
                    maxProfit = prices[i] - minPrice
            
            return maxProfit

# Medium chunk

# 1. medium - 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        target = 0
        ht = {}
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                totalSum = nums[i] + nums[left] + nums[right]
                if totalSum == target:
                    ht[f"{nums[i]}, {nums[left]}, {nums[right]}"] = [nums[i], nums[left], nums[right]]
                    left += 1
                    right -= 1
                elif totalSum > target:
                    right -= 1
                else:
                    left += 1
        
        return list(ht.values())

# 2. Container With Most Water
class Solution:
    # Time: O(n^2) Space: O(1)
#     def maxArea(self, height: List[int]) -> int:
#         max_water = float('-inf')
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 first_barrier = height[i]
#                 second_barrier = height[j]
#                 smallest_barrier = min(first_barrier, second_barrier)
#                 difference = j - i
#                 max_water = max(max_water, difference * smallest_barrier)
        
#         return max_water

    # Time: O(n) Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = float('-inf')
        
        while left < right:
            left_value = height[left]
            right_value = height[right]
            
            difference = abs(left - right)
            smallest = min(left_value, right_value)
            max_water = max(max_water, difference * smallest)
            
            if left_value < right_value:
                left += 1
            else:
                right -= 1
        
        return max_water
   
