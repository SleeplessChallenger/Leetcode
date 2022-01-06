# 1. Find the Duplicate Number
class Solution:
    # Modification & O(n) time
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            curr_abs = abs(num)
            if nums[curr_abs - 1] < 0:
                return curr_abs
            nums[curr_abs - 1] *= -1
            
    # Without modification
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

# 2. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1. Compute total & half
        2. Apply Binary Search on smaller array
        3. Calc. left partition (midd) for the bigger array
            without using BS: subtract left_part of the smaller
            from the total && don't forget that we deal with indicies
        4. Next, we need to know: if midd_element from smaller array
            is smaller than midd+1 element of the bigger array &&
            midd_element from bigger array is smaller that midd+1
            element if the smaller array
        5. Don't forget that indicies may go out of bounds:
            use `inf` to deal with it
        
        
        """
        if len(nums1) > len(nums2):
            return self.find_median(nums2, nums1)
        return self.find_median(nums1, nums2)
    
    def find_median(self, first, second):
        total_length = len(first) + len(second)
        half_length = total_length // 2
        
        left, right = 0, len(first) - 1
        
        while True:
            midd = left + (right - left) // 2
            
            midd_second = half_length - midd - 2
            # as we need index, so first 1 from first arr
            # and second 1 from second arr
            
            first_midd_val = first[midd] if midd >= 0 else float('-inf')
            first_midd_right_val = first[midd + 1] if midd + 1 <= len(first) - 1 else float('inf')
            
            second_midd_val = second[midd_second] if midd_second >= 0\
                else float('-inf')
            second_midd_right_val = second[midd_second + 1] if midd_second + 1 <= len(second) - 1\
                else float('inf')
            
            # partition is correct
            if first_midd_val <= second_midd_right_val and second_midd_val <= first_midd_right_val:
                # odd
                if total_length % 2 != 0:
                    return min(first_midd_right_val, second_midd_right_val)
                # even
                elif total_length % 2 == 0:
                    return (max(first_midd_val, second_midd_val) +\
                        min(first_midd_right_val, second_midd_right_val)) / 2
            
            elif first_midd_val > second_midd_right_val:
                right = midd - 1
            
            # else:
            elif second_midd_val > first_midd_right_val:
                left = midd + 1
