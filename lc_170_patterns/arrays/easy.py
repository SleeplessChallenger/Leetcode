# 1. Find All Numbers Disappeared in an Array
class Solution:
    # Time: O(n) Space: O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ht = {}
        for num in nums:
            ht[num] = True
        
        result = []
        for idx in range(1, len(nums) + 1):
            if idx not in ht:
                result.append(idx)
        
        return result
    
    ####
    # Time: O(n) Space: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] > 0:
                nums[abs_num - 1] *= - 1

        result = []
        for idx in range(len(nums)):
            num = nums[idx]
            if num > 0:
                result.append(idx + 1)

        return result

# 2. Range Sum Query - Immutable
class NumArray:
    # Uses `sumRange` as O(n)
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for idx in range(left, right + 1):
            num = self.nums[idx]
            total += num
        
        return total
    
    # Uses `sumRange` as O(1)
    def __init__(self, nums: List[int]):
        self.numbers = []
        temp_sum = 0
        for num in nums:
            # we accumulate sum so that
            # indicies can be used
            temp_sum += num
            self.numbers.append(temp_sum)
            
        
    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.numbers[right] - self.numbers[left - 1]
        else:
            # the one which is not 0 will be chosen
            return self.numbers[right or left]

# 3. Peak Index in a Mountain Array
class Solution:
    
    # as `0 < i < len(arr) - 1`, we can check
    # for prev & next values
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i
    
    # Binary Search
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle
        
        return left

 # 4. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0 for _ in nums]
        left = 0
        right = len(nums) - 1
        
        for i in reversed(range(len(nums))):
            leftNum = nums[left]
            rightNum = nums[right]
            if abs(leftNum) > abs(rightNum):
                arr[i] = leftNum * leftNum
                left += 1
            else:
                arr[i] = rightNum * rightNum
                right -= 1
        
        return arr
