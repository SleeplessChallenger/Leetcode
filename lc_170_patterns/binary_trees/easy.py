# 1. Merge Two Binary Trees

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is None or root2 is None:
            return root1 if not root2 else root2
        
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        
        return node

# 2. Minimum Depth of Binary Tree
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        leftCount = self.minDepth(root.left)
        rightCount = self.minDepth(root.right)
        
        if leftCount == 0:
            smallestCount = rightCount
        elif rightCount == 0:
            smallestCount = leftCount
        else:
            smallestCount = min(leftCount, rightCount)
        
        return 1 + smallestCount


# not mine
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        else:
            return min(self.minDepth(root.left),
                self.minDepth(root.right)) + 1

# 3. Path Sum
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # as we can get None as root node
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return targetSum == root.val
        
        return self.hasPathSum(root.left, targetSum - root.val) or\
            self.hasPathSum(root.right, targetSum - root.val)

# 4. Diameter of Binary Tree
class Help:
    def __init__(self, d, h):
        self.d = d
        self.h = h
    
    
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.traverse(root).d
        
    def traverse(self, root):  
        if root is None:
            return Help(0, 0)
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        longest = (left.h + right.h)
        curr = max(left.d, right.d)
        d = max(longest, curr)
        h = max(left.h, right.h) + 1
        
        return Help(d, h)

# 5. Average of Levels in Binary Tree
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        result = []
        
        while len(queue) != 0:
            length = len(queue)
            value = 0
            for i in range(length):    
                node = queue.pop(0)
                value += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(value / length)
        
        return result
