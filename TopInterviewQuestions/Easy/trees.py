# 1. Symmetric Tree
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root.left, root.right)
    
    def isValid(self, leftTree, rightTree):
        if leftTree is None and rightTree is None:
            return True
        if leftTree is None or rightTree is None:
            return False
        # we'll visit this line and only after
        # THIS we'll go to recursive call check for `None`
        if leftTree.val != rightTree.val:
            return False

        return self.isValid(leftTree.left, rightTree.right) and\
            self.isValid(leftTree.right, rightTree.left)

# 2. Convert Sorted Array to Binary Search Tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.minHeight(nums, 0, len(nums) - 1)
    
    def minHeight(self, nums, left, right):
        if left > right:
            return None
        middle = (left + right) // 2
        node = TreeNode(nums[middle])
        # `-` & `+` are essential as without
        # them we'll get error
        node.left = self.minHeight(nums, left, middle - 1)
        node.right = self.minHeight(nums, middle + 1, right)
        return node

# 3. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result, queue = [], [root]
        
        while len(queue) != 0:
            result.append([node.val for node in queue])
            nextQueue = queue
            queue = []
        
            for node in nextQueue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
       
        return result
