# 1. Majority Element
class Solution:
    # Time: O(n) Space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 0
            ht[num] += 1
    
        # first way
        return max(ht, key=ht.get)
    
        # second way
        result = float('-inf')
        biggest_key = None
        for key, value in ht.items():
            if value > result:
                result = value
                biggest_key = key
        
        return biggest_key
    
    # Time: O(n) Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate
