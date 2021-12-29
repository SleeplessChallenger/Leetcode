# 1. Search for a Range
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        self.search_nums(nums, result, target, True)
        self.search_nums(nums, result, target, False)
        
        return result
    
    def search_nums(self, nums, result, t, go_left):
        left = 0
        right = len(nums) - 1
        while left <= right:
            midd = (left + right) // 2
            
            if nums[midd] < t:
                left = midd + 1
            elif nums[midd] > t:
                right = midd - 1
            else:
                # `go back` as we have 2 conditions which
                # prevent us from success: a) midd is edge (
                # either first or last idx) b) midd-1/midd+1
                # != target. Also, keep in mind that this `else`
                # does mean `midd` == target
                if go_left:

                    if midd == 0 or nums[midd - 1] != t:
                        result[0] = midd
                        return
                    else:
                        right = midd - 1
                else:
                    if midd == len(nums) - 1 or nums[midd + 1] != t:
                        result[1] = midd
                        return
                    else:
                        left = midd + 1
                # why use right in LEFT chunk and left in RIGHT?
                # => we need to find borders and if we `go_left`, we
                # don't care about right half of the array, We need
                # new right to calc. new `midd`

# 2. Find K Closest Elements
class Solution:
    # Time: O(n*log n)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sort by least space between num & x
        result = sorted(arr, key=lambda num: abs(num-x))
        output = []
        
        for i in range(k):
            output.append(result[i])
        
        # sort again as we can have them
        # in unsorted order
        return sorted(output)
    
    # Time: O(log n)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        left = bisect_left(arr,x) - 1
        right = left + 1
        
        while right - left - 1 < k:
            # we expand to the right if left
            # bound is met. In result we'll
            # have right idx used in return
            if left == -1:
                right += 1
                continue
            
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # + 1 as we definitely need one step ahead
        # due to either left == -1 or left being
        # not in correct position
        return arr[left+1:right]
    
    # Time: O(log n)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        # max bound for left (max index left bound can take) can be 
        # length of the whole arr - k elements
        right = len(arr) - k
        
        while left < right:
        # [1]; `<` prevent us from error
            midd = (left + right) // 2
            # midd & midd + k: only one of them can
            # move at a time
            # if left side has bigger diff
            # than right side => move left pointer
            # to the right, vice versa
            if x - arr[midd] > arr[midd+k] - x:
                left = midd + 1
            else:
                # if diff of the `left` <= `right`
                right = midd
        
        return arr[left:left+k]
