# 1. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        # [0,0,1,1,1,2,2,3,3,4]
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
                j += 1

        return i + 1

# 2. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. transpose
        # 2. swap columns in 2 pointers
        # manner moving to the middle
        # by traversing matrix row by row
        # and in every row we'll do that
        # 2 pointers method
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return self.reverse(matrix)
    
    def reverse(self, matrix):
        for i in range(len(matrix)):
            row = matrix[i]
            first = 0
            second = len(matrix[0]) - 1
            while first < second:
                row[first], row[second] = row[second], row[first]
                first += 1
                second -= 1
        
        return matrix

# 3. Best Time to Buy and Sell Stock II
class Solution:
    # single pass
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return  0
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, maxProfit + prices[i] - prices[i - 1])
        
        return maxProfit
 

    # peak & valley
    def maxProfit(self, prices: List[int]) -> int:
        peak = None
        valley = None
        i = 0
        maxProfit = 0
        # -1 as we need to look one ahead
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        
        return maxProfit

# 4. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = -1
        while (digits[i] // 10) != 0:
            withoutCarry = digits[i] % 10
            carry = digits[i] // 10
            
            digits[i] = withoutCarry
            i -= 1
            if abs(i) > len(digits) and carry != 0:
            # `>` as we use `-` initially and there
            # is no overlap with index
                digits.insert(0, carry)
            elif carry != 0:
                digits[i] += carry
        
        return digits
