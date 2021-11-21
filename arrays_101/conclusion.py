# 1. Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                count += 1
        
        return count

# 2. Max Consecutive Ones II
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # v1
#         if len(nums) < 2:
#             return 1
        # we need right as 0:
    # [0, 0] in this case edge case check won't help
        right = 0
        left = 0
        longest = 0
        zeroIdx = 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeroIdx += 1
            
            while zeroIdx == 2:
                # if left != 0: just move right
                # elif 0: decrease count & move right
                if nums[left] == 0:
                    zeroIdx -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest

# 3. Third Maximum Number
class Solution:
    # ver 1. Time: n*log(n) Space: O(n)
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        
        # python 3.6+ hash table keeps in order
        # as OrderedDict
        ht = {}
        for num in nums:
            ht[num] = True
        
        if len(ht) < 3:
            return max(list(ht.keys()))
        
        return list(ht.keys())[-3]
    
    # ver 2. Set and Delete
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        
        max_num = max(nums)
        
        if len(nums) < 3:
            return max_num
        
        nums.remove(max_num)
        sec_max = max(nums)
        nums.remove(sec_max)
        th_max = max(nums)
        
        return th_max
    
     # ver 3. Max set
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        
        for i in range(3):
            max_curr = self.find_max(seen, nums)
            if max_curr is None:
                return max(seen)
            seen.add(max_curr)
        
        return min(seen)
    
    def find_max(self, seen, nums):
        m_c = None
        for num in nums:
            if num in seen:
                continue
            if m_c is None or m_c < num:
                m_c = num
        
        return m_c
    
    # ver 4. One set
    def thirdMax(self, nums: List[int]) -> int:
        res = set()
        
        for num in nums:
            if num in res:
                continue
            res.add(num)
            self.check(res)
        
        return min(res) if len(res) == 3 else max(res)
    
    def check(self, res):
        if len(res) > 3:
            res.remove(min(res))
