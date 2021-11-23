# 1. Maximum Depth of N-ary Tree
class Solution:
    # recursive
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:
            return 0
        
        elif root.children == []:
            return 1
    
        for child in root.children:
            result = 1 + self.maxDepth(child)
            depth = max(depth, result)
        
        return depth
    
    # iterative
    def maxDepth(self, root: 'Node') -> int:
        queue = []
        if root:
            queue.append((1, root))
        
        depth = 0
        while len(queue) != 0:
            curr_depth, node = queue.pop(0)
            if node:
                depth = max(depth, curr_depth)
                
                for v in node.children:
                    queue.append((curr_depth + 1, v))
        
        return depth

##
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n - 1, k/2 + k % 2)
        # a) 3/2 = 1.5; 1.5 +  b) 4/2 = 2; 2 + 4 % 2 = 2
        isOdd = k % 2 == 1
        if parent == 1:
            return 1 if isOdd else 0
        else:
            return 0 if isOdd else 1

# 2. Kth Missing Positive Number
class Solution:
    # Time: O(n) Space: O(n)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lastValue = arr[-1]
        
        ht = self.put_values(lastValue) # O(n)
        
        count = 0
        nums = set(arr) # for O(1) time checks
        
        for val in ht.keys(): # O(n)
        # Python 3.6 + hasht_table is ordered
        # => we need this property
        # Otherwise use OrderedDict
            if val not in nums:
                count += 1
            
            if count == k:
                return val
        
        # this part for cases when: [1,2,3,4]; k = 2
        # => we need to traverse for non-exisitng values
        
        while count != k: # O(n)
            lastValue += 1
            count += 1
            
        return lastValue

    def put_values(self, value):
        ht = {}
        for i in range(1, value):
            ht[i] = True
        
        return ht
    
    # Time: O(n)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0] - 1:
            return k
        
        k -= arr[0] - 1
        
        for i in range(len(arr) - 1):
            # next - curr - 1
            # I.e. [7,11]: 11 - 7 = 4. 4 - 1 = 3
            curr_missing = arr[i + 1] - arr[i] - 1
            if curr_missing >= k:
                return arr[i] + k
            
            k -= curr_missing
        
        return arr[-1] + k
    
    # Time: O(log n)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # value - idx - 1: [2,3,4,7,11]. 7 - 3 - 1 = 3 => 1,5,6
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            pivot = (right + left) // 2
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return left + k
