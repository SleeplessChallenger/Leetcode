# 1. add strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        total: int = 0
        carry: int = 0
        result: list = list()
        
        i: int = len(num1) - 1
        j: int = len(num2) - 1
        
        while i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                # total += int(num1[i])
                total += ord(num1[i]) - ord('0')
            if j >= 0:
                # total += int(num2[j])
                total += ord(num2[j]) - ord('0')
            
            result.append(str(total % 10))
            carry = total // 10
            
            i -= 1
            j -= 1
        
        if carry > 0:
            result.append(str(carry))
        
        # return ''.join(list(reversed(result)))
        return ''.join(str(num) for num in result[::-1])

# 2. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        small: int = 0
        big: int = 0
        
        while small < len(s):
            flag: bool = False
            while big < len(t):
                if s[small] == t[big]:
                    flag = True
                    break
                
                big += 1
            
            if not flag:
                return False
            
            small += 1
            big += 1
        
        return True

# 3. Summary Ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        
        slow: int = 0
        fast: int = 1
        
        result = list()
        
        while fast < len(nums):
            slow_val: int = nums[fast-1]
            fast_val: int = nums[fast]
                
            if (fast_val - slow_val) > 1:
                self._process_gap(slow, fast-1, nums, result)
                slow = fast
                fast += 1
            else:
                fast += 1
        
        self._process_gap(slow, fast-1, nums, result)
        return result
    
    def _process_gap(self, lo: int, high: int, nums, result) -> None:
        first_val: int = nums[lo]
        last_val: int = nums[high]
        if first_val == last_val:
            gap: str = f"{first_val}"
        else:
            gap: str = f"{first_val}->{last_val}"
        result.append(gap)

# 4. Max Stack
import heapq


class MaxStack:
    """
    [5,1,5]
        5
       / \
      1   5
     
    [5,1]
        5
       /
      1
    """

    def __init__(self):
        self.soft_deleted = set()
        self.max_heap = []
        self.recency_stack = []
        self.next_id = 0
        
    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.recency_stack.append((x, self.next_id))
        self.next_id -= 1

    def _clean_up(self):
        while self.recency_stack and self.recency_stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.recency_stack.pop()[1])
        while self.max_heap and self.max_heap[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.max_heap)[1])

    def pop(self) -> int:
        """
        1. remove from stack
        2. find this ele in heap - remove
        3. but don't do anything to stack
        """
        value, time = self.recency_stack.pop()
        self.soft_deleted.add(time)
        self._clean_up()
        return value
        
    def top(self) -> int:
        return self.recency_stack[-1][0]

    def peekMax(self) -> int:
        return -self.max_heap[0][0]
        
    def popMax(self) -> int:
        """
        1. remove from heap
        2. find this ele in stack - remove
        3. but don't do anything with heap as we've already removed
        
        Also, heap will be recalibrated after this method
        """
        value, time = heapq.heappop(self.max_heap)
        self.soft_deleted.add(time)
        self._clean_up()
        return value * -1
