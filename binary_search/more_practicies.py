# 1.  Find Minimum in Rotated Sorted Array II
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            midd = left + (right - left) // 2
            
            # if `right` > `midd` => move right as middle.
            # But we can't apply `-1` as maybe `midd` is
            # the smallest value
            if nums[midd] < nums[right]:
                right = midd
            
            # if `right` < `midd` => move left && add + 1
            # as `midd` is already bigger than right, hence
            # at least we have right as smaller and need to
            # check from `midd + 1`
            elif nums[midd] > nums[right]:
                left = midd + 1
            
            # if figures are equal, move right
            # bound one left as at least we have
            # `midd` which is equal
            elif nums[midd] == nums[right]:
                right -= 1
        
        return nums[left]

# 2. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        if len(nums1) > len(nums2):
            return self.check_nums(nums2, nums1)
        
        return self.check_nums(nums1, nums2)
    
    def check_nums(self, small, big):
        small_set = set(small)
        big_set = set(big)
        result = list()
        
        for num in small_set:
            if num in big_set:
                result.append(num)
        
        return result

# 3. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.get_numbers(nums2, nums1)
        return self.get_numbers(nums1, nums2)
    
    def get_numbers(self, small, big):
        ht = {}
        for num in big:
            if num not in ht:
                ht[num] = 0
            ht[num] += 1
        
        result = list()
        for num in small:
            if num in ht and ht[num] != 0:
                result.append(num)
                ht[num] -= 1
                
        return result
