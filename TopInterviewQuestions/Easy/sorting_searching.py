# 1. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        m -= 1
        n -= 1
        
        while idx >= 0:
            if m < 0:
                nums1[idx] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[idx] = nums1[m]
                m -= 1
            else:
                if nums1[m] > nums2[n]:
                    nums1[idx] = nums1[m]
                    m -= 1
                else:
                    nums1[idx] = nums2[n]
                    n -= 1
            idx -= 1

# 2. First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n)
        if n == 0:
            return 0
        if n == 1:
            if isBadVersion(n):
                return 1
        
        for i in range(1, n + 1):
            if isBadVersion(i) == True:
                return i
        
        # Optimal. As we're said that after one bad
        # version we get all bad -> use binary search 
        # to trim useless parts
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle) == True:
                right = middle - 1
            # if there is bad to the right
            # => move left to find bad
   
            else:
                left = middle + 1
        
        return left
