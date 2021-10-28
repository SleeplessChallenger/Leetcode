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

# 5. Single Number
class Solution:
        '''
At first, recommend you to skim through the following resources:
1. https://www.interviewcake.com/table-of-contents#section_bit-manipulation_concept_not
2. https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate

**Steps:**

take `[4,1,2,1,2]` as an example

1. ^ will do addition in bitwise manner.
2. But why do we need `result=0`? Why not simply `result=nums[0]` and start iteration from the second? => As I mentioned in the beginning, it is an addition. So, taking 4 and 1, it will give 5. But with `result=0` it'll give 4 at first,
then we add 1 and 2.
3. But then, we find duplicates of 1 and 2 which will be subtracted. Why? ^ gives 0 when 2 similar numbers are applied:
* 8 ^ 8 = 0

Okay, let me explain everything in more details.
Take binary representation: 
0000: 0
0001: 1
0010: 2
0011: 3
0100: 4
0101: 5
0110: 6
0111: 7
1000: 8
1001: 9
1010: 10

So, let's iterate over that array:
1. 0 ^ 4: we check bit by bit: 0 ^ 0 is 0 and 0 ^ 1 is 1, 1 ^ 1 is 0
	=> we get 0100 from it. To put it simply, 4

2. 4 ^ 1: 0100 ^ 0001 => 0101 which is 5
3. 5 ^ 2:  0101 ^ 0010 => 0111 which is 7
4. 7 ^ 1: 0111 ^ 0001 => 0110 which is 6
5.  6 ^ 2: 0110 ^ 0010 => 0100 which is 4

And 4 is our answer
        '''
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor

# 6. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
      # Time: O(n) Space: O(n)
      #   arr = [0 for _ in nums]
      #   i = 0
      #   for num in nums:
      #       if num != 0:
      #           arr[i] = num
      #           i += 1
                
      #   return arr

        # Time: O(n) Space: O(1)
        idxNotZero = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[idxNotZero] = nums[i]
                idxNotZero += 1
            
            i += 1
        
        while idxNotZero != len(nums):
            nums[idxNotZero] = 0
            idxNotZero += 1

# 7. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n) Space: O(1)
        k = k % len(nums)
        
        i = 0
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = 0
        j = k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = k
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

# 8. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == '.':
                    continue
                
                result = self.isValid(num, i, j, board)
                if not result:
                    return False

        return True
    
    def isValid(self, num, row, col, board):
        # in the following 2 checks we continue
        # if row == curr row or col == curr col
        for i in range(len(board[row])):
            if i == col:
                continue
            elif board[row][i] == num:
                return False
            
        for j in range(len(board)):
            if j ==  row:
                continue
            elif board[j][col] == num:
                return False
        
        rowGrid = row // 3
        colGrid = col // 3
        
        for i in range(3):
            for j in range(3):
                rowCheck = rowGrid * 3 + i
                colCheck = colGrid * 3 + j
                # if pos. of current number => skip
                if rowCheck == row and colCheck == col:
                    continue
                
                
                figure = board[rowCheck][colCheck]
                if figure == '.':
                    continue
                
                if num == figure:
                    return False
        
        return True

# 9. Intersection of Two Arrays II
class Solution:
    # Time: O(n)  Space: O(n)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht1 = {}
        ht2 = {}
        
        for num in nums1:
            if num not in ht1:
                ht1[num] = 0
            ht1[num] += 1
        
        for num in nums2:
            if num  not in ht2:
                ht2[num] = 0
            ht2[num] += 1
        
        result = []
        for i, j in ht1.items():
            if i in ht2:
                # take smallest of two values
                count = ht2[i] if ht2[i] < j else j
                while count != 0:
                    result.append(i)
                    count -= 1
        
        return result
    
    # Time: O(n*log n) Space: O(1)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        first = 0
        second = 0
        result  = []
        
        while first < len(nums1) and second < len(nums2):
            if nums1[first] > nums2[second]:
                second += 1
            elif nums1[first] < nums2[second]:
                first += 1
            else:
                result.append(nums1[first])
                first += 1
                second += 1
        
        return result
