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

# 3. Kth Largest Element in an Array
class Solution:
    # Time: O(n*log n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        1. put values in ht with coutn of occurence
        2. keep max value
        3. start loop by checking if we've reached k AND max_value
            is in ht as the following example may ruin:
            [-1,2,0]  k = 2
        4. if curr max_value NOT in ht: just decrease count
            else:
            4.1 decrease k
            4.2 decrease count of max_value in ht
            4.3 ONLY if count in ht is 0, decrease max_value
            4.4 else proceed with current max_value as duplicates
                are considered unique
            
        """
        ht = {}
        max_value = float('-inf')
        
        for num in nums:
            max_value = max(num, max_value)
            if num not in ht:
                ht[num] = 0
            ht[num] += 1
        
        while True:
            if k == 1 and max_value in ht:
                return max_value
            
            if max_value in ht:
                k -= 1
                ht[max_value] -= 1
                if ht[max_value] == 0:
                    max_value -= 1
                else:
                    continue
            else:
                max_value -= 1

    # Quickselect
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        return self._find_target_element(nums, target, 0, len(nums)-1)
    
    def _find_target_element(self, nums, target, start, end):
        while True:
            pivot = start
            left = pivot + 1
            right = end
            
            while left <= right:
                if nums[pivot] < nums[left] and nums[pivot] > nums[right]:
                    self.swap(nums, left, right)
                if nums[pivot] >= nums[left]:
                    left += 1
                if nums[pivot] <= nums[right]:
                    right -= 1
            
            self.swap(nums, right, pivot)
            if right > target:
                end = right - 1
            elif right < target:
                start = right + 1
            else:
                return nums[target]
                
    def swap(self, nums, l, r):
        nums[l], nums[r] = nums[r], nums[l]

# 4. Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeInfo:
    def __init__(self, height, is_balanced):
        self.height = height
        self.is_balanced = is_balanced


class Solution:
    # first way
    def isBalanced(self, root: TreeNode) -> bool:
        return self.traverseTree(root).is_balanced
    
    def traverseTree(self, root):
        if root is None:
            return TreeInfo(-1, True)
        
        left_branch = self.traverseTree(root.left)
        right_branch = self.traverseTree(root.right)
        
        curr_is_balanced = left_branch.is_balanced and\
            right_branch.is_balanced and\
            abs(left_branch.height - right_branch.height) <= 1
        
        curr_height = 1 + max(left_branch.height, right_branch.height)
        
        return TreeInfo(curr_height, curr_is_balanced)
    
    # second way
    def isBalanced(self, root: TreeNode) -> bool:
        def count_levels(node):
            if node is None:
                return 0
            
            return max(count_levels(node.left), count_levels(node.right)) + 1
        
        if root is None:
            return True
        
        return abs(count_levels(root.left) - count_levels(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)

# 5. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Space: O(n); Time: O(n)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        all_nodes = list()
        
        def traverse(node):
            if node is not None and node.val >= low and node.val <= high:
                all_nodes.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        traverse(root)
        total = 0
        
        for node in all_nodes:
            total += node
        
        return total
        
# More optimal        
class Solution:
    def __init__(self):
        self.result = 0
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        return sum of `node.val` that are inside [low, high]
        """
        self.find_sum(root, low, high)
        
        return self.result

    def find_sum(self, node, low, high):
        if not node:
            return
        
        if node.val >= low and node.val <= high:
            self.result += node.val
         
        if node.val > low:
            self.find_sum(node.left, low, high)
        
        if node.val < high:
            self.find_sum(node.right, low, high)
        
        return

# 6. Sum of Left Leaves
class Solution:
    # Recursive O(n)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        we need to count only LEAVES nodes
        """
        self.count = 0
        self.start_traversal(root)
        return self.count
    
    def start_traversal(self, node):
        if node.left and node.left.left is None and node.left.right is None:
            self.count += node.left.val
        if node.left:
            self.start_traversal(node.left)
        if node.right:
            self.start_traversal(node.right)
    
    # Iterative
    def __init__(self):
        self.stack = list()
        self.total = 0
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        check beforehand that `.left` is a leaf node. Hence if we
        put that `leaf` node on the stack, it won't be added second
        time as our check: `if node.left && it's a leaf`
        """
        self.traverse_tree(root)
        
        return self.total
    
    def traverse_tree(self, node):
        self.stack.append(node)
        
        while len(self.stack) != 0:
            curr = self.stack.pop()
            print(curr.val, self.total)
            if curr.left and\
                curr.left.left is None and curr.left.right is None:
                self.total += curr.left.val
            
            if curr.right:
                self.stack.append(curr.right)
            
            if curr.left:
                self.stack.append(curr.left)
    
    # Morris Traversal
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        while root:
            if not root.left:
                root = root.right
            else:
                curr_left_previous = root.left
                if curr_left_previous.left is None and curr_left_previous.right is None:
                    total += curr_left_previous.val
                
                # we still need to enter this chunk. Why?
                # ->    3 - root
                #      /
                #    9  Hence we create link from 9 to 3 and then return
                #   to the root from 9
                while curr_left_previous.right and curr_left_previous.right != root:
                    curr_left_previous = curr_left_previous.right

                if not curr_left_previous.right:
                    curr_left_previous.right = root
                    root = root.left
                else:
                    curr_left_previous.right = None
                    root = root.right
        
        return total

# 7. Unique Binary Search Trees
class Solution:
    # first ver
    def numTrees(self, n: int) -> int:
        return self.find_nums(n, {0: 1})
    
    def find_nums(self, n, memo):
        if n in memo:
            return memo[n]
        
        counter = 0
        # both ways work
        # for left in range(n):
        for left in reversed(range(n)):
            right = n - left - 1
            left_counter = self.find_nums(left, memo)
            right_counter = self.find_nums(right, memo)
            counter += left_counter * right_counter
        
        memo[n] = counter
        return counter

    # second ver
    def numTrees(self, n: int) -> int:
        memo = [1 for _ in range(n + 1)]
        
        for nodes in range(2, n + 1):
            total_nodes = 0
            for root in range(1, nodes + 1):
                left_nodes = root - 1
                right_nodes = nodes - root
                
                total_nodes += memo[left_nodes] * memo[right_nodes]
            
            memo[nodes] = total_nodes
        
        return memo[n]

# 8. Unique Binary Search Trees II
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.rec(1, n) if n else []
    
    def rec(self, i, j):
        if i > j:
            return [None]
        
        trees = []
        for idx in range(i, j + 1):
            left_ = self.rec(i, idx - 1)
            right_ = self.rec(idx + 1, j)
            for l in left_:
                for r in right_:
                    node = TreeNode(idx)
                    node.left = l
                    node.right = r
                    trees.append(node)
        
        return trees

# 9. Find Winner on a Tic Tac Toe Game
class Solution:
    # brute-force
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        board = [[0] * n for _ in range(n)]
        
        player = 1
        
        for move in moves:
            row, col = move
            board[row][col] = player
            
            if self._check_row(row, player, board) or\
                self._check_col(col, player, board) or\
                (row == col and self._check_diag(player, board)) or\
                (row + col == n - 1 and self._check_anti_diag(player, board)):
                    return 'A' if player == 1 else 'B'
            
            player *= -1
        
        return "Draw" if len(moves) == 9 else "Pending"
        
    def _check_row(self, row, pl, board) -> bool:
        for c in range(3):
            if board[row][c] != pl:
                return False
            
        return True
    
    def _check_col(self, col, pl, board) -> bool:
        for r in range(3):
            if board[r][col] != pl:
                return False
        
        return True
    
    def _check_diag(self, pl, board) -> bool:
        for r in range(3):
            if board[r][r] != pl:
                return False
        
        return True
    
    def _check_anti_diag(self, pl, board) -> bool:
        for r in range(3):
            if board[r][3-1-r] != pl:
                return False
        
        return True

    # optimal
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        1. Calc. sum for every row/col/diag
        2. As players have the opposing figures, it's very convenient
        3. Each col/row set has up to 3 -> nested
        """
        n = 3
        
        player = 1
        
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        for move in moves:
            row, col = move
            
            rows[row] += player
            cols[col] += player
            
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player
            
            result: bool = self._find_result(
                rows[row], cols[col], diag, anti_diag, n
            )
                
            if result:
                return "A" if player == 1 else "B"
            
            player *= -1
        
        return "Draw" if len(moves) == n * n else "Pending"
    
    def _find_result(self, row, col, diag, anti_diag, n) -> bool:
        return any(map(lambda x: abs(x) == n, [row, col, diag, anti_diag]))

# 10. 4 Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def k_sum(k: int, start: int, target: int):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    # why ` - k` ? If k is 4 -> take first and
                    # allow 3 others to be taken after to form a quad
                    
                    # below: if 2 nums are duplicated, but placed to each other -> Ok
                    # but if at least 1 index diff -> enter
                    if i > start and nums[i] == nums[i-1]:
                        continue

                    quad.append(nums[i])
                    k_sum(k-1, i+1, target-nums[i])
                    quad.pop()
                return

            # base case
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    results.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        nums.sort()
        results = list()
        quad = list()
        
        k_sum(4, 0, target)
            
        return results
