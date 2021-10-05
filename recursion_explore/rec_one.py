# 1. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:  
        self.helper(s, 0, len(s) - 1)
    
    def helper(self, string, i, j):
        if i >= j:
            return
        string[i], string[j] = string[j], string[i]
        return self.helper(string, i+1, j-1)

# 2. Swap Nodes in Pairs
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        afterNext = head.next.next
        nx = head.next
        
        head.next = self.swapPairs(afterNext)
        nx.next = head
        
        return nxclass Solution:

# 3. Search in a Binary Search Tree
class Solution:
    # less optimal
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return False
        
        elif root.val == val:
            return root
        
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        
        if not left and not right:
            return None
        return left if not right else right
    
    # more optimal
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root

# 4. Pascal's Triangle II
class Solution:
    # iterative
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        for i in range(1, rowIndex + 1):
            curr = [1]
            for j in range(1, i):
                curr.append(result[i - 1][j - 1] +
                            result[i - 1][j])
            
            curr.append(1)
            result.append(curr)
        
        return result[rowIndex]
    
    # recursive
    def getRow(self, rowIdx: int) -> List[int]:
        if rowIdx == 0:
        # reach here only when
        # rowIdx initially is 0
            return [1]
        if rowIdx == 1:
        # reach here generally
            return [1, 1]
        result = self.getRow(rowIdx - 1)
        return [result[0]] + \
            [result[i] + result[i + 1] for i in range(len(result) - 1)] + \
                [result[-1]]

# 5. Pow(x, n)
class Solution:
    # brute-force
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            # make positive
            n = -n
        total = 1
        for i in range(n):
            total *= x
        
        return total
    
    # fast-power
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        return self.pow(x, n)
    
    def pow(self, x, n):
        if n == 0:
            return 1
        
        half = self.pow(x, n//2)
        
        if int(n % 2) == 0:
            return half * half
        else:
            return half * half * x

# 6. K-th Symbol in Grammar
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        isOdd = k % 2 == 1

        if parent == 1:
            return 1 if isOdd else 0
        else:
            return 0 if isOdd else 1

# 7. Unique Binary Search Trees II
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
